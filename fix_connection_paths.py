#!/usr/bin/env python3
"""
Script to fix all incorrect connection paths pointing to /user-guide/connections/Connections.
The correct path should be /user-guide/Connections.
"""

import re
from pathlib import Path

def fix_connection_paths():
    """Fix all incorrect connection paths"""
    docs_root = Path("docs")
    
    # Find all markdown files
    md_files = list(docs_root.rglob("*.md"))
    
    fixed_count = 0
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix incorrect connection paths
            # Pattern: [text](/user-guide/connections/Connections) -> [text](/user-guide/Connections)
            content = re.sub(
                r'\]\(/user-guide/connections/Connections\)',
                r'](/user-guide/Connections)',
                content
            )
            
            if content != original_content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed connection paths in: {md_file}")
                fixed_count += 1
        
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    print(f"\nFixed connection paths in {fixed_count} files")

if __name__ == "__main__":
    fix_connection_paths()
