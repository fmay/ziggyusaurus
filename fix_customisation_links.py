#!/usr/bin/env python3
"""
Script to fix customisation section links that are using incorrect lowercase paths.
"""

import re
from pathlib import Path

def fix_customisation_links():
    """Fix customisation section links with incorrect paths"""
    docs_root = Path("docs")
    
    # Find all markdown files in customisation directory
    customisation_files = list(docs_root.rglob("customisation/**/*.md"))
    
    fixed_count = 0
    
    for md_file in customisation_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix 1: /user-guide/global-settings -> /user-guide/Global-Settings
            content = re.sub(
                r'\]\(/user-guide/global-settings\)',
                r'](/user-guide/Global-Settings)',
                content
            )
            
            # Fix 2: /user-guide/monitoring -> /user-guide/Monitoring
            content = re.sub(
                r'\]\(/user-guide/monitoring\)',
                r'](/user-guide/Monitoring)',
                content
            )
            
            # Fix 3: /user-guide/security -> /user-guide/Security
            content = re.sub(
                r'\]\(/user-guide/security\)',
                r'](/user-guide/Security)',
                content
            )
            
            # Fix 4: /user-guide/connections -> /user-guide/Connections
            content = re.sub(
                r'\]\(/user-guide/connections\)',
                r'](/user-guide/Connections)',
                content
            )
            
            # Fix 5: /user-guide/secrets -> /user-guide/Secrets
            content = re.sub(
                r'\]\(/user-guide/secrets\)',
                r'](/user-guide/Secrets)',
                content
            )
            
            # Fix 6: /user-guide/batching -> /user-guide/Batching
            content = re.sub(
                r'\]\(/user-guide/batching\)',
                r'](/user-guide/Batching)',
                content
            )
            
            # Fix 7: /user-guide/editor -> /user-guide/editor
            # (This one is correct, just checking)
            
            # Fix 8: /user-guide/block-types -> /user-guide/block-types
            # (This one is correct, just checking)
            
            if content != original_content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed customisation links in: {md_file}")
                fixed_count += 1
        
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    print(f"\nFixed customisation links in {fixed_count} files")

if __name__ == "__main__":
    fix_customisation_links()
