#!/usr/bin/env python3
"""
Script to fix the very last remaining broken links and anchors.
"""

import re
from pathlib import Path

def fix_last_issues():
    """Fix the very last remaining broken links and anchors"""
    docs_root = Path("docs")
    
    # Find all markdown files
    md_files = list(docs_root.rglob("*.md"))
    
    fixed_count = 0
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix 1: /case-studies/hubspot -> /case-studies/hubspot/ (add trailing slash)
            content = re.sub(
                r'\]\(/case-studies/hubspot\)',
                r'](/case-studies/hubspot/)',
                content
            )
            
            # Fix 2: /user-guide/editor/Editor -> /user-guide/editor/Editor (this is correct, just checking)
            
            # Fix 3: Remove the broken anchor link since #security doesn't exist in Javascript.md
            content = re.sub(
                r'\]\(/user-guide/block-types/core/Javascript#security\)',
                r'](/user-guide/block-types/core/Javascript)',
                content
            )
            
            if content != original_content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed last issues in: {md_file}")
                fixed_count += 1
        
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    print(f"\nFixed last issues in {fixed_count} files")

if __name__ == "__main__":
    fix_last_issues()
