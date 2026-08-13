#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
URL design language extractor for Smart UI Designer.
"""

import argparse
import csv
import hashlib
import html
import json
import re
import sys
import urllib.request
from collections import Counter
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

DATA_DIR = Path(__file__).parent.parent / "data"
EXTRACTED_DIR = DATA_DIR / "extracted"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

STYLE_FIELDS = ["Style Name", "Category", "Keywords", "Colors", "Effects", "Best For", "Complexity", "Accessibility"]
COLOR_FIELDS = ["Theme Name", "Primary", "Secondary", "Accent", "Background", "Foreground", "Border", "Notes"]
INDEX_FIELDS = ["Slug", "Name", "Source URL", "Extracted At", "Tags", "Tokens Path", "Preview Path"]

COMMON_COMPONENTS = {
    "Button": ["button", "btn", "cta"],
    "Card": ["card", "tile", "panel"],
    "Navigation": ["nav", "navbar", "menu", "header"],
    "Input": ["input", "search", "form", "field"],
    "Modal": ["modal", "dialog", "overlay"],
    "Tag": ["tag", "chip", "badge", "pill"],
}


def _slugify(value):
    value = (value or "").strip().lower()
    value = re.sub(r"^https?://", "", value)
    value = re.sub(r"[^a-z0-9一-鿿_-]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    if not value:
        value = "extracted"
    return value[:60]


def _read_url(url):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=20) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        body = response.read(2_000_000)
    return body.decode(charset, errors="replace")


def _extract_title(markup, url):
    match = re.search(r"<title[^>]*>(.*?)</title>", markup, re.I | re.S)
    if match:
        title = re.sub(r"\s+", " ", html.unescape(match.group(1))).strip()
        if title:
            return title[:80]
    host = urlparse(url).netloc.replace("www.", "")
    return host or "Extracted Style"


def _normalize_hex(value):
    value = value.strip().lower()
    if re.fullmatch(r"#[0-9a-f]{3}", value):
        return "#" + "".join(ch * 2 for ch in value[1:])
    if re.fullmatch(r"#[0-9a-f]{6}", value):
        return value.upper()
    return None


def _rgb_to_hex(match):
    parts = [int(float(match.group(i))) for i in range(1, 4)]
    return "#" + "".join(f"{max(0, min(255, p)):02X}" for p in parts)


def _extract_colors(markup):
    colors = []
    for raw in re.findall(r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?\b", markup):
        normalized = _normalize_hex(raw)
        if normalized and normalized not in {"#FFFFFF", "#000000"}:
            colors.append(normalized)
    for match in re.finditer(r"rgba?\(\s*([0-9.]+)\s*,\s*([0-9.]+)\s*,\s*([0-9.]+)", markup, re.I):
        color = _rgb_to_hex(match)
        if color not in {"#FFFFFF", "#000000"}:
            colors.append(color)
    counts = Counter(colors)
    ranked = [color for color, _ in counts.most_common(12)]
    return ranked or ["#2563EB", "#111827", "#F9FAFB", "#E5E7EB"]


def _extract_font_families(markup):
    fonts = []
    for match in re.finditer(r"font-family\s*:\s*([^;}{]+)", markup, re.I):
        font = re.sub(r"['\"]", "", match.group(1)).strip()
        font = re.sub(r"\s+", " ", font)
        if font and len(font) < 120:
            fonts.append(font)
    google_fonts = re.findall(r"fonts\.googleapis\.com/css[^\"']*family=([^&\"']+)", markup, re.I)
    for font in google_fonts:
        fonts.append(font.replace("+", " "))
    if not fonts:
        return {"heading": "system-ui, -apple-system, BlinkMacSystemFont, sans-serif", "body": "system-ui, -apple-system, BlinkMacSystemFont, sans-serif"}
    ranked = Counter(fonts).most_common(2)
    body = ranked[0][0]
    heading = ranked[1][0] if len(ranked) > 1 else body
    return {"heading": heading, "body": body}


def _extract_numbers(pattern, markup, limit=8):
    values = []
    for match in re.finditer(pattern, markup, re.I):
        try:
            value = int(float(match.group(1)))
        except ValueError:
            continue
        if 0 <= value <= 96:
            values.append(value)
    return [value for value, _ in Counter(values).most_common(limit)]


def _extract_shadows(markup):
    shadows = []
    for match in re.finditer(r"box-shadow\s*:\s*([^;}{]+)", markup, re.I):
        shadow = re.sub(r"\s+", " ", match.group(1)).strip()
        if shadow and shadow != "none" and len(shadow) < 160:
            shadows.append(shadow)
    return [shadow for shadow, _ in Counter(shadows).most_common(4)]


def _detect_components(markup):
    lowered = markup.lower()
    found = []
    for component, needles in COMMON_COMPONENTS.items():
        if any(needle in lowered for needle in needles):
            found.append(component)
    return found


def _infer_effects(tokens):
    effects = []
    if tokens["shadows"]:
        effects.append("阴影层级")
    if tokens["radii"] and max(tokens["radii"]) >= 12:
        effects.append("大圆角")
    if re.search(r"gradient|linear-gradient|radial-gradient", tokens.get("raw_sample", ""), re.I):
        effects.append("渐变背景")
    if len(tokens["colors"]["palette"]) >= 5:
        effects.append("多层次色板")
    return "、".join(effects) if effects else "克制视觉层级、统一组件状态"


def extract_tokens(url, name=None, slug=None, tags=None):
    markup = _read_url(url)
    title = name or _extract_title(markup, url)
    slug = _slugify(slug or name or urlparse(url).netloc or title)
    palette = _extract_colors(markup)
    fonts = _extract_font_families(markup)
    radii = _extract_numbers(r"border-radius\s*:\s*([0-9.]+)px", markup)
    spacing = _extract_numbers(r"(?:padding|margin|gap)\s*:\s*([0-9.]+)px", markup)
    shadows = _extract_shadows(markup)
    components = _detect_components(markup)
    background = next((c for c in palette if c.upper() in {"#FFFFFF", "#F9FAFB", "#F8FAFC", "#F5F5F5"}), "#FFFFFF")
    foreground = next((c for c in palette if c.upper() not in {background.upper()}), "#111827")

    tokens = {
        "slug": slug,
        "name": title,
        "source_url": url,
        "tags": tags or [],
        "extracted_at": datetime.now().isoformat(timespec="seconds"),
        "hash": hashlib.sha256(markup.encode("utf-8", errors="ignore")).hexdigest()[:16],
        "colors": {
            "primary": palette[0],
            "secondary": palette[1] if len(palette) > 1 else "#64748B",
            "accent": palette[2] if len(palette) > 2 else palette[0],
            "background": background,
            "foreground": foreground,
            "border": palette[3] if len(palette) > 3 else "#E5E7EB",
            "palette": palette,
        },
        "typography": fonts,
        "radii": radii or [4, 8, 12],
        "spacing": spacing or [8, 12, 16, 24, 32],
        "shadows": shadows,
        "components_detected": components,
        "raw_sample": markup[:12000],
    }
    return tokens


def _ensure_csv(path, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        with open(path, "w", encoding="utf-8", newline="") as f:
            csv.DictWriter(f, fieldnames=fields).writeheader()


def _upsert_csv(path, fields, key_field, row):
    _ensure_csv(path, fields)
    with open(path, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    rows = [r for r in rows if r.get(key_field) != row.get(key_field)]
    rows.append(row)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _tokens_to_rows(tokens):
    colors = tokens["colors"]
    tags = ",".join(tokens.get("tags") or [])
    keywords = ",".join(filter(None, [tokens["slug"], tags, "extracted", "网页提取", tokens["name"]]))
    style_name = f"{tokens['name']}（提取模板）"
    color_name = f"{tokens['name']} 配色"
    style_row = {
        "Style Name": style_name,
        "Category": "Extracted/Web",
        "Keywords": keywords,
        "Colors": " ".join(colors["palette"][:6]),
        "Effects": _infer_effects(tokens),
        "Best For": f"参考 {tokens['source_url']} 的视觉语言，可用于风格迁移、原型和界面改造",
        "Complexity": "中等",
        "Accessibility": "需人工复核",
    }
    color_row = {
        "Theme Name": color_name,
        "Primary": colors["primary"].lstrip("#"),
        "Secondary": colors["secondary"].lstrip("#"),
        "Accent": colors["accent"].lstrip("#"),
        "Background": colors["background"].lstrip("#"),
        "Foreground": colors["foreground"].lstrip("#"),
        "Border": colors["border"].lstrip("#"),
        "Notes": f"Extracted from {tokens['source_url']}；字体：{tokens['typography']['body']}；圆角：{tokens['radii']}",
    }
    return style_row, color_row


def _write_preview(tokens, target_dir):
    colors = tokens["colors"]
    swatch_cards = "".join(
        f'<div class="card"><div class="swatch" style="background:{color}"></div><p>{color}</p></div>'
        for color in colors["palette"][:8]
    )
    preview = f"""<!doctype html>
