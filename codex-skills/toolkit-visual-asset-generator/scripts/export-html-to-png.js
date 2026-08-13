/**
 * HTML to PNG Export Script
 *
 * Uses Puppeteer to convert HTML files (including ECharts) to PNG images.
 * Supports batch export and custom resolution settings.
 *
 * Usage:
 *   node export-html-to-png.js <input.html> <output.png> [options]
 *   node export-html-to-png.js --batch <inputDir> <outputDir> [options]
 *
 * Options:
 *   --width <number>    Output width (default: 1920)
 *   --height <number>   Output height (default: 1080)
 *   --scale <number>    Scale factor for higher resolution (default: 2)
 *   --wait <number>     Wait time for rendering in ms (default: 1000)
 */

const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

/**
 * Export a single HTML file to PNG
 * @param {string} htmlPath - Path to the HTML file
 * @param {string} outputPath - Path for the output PNG file
 * @param {object} options - Export options
 * @param {number} options.width - Output width (default: 1920)
 * @param {number} options.height - Output height (default: 1080)
 * @param {number} options.scale - Scale factor (default: 2)
 * @param {number} options.waitTime - Wait time for rendering in ms (default: 1000)
 */
async function exportHtmlToPng(htmlPath, outputPath, options = {}) {
  const {
    width = 1920,
    height = 1080,
    scale = 2,
    waitTime = 1000
  } = options;

  console.log(`Converting: ${htmlPath}`);
  console.log(`Output: ${outputPath}`);
  console.log(`Resolution: ${width}x${height} @ ${scale}x scale`);

  const browser = await puppeteer.launch({
    headless: 'new',
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-web-security',
      '--disable-features=IsolateOrigins,site-per-process'
    ]
  });

  try {
    const page = await browser.newPage();
    await page.setViewport({
      width,
      height,
      deviceScaleFactor: scale
    });

    // Navigate to the HTML file
    const absolutePath = path.resolve(htmlPath);
    await page.goto(`file://${absolutePath}`, {
      waitUntil: 'networkidle0',
      timeout: 30000
    });

    // Wait for any async rendering (ECharts, animations, etc.)
    await page.waitForTimeout(waitTime);

    // Take screenshot
    await page.screenshot({
      path: outputPath,
      type: 'png',
      fullPage: false
    });

    console.log(`✅ Export successful: ${outputPath}`);
  } catch (error) {
    console.error(`❌ Export failed: ${error.message}`);
    throw error;
  } finally {
    await browser.close();
  }
}

/**
 * Batch export all HTML files in a directory
 * @param {string} inputDir - Directory containing HTML files
 * @param {string} outputDir - Directory for output PNG files
 * @param {object} options - Export options
 */
async function batchExport(inputDir, outputDir, options = {}) {
  // Ensure output directory exists
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  // Find all HTML files
  const files = fs.readdirSync(inputDir).filter(f => f.endsWith('.html'));

  if (files.length === 0) {
    console.log('No HTML files found in the input directory.');
    return;
  }

  console.log(`Found ${files.length} HTML file(s) to convert.\n`);

  const results = {
    success: [],
    failed: []
  };

  for (const file of files) {
    const htmlPath = path.join(inputDir, file);
    const pngPath = path.join(outputDir, file.replace('.html', '.png'));

    try {
      await exportHtmlToPng(htmlPath, pngPath, options);
      results.success.push(file);
    } catch (error) {
      results.failed.push({ file, error: error.message });
    }
  }

  // Summary
  console.log('\n========== Export Summary ==========');
  console.log(`✅ Successful: ${results.success.length}`);
  console.log(`❌ Failed: ${results.failed.length}`);

  if (results.failed.length > 0) {
    console.log('\nFailed files:');
    results.failed.forEach(({ file, error }) => {
      console.log(`  - ${file}: ${error}`);
    });
  }

  return results;
}

/**
 * Parse command line arguments
 */
function parseArgs() {
  const args = process.argv.slice(2);
  const options = {
    width: 1920,
    height: 1080,
    scale: 2,
    waitTime: 1000,
    batch: false,
    input: null,
    output: null
  };

  for (let i = 0; i < args.length; i++) {
    const arg = args[i];

    if (arg === '--batch') {
      options.batch = true;
    } else if (arg === '--width' && args[i + 1]) {
      options.width = parseInt(args[++i], 10);
    } else if (arg === '--height' && args[i + 1]) {
      options.height = parseInt(args[++i], 10);
    } else if (arg === '--scale' && args[i + 1]) {
      options.scale = parseInt(args[++i], 10);
    } else if (arg === '--wait' && args[i + 1]) {
      options.waitTime = parseInt(args[++i], 10);
    } else if (!arg.startsWith('--')) {
      if (!options.input) {
        options.input = arg;
      } else if (!options.output) {
        options.output = arg;
      }
    }
  }

  return options;
}

/**
 * Main entry point
 */
async function main() {
  const options = parseArgs();

  // Show help if no input provided
  if (!options.input) {
    console.log(`
HTML to PNG Export Script

Usage:
  Single file:
    node export-html-to-png.js <input.html> <output.png> [options]

  Batch mode:
    node export-html-to-png.js --batch <inputDir> <outputDir> [options]

Options:
  --width <number>    Output width (default: 1920)
  --height <number>   Output height (default: 1080)
  --scale <number>    Scale factor for higher resolution (default: 2)
  --wait <number>     Wait time for rendering in ms (default: 1000)

Examples:
  # Single file export
  node export-html-to-png.js background.html background.png

  # Batch export
  node export-html-to-png.js --batch ./html/ ./images/

  # Custom resolution
  node export-html-to-png.js background.html background.png --width 2560 --height 1440

  # High DPI export
  node export-html-to-png.js background.html background.png --scale 3
`);
    process.exit(0);
  }

  try {
    if (options.batch) {
      if (!options.output) {
        console.error('Error: Output directory is required for batch mode.');
        process.exit(1);
      }
      await batchExport(options.input, options.output, options);
    } else {
      if (!options.output) {
        // Auto-generate output filename
        options.output = options.input.replace('.html', '.png');
      }
      await exportHtmlToPng(options.input, options.output, options);
    }
  } catch (error) {
    console.error(`Error: ${error.message}`);
    process.exit(1);
  }
}

// Export functions for programmatic use
module.exports = {
  exportHtmlToPng,
  batchExport
};

// Run CLI if executed directly
if (require.main === module) {
  main();
}
