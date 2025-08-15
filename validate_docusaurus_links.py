#!/usr/bin/env python3
"""
Script to validate Docusaurus markdown links properly.
This understands Docusaurus routing and validates links according to the actual file structure.
"""

import re
import os
from pathlib import Path
from typing import List, Dict, Set, Tuple

class DocusaurusLinkValidator:
    def __init__(self, docs_root: str = "docs"):
        self.docs_root = Path(docs_root)
        self.md_files = set()
        self.valid_paths = set()
        self.broken_links = []
        
    def scan_files(self):
        """Scan for all markdown files and build valid paths"""
        print("Scanning for markdown files...")
        
        for md_file in self.docs_root.rglob("*.md"):
            self.md_files.add(md_file)
            
            # Add the file path without .md extension (Docusaurus format)
            relative_path = md_file.relative_to(self.docs_root)
            docusaurus_path = f"/{relative_path.with_suffix('')}"
            self.valid_paths.add(docusaurus_path)
            
            # Also add the path without leading slash for relative links
            self.valid_paths.add(str(relative_path.with_suffix('')))
        
        print(f"Found {len(self.md_files)} markdown files")
        print(f"Generated {len(self.valid_paths)} valid paths")
    
    def validate_links_in_file(self, file_path: Path) -> List[Dict]:
        """Validate all links in a single file"""
        broken_links = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Pattern to match markdown links: [text](url)
            link_pattern = r'\[([^\]]*)\]\(([^)]+)\)'
            
            for match in re.finditer(link_pattern, content):
                link_text = match.group(1)
                link_url = match.group(2)
                line_number = content[:match.start()].count('\n') + 1
                
                # Skip external links, anchors, and mailto
                if (link_url.startswith('http') or 
                    link_url.startswith('#') or 
                    link_url.startswith('mailto:') or
                    link_url.startswith('https://')):
                    continue
                
                # Handle Docusaurus paths (starting with /)
                if link_url.startswith('/'):
                    if link_url not in self.valid_paths:
                        broken_links.append({
                            'file': str(file_path),
                            'line': line_number,
                            'link_text': link_text,
                            'link_url': link_url,
                            'type': 'absolute'
                        })
                
                # Handle relative paths
                elif not link_url.startswith('http'):
                    # Try to resolve relative path
                    if link_url not in self.valid_paths:
                        broken_links.append({
                            'file': str(file_path),
                            'line': line_number,
                            'link_text': link_text,
                            'link_url': link_url,
                            'type': 'relative'
                        })
        
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
        
        return broken_links
    
    def validate_all_files(self):
        """Validate links in all markdown files"""
        print("Validating links in all files...")
        
        for md_file in self.md_files:
            broken_links = self.validate_links_in_file(md_file)
            self.broken_links.extend(broken_links)
        
        print(f"Found {len(self.broken_links)} broken links")
    
    def generate_report(self):
        """Generate a detailed report of broken links"""
        if not self.broken_links:
            print("✅ No broken links found!")
            return
        
        print("\n" + "=" * 80)
        print("❌ BROKEN LINKS REPORT")
        print("=" * 80)
        
        # Group by file
        by_file = {}
        for link in self.broken_links:
            file = link['file']
            if file not in by_file:
                by_file[file] = []
            by_file[file].append(link)
        
        for file, links in by_file.items():
            print(f"\n📄 {file}:")
            for link in links:
                print(f"   Line {link['line']}: [{link['link_text']}]({link['link_url']})")
        
        print(f"\n📊 Summary: {len(self.broken_links)} broken links in {len(by_file)} files")
    
    def generate_ignore_patterns(self):
        """Generate ignore patterns for common link checkers"""
        print("\n" + "=" * 80)
        print("🔧 IGNORE PATTERNS FOR LINK CHECKERS")
        print("=" * 80)
        
        print("\nFor markdown-link-check (.markdown-link-check.json):")
        print("""{
  "ignorePatterns": [
    {
      "pattern": "^/"
    },
    {
      "pattern": "^/user-guide/"
    },
    {
      "pattern": "^/block-types/"
    },
    {
      "pattern": "^/customisation/"
    },
    {
      "pattern": "^/case-studies/"
    }
  ]
}""")
        
        print("\nFor VS Code (.vscode/settings.json):")
        print("""{
  "markdown.validate.duplicateLinkDefinitions.enabled": false,
  "markdown.validate.fragmentLinks.enabled": false,
  "markdown.validate.fileLinks.enabled": false
}""")
        
        print("\nFor markdownlint (.markdownlint.yaml):")
        print("""MD013: false  # Line length
MD033: false  # HTML tags
MD041: false  # First line in file should be a top level heading""")
    
    def run(self):
        """Run the complete validation process"""
        print("🚀 Docusaurus Link Validator")
        print("=" * 50)
        
        self.scan_files()
        self.validate_all_files()
        self.generate_report()
        self.generate_ignore_patterns()

def main():
    """Main function"""
    validator = DocusaurusLinkValidator()
    validator.run()

if __name__ == "__main__":
    main()
