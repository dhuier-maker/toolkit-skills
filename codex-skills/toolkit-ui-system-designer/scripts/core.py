#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Smart UI Designer - Core search engine
BM25 + Regex hybrid search for UI design intelligence
"""

import csv
import re
from pathlib import Path
from math import log
from collections import defaultdict

# ============ CONFIGURATION ============
DATA_DIR = Path(__file__).parent.parent / "data"
MAX_RESULTS = 3

# Domain configuration with search/output columns
CSV_CONFIG = {
    "style": {
        "file": "styles.csv",
        "search_cols": ["Style Name", "Keywords", "Best For", "Category"],
        "output_cols": ["Style Name", "Category", "Keywords", "Colors", "Effects", "Best For", "Complexity", "Accessibility"]
    },
    "color": {
        "file": "colors.csv",
        "search_cols": ["Theme Name", "Keywords", "Notes"],
        "output_cols": ["Theme Name", "Primary", "Secondary", "Accent", "Background", "Foreground", "Border", "Notes"]
    },
    "admin": {
        "file": "admin-templates.csv",
        "search_cols": ["Template Name", "Keywords", "Features", "Stack"],
        "output_cols": ["Template Name", "Stack", "Features", "Layout", "Components", "Demo URL", "Notes"]
    },
    "bi": {
        "file": "bi-templates.csv",
        "search_cols": ["Template Name", "Keywords", "Chart Types", "Layout"],
        "output_cols": ["Template Name", "Layout", "Chart Types", "Features", "Tech Stack", "Demo URL", "Notes"]
    },
    "mobile": {
        "file": "mobile-specs.csv",
        "search_cols": ["Spec Name", "Keywords", "Platform", "Category"],
        "output_cols": ["Spec Name", "Platform", "Category", "Guidelines", "Do", "Don't", "Code Example"]
    },
    "component": {
        "file": "components.csv",
        "search_cols": ["Component Name", "Keywords", "Category", "Stack"],
        "output_cols": ["Component Name", "Category", "Stack", "Props", "Slots", "Events", "Usage Example", "Notes"]
    },
    "pattern": {
        "file": "patterns.csv",
        "search_cols": ["Pattern Name", "Keywords", "Category", "Use Case"],
        "output_cols": ["Pattern Name", "Category", "Use Case", "Structure", "Best Practices", "Anti Patterns"]
    },
    "ux": {
        "file": "ux-guidelines.csv",
        "search_cols": ["Category", "Issue", "Keywords", "Description"],
        "output_cols": ["Category", "Issue", "Description", "Do", "Don't", "Severity"]
    }
}

# Stack-specific configuration
STACK_CONFIG = {
    "vue3":           {"file": "stacks/vue3.csv"},
    "uniapp":         {"file": "stacks/uniapp.csv"},
    "react":          {"file": "stacks/react.csv"},
    "html-tailwind":  {"file": "stacks/html-tailwind.csv"}
}

_STACK_COLS = {
    "search_cols": ["Category", "Guideline", "Keywords", "Description"],
    "output_cols": ["Category", "Guideline", "Description", "Do", "Don't", "Code Good", "Code Bad", "Severity"]
}

AVAILABLE_STACKS = list(STACK_CONFIG.keys())


# ============ BM25 IMPLEMENTATION ============
class BM25:
    """BM25 ranking algorithm for text search"""

    def __init__(self, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.corpus = []
        self.doc_lengths = []
        self.avgdl = 0
        self.idf = {}
        self.doc_freqs = defaultdict(int)
        self.N = 0

    def tokenize(self, text):
        """Lowercase, split, remove punctuation, filter short words"""
        text = re.sub(r'[^\w\s]', ' ', str(text).lower())
        return [w for w in text.split() if len(w) > 1]

    def fit(self, documents):
        """Build BM25 index from documents"""
        self.corpus = [self.tokenize(doc) for doc in documents]
        self.N = len(self.corpus)
        if self.N == 0:
            return
        self.doc_lengths = [len(doc) for doc in self.corpus]
        self.avgdl = sum(self.doc_lengths) / self.N

        for doc in self.corpus:
            seen = set()
            for word in doc:
                if word not in seen:
                    self.doc_freqs[word] += 1
                    seen.add(word)

        for word, freq in self.doc_freqs.items():
            self.idf[word] = log((self.N - freq + 0.5) / (freq + 0.5) + 1)

    def score(self, query):
        """Score all documents against query"""
        query_tokens = self.tokenize(query)
        scores = []

        for idx, doc in enumerate(self.corpus):
            score = 0
            doc_len = self.doc_lengths[idx]
            term_freqs = defaultdict(int)
            for word in doc:
                term_freqs[word] += 1

            for token in query_tokens:
                if token in self.idf:
                    tf = term_freqs[token]
                    idf = self.idf[token]
                    numerator = tf * (self.k1 + 1)
                    denominator = tf + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)
                    score += idf * numerator / denominator

            scores.append((idx, score))

        return sorted(scores, key=lambda x: x[1], reverse=True)


# ============ SEARCH FUNCTIONS ============
def _load_csv(filepath):
    """Load CSV and return list of dicts"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def _load_domain_csv(filepath):
    """Load base CSV and merge user-extracted templates with the same schema."""
    data = _load_csv(filepath) if filepath.exists() else []
    extracted_path = DATA_DIR / "extracted" / filepath.name
    if extracted_path.exists():
        data.extend(_load_csv(extracted_path))
    return data


