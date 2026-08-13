#!/usr/bin/env node
/**
 * build-pptx.mjs — 将整页幻灯片图片合成为 PPTX
 *
 * 用法：
 *   node build-pptx.mjs --slides <dir> --notes <file> --output <file.pptx>
 *   node build-pptx.mjs --slides <dir> --output <file.pptx>        # 无备注
 *
 * 行为：
 *   - 按文件名排序（slide-01.png → 02 → 03 ...）
 *   - 每张图片全幅铺满一页 PPT
 *   - 若指定 --notes 则读取 speaker-notes.md 并写入对应页备注
 *
 * 依赖：npm install pptxgenjs
 */

import pptxgen from 'pptxgenjs';
import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

function parseArgs() {
  const args = {};
  const argv = process.argv.slice(2);
  for (let i = 0; i < argv.length; i += 2) {
    const k = argv[i].replace(/^--/, '');
    args[k] = argv[i + 1];
  }
  if (!args.slides || !args.output) {
    console.error('用法: node build-pptx.mjs --slides <dir> --output <file.pptx> [--notes <speaker-notes.md>]');
    process.exit(1);
  }
  return args;
}

/**
 * 解析 speaker-notes.md，返回数组，第 N 项对应第 N 张 slide。
 * 格式：## Slide N - 标题\n\n内容...\n\n## Slide N+1 ...
 */
async function loadSpeakerNotes(notesPath) {
  if (!notesPath) return [];
  let raw;
  try {
    raw = await fs.readFile(notesPath, 'utf-8');
  } catch {
    return [];
  }
  const notes = [];
  const sections = raw.split(/(?=^## Slide \d)/m);
  for (const section of sections) {
    const trimmed = section.trim();
    if (!trimmed) continue;
    const lines = trimmed.split('\n');
    // 跳过 "## Slide N - 标题" 行和 [情绪标注] 行
    const bodyLines = lines.filter((l, i) =>
      i > 0 && !l.trim().startsWith('[') && !l.trim().startsWith('#')
    );
    notes.push(bodyLines.join('\n').trim());
  }
  return notes;
}

async function main() {
  const { slides: slidesDir, notes: notesPath, output: outFile } = parseArgs();
  const resolvedSlides = path.resolve(slidesDir);
  const resolvedOut = path.resolve(outFile);

  // 找到所有图片文件
  const files = (await fs.readdir(resolvedSlides))
    .filter(f => /\.(png|jpg|jpeg)$/i.test(f))
    .sort((a, b) => {
      // 按数字排序：slide-01.png → 02 → 03
      const na = parseInt(a.match(/\d+/)?.[0] ?? '0');
      const nb = parseInt(b.match(/\d+/)?.[0] ?? '0');
      return na - nb;
    });

  if (!files.length) {
    console.error(`No images found in ${resolvedSlides}`);
    process.exit(1);
  }

  console.log(`Found ${files.length} slide images`);

  // 加载备注
  const speakerNotes = notesPath ? await loadSpeakerNotes(path.resolve(notesPath)) : [];
  if (speakerNotes.length > 0) {
    console.log(`Loaded ${speakerNotes.length} speaker notes`);
  }

  const pres = new pptxgen();
  // 16:9 宽屏
  pres.layout = 'LAYOUT_WIDE'; // 13.333 × 7.5 inch

  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    const imgPath = path.join(resolvedSlides, file);
    const slide = pres.addSlide();

    // 全幅铺满图片作为背景
    slide.background = { color: 'FFFFFF' };
    slide.addImage(imgPath, {
      x: 0,
      y: 0,
      w: '100%',
      h: '100%',
      stretch: true,
    });

    // 写入备注（如果有对应条目）
    if (speakerNotes[i]) {
      slide.addNotes(speakerNotes[i]);
      console.log(`  [${i + 1}/${files.length}] ${file} ✓ +notes`);
    } else {
      console.log(`  [${i + 1}/${files.length}] ${file} ✓`);
    }
  }

  await pres.writeFile({ fileName: resolvedOut });
  console.log(`\n✓ Wrote ${resolvedOut} (${files.length} slides)${speakerNotes.length > 0 ? ' + 备注' : ''}`);
}

main().catch(e => { console.error(e); process.exit(1); });