<html lang=\"zh-CN\">
<head>
<meta charset=\"utf-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<title>{html.escape(tokens['name'])} Design Tokens</title>
<style>
:root {{
  --primary: {colors['primary']};
  --secondary: {colors['secondary']};
  --accent: {colors['accent']};
  --background: {colors['background']};
  --foreground: {colors['foreground']};
  --border: {colors['border']};
  --radius: {tokens['radii'][min(1, len(tokens['radii']) - 1)]}px;
  --font-body: {tokens['typography']['body']};
}}
body {{ margin: 0; padding: 40px; background: var(--background); color: var(--foreground); font-family: var(--font-body); }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; max-width: 960px; }}
.card {{ border: 1px solid var(--border); border-radius: var(--radius); padding: 20px; box-shadow: {tokens['shadows'][0] if tokens['shadows'] else '0 8px 24px rgba(15,23,42,.08)'}; }}
.button {{ display:inline-flex; align-items:center; border:0; border-radius: var(--radius); padding: 10px 16px; background: var(--primary); color: #fff; font-weight: 600; }}
.swatch {{ height: 80px; border-radius: var(--radius); border: 1px solid var(--border); }}
</style>
</head>
<body>
<h1>{html.escape(tokens['name'])}</h1>
<p>Source: {html.escape(tokens['source_url'])}</p>
<div class=\"grid\">
{swatch_cards}
</div>
<p><button class=\"button\">Primary Button</button></p>
<div class=\"card\"><h2>Component Card</h2><p>Radius: {tokens['radii']} · Components: {', '.join(tokens['components_detected']) or 'unknown'}</p></div>
</body>
</html>
"""
    path = target_dir / "components.html"
    path.write_text(preview, encoding="utf-8")
    return path


def save_template(tokens):
    slug = tokens["slug"]
    target_dir = EXTRACTED_DIR / slug
    target_dir.mkdir(parents=True, exist_ok=True)
    tokens_path = target_dir / "tokens.json"
    tokens_to_save = {k: v for k, v in tokens.items() if k != "raw_sample"}
    tokens_path.write_text(json.dumps(tokens_to_save, indent=2, ensure_ascii=False), encoding="utf-8")
    preview_path = _write_preview(tokens, target_dir)

    style_row, color_row = _tokens_to_rows(tokens)
    _upsert_csv(EXTRACTED_DIR / "styles.csv", STYLE_FIELDS, "Style Name", style_row)
    _upsert_csv(EXTRACTED_DIR / "colors.csv", COLOR_FIELDS, "Theme Name", color_row)
    _upsert_csv(EXTRACTED_DIR / "_index.csv", INDEX_FIELDS, "Slug", {
        "Slug": slug,
        "Name": tokens["name"],
        "Source URL": tokens["source_url"],
        "Extracted At": tokens["extracted_at"],
        "Tags": ",".join(tokens.get("tags") or []),
        "Tokens Path": str(tokens_path),
        "Preview Path": str(preview_path),
    })
    return {
        "slug": slug,
        "tokens_path": str(tokens_path),
        "preview_path": str(preview_path),
        "style": style_row,
        "color": color_row,
    }


def list_templates():
    index = EXTRACTED_DIR / "_index.csv"
    if not index.exists():
        return []
    with open(index, "r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def remove_template(slug):
    removed = False
    slug = _slugify(slug)
    index_rows = list_templates()
    target_name_prefix = None
    for row in index_rows:
        if row.get("Slug") == slug:
            target_name_prefix = row.get("Name")
            removed = True
            break
    if not removed:
        return False

    for path, key in [(EXTRACTED_DIR / "_index.csv", "Slug")]:
        with open(path, "r", encoding="utf-8", newline="") as f:
            rows = [r for r in csv.DictReader(f) if r.get(key) != slug]
        with open(path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=INDEX_FIELDS)
            writer.writeheader()
            writer.writerows(rows)

    for path, fields, key, value in [
        (EXTRACTED_DIR / "styles.csv", STYLE_FIELDS, "Style Name", f"{target_name_prefix}（提取模板）"),
        (EXTRACTED_DIR / "colors.csv", COLOR_FIELDS, "Theme Name", f"{target_name_prefix} 配色"),
    ]:
        if path.exists():
            with open(path, "r", encoding="utf-8", newline="") as f:
                rows = [r for r in csv.DictReader(f) if r.get(key) != value]
            with open(path, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(rows)

    target_dir = EXTRACTED_DIR / slug
    if target_dir.exists():
        for child in target_dir.iterdir():
            if child.is_file():
                child.unlink()
        target_dir.rmdir()
    return True


def main(argv=None):
    parser = argparse.ArgumentParser(description="Extract web design language into local Smart UI Designer templates")
    parser.add_argument("--url", help="Reference website URL")
    parser.add_argument("--name", help="Template display name")
    parser.add_argument("--slug", help="Stable template slug")
    parser.add_argument("--tags", help="Comma-separated keywords")
    parser.add_argument("--dry-run", action="store_true", help="Print tokens without saving")
    parser.add_argument("--list", action="store_true", help="List extracted templates")
    parser.add_argument("--remove", help="Remove extracted template by slug")
    args = parser.parse_args(argv)

    if args.list:
        print(json.dumps({"templates": list_templates()}, indent=2, ensure_ascii=False))
        return 0
    if args.remove:
        print(json.dumps({"removed": remove_template(args.remove), "slug": _slugify(args.remove)}, ensure_ascii=False))
        return 0
    if not args.url:
        parser.error("--url is required unless --list or --remove is used")

    tags = [tag.strip() for tag in (args.tags or "").split(",") if tag.strip()]
    tokens = extract_tokens(args.url, name=args.name, slug=args.slug, tags=tags)
    if args.dry_run:
        print(json.dumps({k: v for k, v in tokens.items() if k != "raw_sample"}, indent=2, ensure_ascii=False))
        return 0
    result = save_template(tokens)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
