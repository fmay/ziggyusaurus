#!/usr/bin/env python3
"""
Script to fix documentation references in Docusaurus markdown files.
Fixes:
1. Image references to use proper Docusaurus paths
2. Markdown link references to use proper relative paths
"""

import os
import re
import glob
from pathlib import Path
from typing import List, Tuple, Dict

class DocsReferenceFixer:
    def __init__(self, docs_root: str = "docs", static_img_root: str = "static/img"):
        self.docs_root = Path(docs_root)
        self.static_img_root = Path(static_img_root)
        self.md_files = []
        self.image_files = set()
        self.fixed_files = []
        
    def scan_files(self):
        """Scan for markdown files and image files"""
        print("Scanning for markdown files...")
        self.md_files = list(self.docs_root.rglob("*.md"))
        print(f"Found {len(self.md_files)} markdown files")
        
        print("Scanning for image files...")
        for img_file in self.static_img_root.rglob("*.png"):
            self.image_files.add(img_file.name)
        print(f"Found {len(self.image_files)} PNG files")
        
    def fix_image_references(self, content: str, file_path: Path) -> Tuple[str, bool]:
        """Fix image references to use proper Docusaurus paths"""
        original_content = content
        fixed = False
        
        # Pattern to match image references: ![alt text](image.png)
        img_pattern = r'!\[([^\]]*)\]\(([^)]+\.png)\)'
        
        def replace_image(match):
            nonlocal fixed
            alt_text = match.group(1)
            image_name = match.group(2)
            
            # Check if image exists in static/img
            if image_name in self.image_files:
                # Convert to Docusaurus path format
                # Find the actual path of the image
                for img_path in self.static_img_root.rglob(image_name):
                    # Calculate relative path from docs root to static/img
                    relative_path = f"/img/{img_path.relative_to(self.static_img_root)}"
                    fixed = True
                    print(f"  Fixed image: {image_name} -> {relative_path}")
                    return f'![{alt_text}]({relative_path})'
            
            # If image not found, keep original but warn
            print(f"  Warning: Image not found: {image_name}")
            return match.group(0)
        
        content = re.sub(img_pattern, replace_image, content)
        return content, fixed
    
    def fix_markdown_links(self, content: str, file_path: Path) -> Tuple[str, bool]:
        """Fix markdown link references to use proper paths"""
        original_content = content
        fixed = False
        
        # Pattern to match markdown links: [text](filename.md)
        link_pattern = r'\[([^\]]*)\]\(([^)]+\.md)\)'
        
        def replace_link(match):
            nonlocal fixed
            link_text = match.group(1)
            link_file = match.group(2)
            
            # Skip if it's already an absolute path
            if link_file.startswith('/'):
                return match.group(0)
            
            # Find the referenced file
            target_file = None
            for md_file in self.md_files:
                if md_file.name == link_file:
                    target_file = md_file
                    break
            
            if target_file:
                # Calculate relative path from current file to target file
                try:
                    relative_path = os.path.relpath(target_file, file_path.parent)
                    # Convert to Docusaurus format (remove .md extension)
                    relative_path = relative_path.replace('.md', '')
                    
                    # If it's in the same directory, just use the filename without .md
                    if relative_path == link_file:
                        relative_path = link_file.replace('.md', '')
                    elif relative_path.startswith('..'):
                        # Going up directories, convert to absolute path
                        relative_path = f"/{target_file.relative_to(self.docs_root).with_suffix('')}"
                    
                    fixed = True
                    print(f"  Fixed link: {link_file} -> {relative_path}")
                    return f'[{link_text}]({relative_path})'
                except ValueError:
                    # If we can't calculate relative path, use absolute
                    relative_path = f"/{target_file.relative_to(self.docs_root).with_suffix('')}"
                    fixed = True
                    print(f"  Fixed link (absolute): {link_file} -> {relative_path}")
                    return f'[{link_text}]({relative_path})'
            else:
                print(f"  Warning: Referenced file not found: {link_file}")
                return match.group(0)
        
        content = re.sub(link_pattern, replace_link, content)
        return content, fixed
    
    def process_file(self, file_path: Path) -> bool:
        """Process a single markdown file"""
        print(f"Processing: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix image references
            content, images_fixed = self.fix_image_references(content, file_path)
            
            # Fix markdown links
            content, links_fixed = self.fix_markdown_links(content, file_path)
            
            # Write back if changes were made
            if images_fixed or links_fixed:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.fixed_files.append(str(file_path))
                print(f"  ✅ Updated file")
                return True
            else:
                print(f"  ⏭️  No changes needed")
                return False
                
        except Exception as e:
            print(f"  ❌ Error processing file: {e}")
            return False
    
    def run(self):
        """Run the fixer on all markdown files"""
        print("🚀 Starting documentation reference fixer...")
        print("=" * 50)
        
        self.scan_files()
        print()
        
        print("🔧 Processing files...")
        print("-" * 30)
        
        processed_count = 0
        fixed_count = 0
        
        for md_file in self.md_files:
            if self.process_file(md_file):
                fixed_count += 1
            processed_count += 1
            print()
        
        print("=" * 50)
        print(f"📊 Summary:")
        print(f"   Files processed: {processed_count}")
        print(f"   Files updated: {fixed_count}")
        print(f"   Files unchanged: {processed_count - fixed_count}")
        
        if self.fixed_files:
            print(f"\n📝 Updated files:")
            for file_path in self.fixed_files:
                print(f"   - {file_path}")
        
        print("\n✨ Done!")

def main():
    """Main function"""
    fixer = DocsReferenceFixer()
    fixer.run()

if __name__ == "__main__":
    main()
