#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const DOCS_DIR = path.join(__dirname, 'docs');
const SIDEBAR_FILE = path.join(__dirname, 'sidebars.js');

/**
 * Recursively find all markdown files in a directory
 */
function findMarkdownFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);

  files.forEach(file => {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      findMarkdownFiles(filePath, fileList);
    } else if (file.match(/\.(md|mdx)$/i)) {
      fileList.push(filePath);
    }
  });

  return fileList;
}

/**
 * Convert absolute file path to sidebar reference format
 */
function filePathToSidebarRef(filePath) {
  const relativePath = path.relative(DOCS_DIR, filePath);
  // Remove file extension and normalize slashes
  return relativePath.replace(/\.(md|mdx)$/i, '').replace(/\\/g, '/');
}

/**
 * Extract all file references from sidebar.js content
 */
function extractSidebarReferences(sidebarContent) {
  const references = new Set();

  // Match all string literals that look like file paths
  // This handles both single-quoted and template literal strings
  const stringMatches = sidebarContent.matchAll(/['"]([^'"]+)['"]/g);

  for (const match of stringMatches) {
    const ref = match[1];
    // Only include references that look like file paths (contain / or are simple names)
    // Exclude things like 'category', 'label', etc.
    if (ref.includes('/') || (!ref.includes(' ') && ref !== 'category' && ref !== 'label' && ref !== 'type')) {
      references.add(ref);
    }
  }

  return references;
}

// Main execution
console.log('🔍 Finding unreferenced documentation files...\n');

// Find all markdown files
const allMarkdownFiles = findMarkdownFiles(DOCS_DIR);
console.log(`Found ${allMarkdownFiles.length} markdown files in docs/\n`);

// Read sidebar.js
const sidebarContent = fs.readFileSync(SIDEBAR_FILE, 'utf-8');
const sidebarReferences = extractSidebarReferences(sidebarContent);
console.log(`Found ${sidebarReferences.size} references in sidebars.js\n`);

// Find unreferenced files
const unreferencedFiles = [];

allMarkdownFiles.forEach(filePath => {
  const sidebarRef = filePathToSidebarRef(filePath);

  if (!sidebarReferences.has(sidebarRef)) {
    unreferencedFiles.push({
      path: filePath,
      ref: sidebarRef
    });
  }
});

// Report results
if (unreferencedFiles.length === 0) {
  console.log('✅ All documentation files are referenced in sidebars.js!');
} else {
  console.log(`⚠️  Found ${unreferencedFiles.length} unreferenced files:\n`);

  unreferencedFiles.forEach(file => {
    console.log(`  • ${file.ref}`);
    console.log(`    ${file.path}`);
    console.log();
  });

  console.log('\nTo reference these files, add them to sidebars.js using the format:');
  console.log("  'path/to/file'  (without the .md extension)\n");
}

// Exit with error code if there are unreferenced files
process.exit(unreferencedFiles.length > 0 ? 1 : 0);
