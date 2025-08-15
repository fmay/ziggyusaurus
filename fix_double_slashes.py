#!/usr/bin/env python3
"""
Script to fix double slash issues in markdown files.
"""

import re
from pathlib import Path

def fix_double_slashes():
    """Fix all double slash issues in markdown files"""
    docs_root = Path("docs")
    
    # Find all markdown files
    md_files = list(docs_root.rglob("*.md"))
    
    fixed_count = 0
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix double slashes in links
            content = re.sub(r'\]\(//', '](/', content)
            
            if content != original_content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed double slashes in: {md_file}")
                fixed_count += 1
        
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    print(f"\nFixed double slashes in {fixed_count} files")

if __name__ == "__main__":
    fix_double_slashes()
