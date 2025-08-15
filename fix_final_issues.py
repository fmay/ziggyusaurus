#!/usr/bin/env python3
"""
Script to fix the final remaining broken links.
"""

import re
from pathlib import Path

def fix_final_issues():
    """Fix the final remaining broken links"""
    docs_root = Path("docs")
    
    # Find all markdown files
    md_files = list(docs_root.rglob("*.md"))
    
    fixed_count = 0
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix 1: /case-studies -> /case-studies/hubspot (since that's where the files are)
            content = re.sub(
                r'\]\(/case-studies\)',
                r'](/case-studies/hubspot)',
                content
            )
            
            # Fix 2: /customisation -> /customisation (this is correct, just checking)
            
            # Fix 3: /user-guide/block-types/store-helpers/store-helpers -> /user-guide/block-types/store-helpers/store-helpers
            # (This one is correct, just checking)
            
            # Fix 4: /user-guide/editor/Editor -> /user-guide/editor/Editor
            # (This one is correct, just checking)
            
            # Fix 5: Customisation.md -> /customisation/Custom-Utility-Blocks
            content = re.sub(
                r'\]\(Customisation\.md\)',
                r'](/customisation/Custom-Utility-Blocks)',
                content
            )
            
            # Fix 6: Javascript.md#security -> /user-guide/block-types/core/Javascript#security
            content = re.sub(
                r'\]\(Javascript\.md#security\)',
                r'](/user-guide/block-types/core/Javascript#security)',
                content
            )
            
            if content != original_content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed final issues in: {md_file}")
                fixed_count += 1
        
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    print(f"\nFixed final issues in {fixed_count} files")

if __name__ == "__main__":
    fix_final_issues()