def _search_csv(filepath, search_cols, output_cols, query, max_results):
    """Core search function using BM25"""
    data = _load_domain_csv(filepath)
    if not data:
        return []

    documents = [" ".join(str(row.get(col, "")) for col in search_cols) for row in data]

    bm25 = BM25()
    bm25.fit(documents)
    ranked = bm25.score(query)

    results = []
    for idx, score in ranked[:max_results]:
        if score > 0:
            row = data[idx]
            results.append({col: row.get(col, "") for col in output_cols if col in row})

    return results


def detect_domain(query):
    """Auto-detect the most relevant domain from query"""
    query_lower = query.lower()

    domain_keywords = {
        "style": ["风格", "样式", "style", "设计风格", "ui风格", "视觉效果"],
        "color": ["颜色", "配色", "色彩", "color", "palette", "主题色"],
        "admin": ["后台", "管理", "admin", "管理系统", "后台管理", "cms", "erp", "crm"],
        "bi": ["大屏", "bi", "dashboard", "数据可视化", "图表", "驾驶舱", "监控大屏"],
        "mobile": ["移动端", "手机", "mobile", "app", "小程序", "h5", "uniapp", "响应式"],
        "component": ["组件", "component", "控件", "元素", "按钮", "表单", "表格", "弹窗"],
        "pattern": ["模式", "pattern", "布局", "结构", "模板", "架构"],
        "ux": ["体验", "ux", "交互", "可用性", "无障碍", "accessibility", "动画"]
    }

    scores = {}
    for domain, keywords in domain_keywords.items():
        score = sum(1 for kw in keywords if kw in query_lower)
        scores[domain] = score

    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "style"


def search(query, domain=None, max_results=MAX_RESULTS):
    """Main search function with auto-domain detection"""
    if domain is None:
        domain = detect_domain(query)

    config = CSV_CONFIG.get(domain, CSV_CONFIG["style"])
    filepath = DATA_DIR / config["file"]

    if not filepath.exists() and not (DATA_DIR / "extracted" / config["file"]).exists():
        return {"error": f"数据文件不存在: {filepath}", "domain": domain, "available_domains": list(CSV_CONFIG.keys())}

    results = _search_csv(filepath, config["search_cols"], config["output_cols"], query, max_results)

    return {
        "domain": domain,
        "query": query,
        "file": config["file"],
        "count": len(results),
        "results": results
    }


def search_stack(query, stack, max_results=MAX_RESULTS):
    """Search stack-specific guidelines"""
    if stack not in STACK_CONFIG:
        return {"error": f"未知技术栈: {stack}。可用: {', '.join(AVAILABLE_STACKS)}"}

    filepath = DATA_DIR / STACK_CONFIG[stack]["file"]

    if not filepath.exists():
        return {"error": f"技术栈文件不存在: {filepath}", "stack": stack}

    results = _search_csv(filepath, _STACK_COLS["search_cols"], _STACK_COLS["output_cols"], query, max_results)

    return {
        "domain": "stack",
        "stack": stack,
        "query": query,
        "file": STACK_CONFIG[stack]["file"],
        "count": len(results),
        "results": results
    }


def list_available_data():
    """List all available data files and their record counts"""
    available = {}
    for domain, config in CSV_CONFIG.items():
        filepath = DATA_DIR / config["file"]
        base_count = len(_load_csv(filepath)) if filepath.exists() else 0
        extracted_path = DATA_DIR / "extracted" / config["file"]
        extracted_count = len(_load_csv(extracted_path)) if extracted_path.exists() else 0
        if base_count or extracted_count:
            available[domain] = {
                "file": config["file"],
                "count": base_count + extracted_count,
                "base_count": base_count,
                "extracted_count": extracted_count
            }
        else:
            available[domain] = {
                "file": config["file"],
                "count": 0,
                "status": "not_found"
            }
    return available
