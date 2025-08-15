#!/usr/bin/env python3
"""
Script to replace image references with width attributes from markdown format to HTML img tag format.
Converts: ![alt](path.png){width=700} to <img src="path.png" alt="alt" width="700" />
"""

import os
import re
import glob
from pathlib import Path
from typing import List, Tuple

class ImageWidthFixer:
    def __init__(self, docs_root: str = "docs"):
        self.docs_root = Path(docs_root)
        self.md_files = []
        self.fixed_files = []
        
    def scan_files(self):
        """Scan for markdown files"""
        print("Scanning for markdown files...")
        self.md_files = list(self.docs_root.rglob("*.md"))
        print(f"Found {len(self.md_files)} markdown files")
        
    def fix_image_widths(self, content: str) -> Tuple[str, bool]:
        """Fix image references with width attributes"""
        original_content = content
        fixed = False
        
        # Pattern to match: ![alt](path.png){width=700} or ![alt](path.png){ width=700}
        # This handles both {width=700} and { width=700} formats
        img_pattern = r'!\[([^\]]*)\]\(([^)]+)\)\s*\{\s*width\s*=\s*(\d+)\s*\}'
        
        def replace_image(match):
            nonlocal fixed
            alt_text = match.group(1)
            image_path = match.group(2)
            width_value = match.group(3)
            
            fixed = True
            print(f"  Fixed image: ![alt](path){{width=width}} -> <img src=\"path\" alt=\"alt\" width=\"width\" />")
            return f'<img src="{image_path}" alt="{alt_text}" width="{width_value}" />'
        
        content = re.sub(img_pattern, replace_image, content)
        
        # Pattern to match: ![alt](path.png){style="inline"}{width="550"} or similar multi-attribute patterns
        multi_attr_pattern = r'!\[([^\]]*)\]\(([^)]+)\)(\s*\{[^}]+\})+\s*\{\s*width\s*=\s*["\']?(\d+)["\']?\s*\}'
        
        def replace_multi_attr_image(match):
            nonlocal fixed
            alt_text = match.group(1)
            image_path = match.group(2)
            width_value = match.group(4)
            
            fixed = True
            print(f"  Fixed multi-attribute image: ![alt](path){{...}}{{width=width}} -> <img src=\"path\" alt=\"alt\" width=\"width\" />")
            return f'<img src="{image_path}" alt="{alt_text}" width="{width_value}" />'
        
        content = re.sub(multi_attr_pattern, replace_multi_attr_image, content)
        
        return content, fixed
    
    def process_file(self, file_path: Path) -> bool:
        """Process a single markdown file"""
        print(f"Processing: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Fix image width references
            content, images_fixed = self.fix_image_widths(content)
            
            # Write back if changes were made
            if images_fixed:
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
        print("🚀 Starting image width attribute fixer...")
        print("=" * 50)
        print("📋 Converting:")
        print("   ![alt](path.png){width=700} -> <img src=\"path.png\" alt=\"alt\" width=\"700\" />")
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
    fixer = ImageWidthFixer()
    fixer.run()

if __name__ == "__main__":
    main()
