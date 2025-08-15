#!/usr/bin/env python3
"""
Ultimate final script to fix all remaining broken links.
"""

import re
from pathlib import Path

def fix_ultimate_final():
    """Fix all remaining broken links once and for all"""
    docs_root = Path("docs")
    
    # Find all markdown files
    md_files = list(docs_root.rglob("*.md"))
    
    fixed_count = 0
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix 1: /case-studies/hubspot/ -> /case-studies/hubspot/Case-Study-Hubspot
            content = re.sub(
                r'\]\(/case-studies/hubspot/\)',
                r'](/case-studies/hubspot/Case-Study-Hubspot)',
                content
            )
            
            # Fix 2: /user-guide/block-types/store-helpers/store-helpers -> /user-guide/block-types/store-helpers/store-helpers
            # (This one is correct, just checking)
            
            # Fix 3: /user-guide/editor/Editor -> /user-guide/editor/Editor
            # (This one is correct, just checking)
            
            if content != original_content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed ultimate final issues in: {md_file}")
                fixed_count += 1
        
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    print(f"\nFixed ultimate final issues in {fixed_count} files")

if __name__ == "__main__":
    fix_ultimate_final()
