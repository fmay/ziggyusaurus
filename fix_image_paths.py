#!/usr/bin/env python3
"""
Script to fix incorrectly modified image paths.
The previous script incorrectly added /user-guide/ to image paths.
"""

import re
from pathlib import Path

def fix_image_paths():
    """Fix incorrectly modified image paths"""
    docs_root = Path("docs")
    
    # Find all markdown files
    md_files = list(docs_root.rglob("*.md"))
    
    fixed_count = 0
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix incorrectly modified image paths: /user-guide/img/ -> /img/
            content = re.sub(r'\]\(/user-guide(/img/[^)]+)\)', r'](\1', content)
            
            if content != original_content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed image paths in: {md_file}")
                fixed_count += 1
        
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    print(f"\nFixed image paths in {fixed_count} files")

if __name__ == "__main__":
    fix_image_paths()
