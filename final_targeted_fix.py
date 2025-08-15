#!/usr/bin/env python3
"""
Final targeted script to fix the remaining broken links.
"""

import re
from pathlib import Path

def fix_final_links():
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
            
            # Fix 1: Add /user-guide/ prefix to paths that need it
            # Pattern: [text](/connections) -> [text](/user-guide/connections)
            content = re.sub(
                r'\]\(/(connections|secrets|variables|structures|batching|error-handling|memory-store|data-store|monitoring|global-settings|tests|tags|deployment|security|troubleshooting|logging|alerts|launching|transferring-data|auditing|data-browser)\)',
                r'](/user-guide/\1)',
                content
            )
            
            # Fix 2: Fix specific relative paths that should be absolute
            # Pattern: [text](Connections) -> [text](/user-guide/connections/Connections)
            content = re.sub(
                r'\]\((Connections)\)',
                r'](/user-guide/connections/\1)',
                content
            )
            
            # Fix 3: Fix specific relative paths that should be absolute
            # Pattern: [text](Secrets) -> [text](/user-guide/secrets/Secrets)
            content = re.sub(
                r'\]\((Secrets)\)',
                r'](/user-guide/secrets/\1)',
                content
            )
            
            # Fix 4: Fix specific relative paths that should be absolute
            # Pattern: [text](Alerts) -> [text](/user-guide/alerts/Alerts)
            content = re.sub(
                r'\]\((Alerts)\)',
                r'](/user-guide/alerts/\1)',
                content
            )
            
            # Fix 5: Fix specific relative paths that should be absolute
            # Pattern: [text](Launching-flows) -> [text](/user-guide/launching/Launching-flows)
            content = re.sub(
                r'\]\((Launching-flows)\)',
                r'](/user-guide/launching/\1)',
                content
            )
            
            # Fix 6: Fix specific relative paths that should be absolute
            # Pattern: [text](Transferring-Data) -> [text](/user-guide/transferring-data/Transferring-Data)
            content = re.sub(
                r'\]\((Transferring-Data)\)',
                r'](/user-guide/transferring-data/\1)',
                content
            )
            
            # Fix 7: Fix specific relative paths that should be absolute
            # Pattern: [text](Auditing) -> [text](/user-guide/auditing/Auditing)
            content = re.sub(
                r'\]\((Auditing)\)',
                r'](/user-guide/auditing/\1)',
                content
            )
            
            # Fix 8: Fix specific relative paths that should be absolute
            # Pattern: [text](Tests) -> [text](/user-guide/tests/Tests)
            content = re.sub(
                r'\]\((Tests)\)',
                r'](/user-guide/tests/\1)',
                content
            )
            
            # Fix 9: Fix specific relative paths that should be absolute
            # Pattern: [text](Editor) -> [text](/user-guide/editor/Editor)
            content = re.sub(
                r'\]\((Editor)\)',
                r'](/user-guide/editor/\1)',
                content
            )
            
            # Fix 10: Fix specific relative paths that should be absolute
            # Pattern: [text](Data-Store-section) -> [text](/user-guide/block-types/Data-Store-section)
            content = re.sub(
                r'\]\((Data-Store-section)\)',
                r'](/user-guide/block-types/\1)',
                content
            )
            
            # Fix 11: Fix specific relative paths that should be absolute
            # Pattern: [text](store-helpers) -> [text](/user-guide/block-types/store-helpers/store-helpers)
            content = re.sub(
                r'\]\((store-helpers)\)',
                r'](/user-guide/block-types/store-helpers/store-helpers)',
                content
            )
            
            # Fix 12: Fix specific relative paths that should be absolute
            # Pattern: [text](Memory-Store) -> [text](/user-guide/memory-store/Memory-Store)
            content = re.sub(
                r'\]\((Memory-Store)\)',
                r'](/user-guide/memory-store/\1)',
                content
            )
            
            # Fix 13: Fix specific relative paths that should be absolute
            # Pattern: [text](Data-and-Memory-Store-Browser) -> [text](/user-guide/data-browser/Data-and-Memory-Store-Browser)
            content = re.sub(
                r'\]\((Data-and-Memory-Store-Browser)\)',
                r'](/user-guide/data-browser/\1)',
                content
            )
            
            # Fix 14: Fix specific relative paths that should be absolute
            # Pattern: [text](Structures-and-mapping) -> [text](/user-guide/structures/Structures-and-mapping)
            content = re.sub(
                r'\]\((Structures-and-mapping)\)',
                r'](/user-guide/structures/\1)',
                content
            )
            
            # Fix 15: Fix specific relative paths that should be absolute
            # Pattern: [text](Batching) -> [text](/user-guide/batching/Batching)
            content = re.sub(
                r'\]\((Batching)\)',
                r'](/user-guide/batching/\1)',
                content
            )
            
            # Fix 16: Fix specific relative paths that should be absolute
            # Pattern: [text](sql-mapping) -> [text](/user-guide/block-types/utility/sql/sql-mapping)
            content = re.sub(
                r'\]\((sql-mapping)\)',
                r'](/user-guide/block-types/utility/sql/\1)',
                content
            )
            
            # Fix 17: Fix specific relative paths that should be absolute
            # Pattern: [text](sql-editing) -> [text](/user-guide/block-types/utility/sql/sql-editing)
            content = re.sub(
                r'\]\((sql-editing)\)',
                r'](/user-guide/block-types/utility/sql/\1)',
                content
            )
            
            # Fix 18: Fix specific relative paths that should be absolute
            # Pattern: [text](sql-configuration) -> [text](/user-guide/block-types/utility/sql/sql-configuration)
            content = re.sub(
                r'\]\((sql-configuration)\)',
                r'](/user-guide/block-types/utility/sql/\1)',
                content
            )
            
            # Fix 19: Fix specific relative paths that should be absolute
            # Pattern: [text](sql-select) -> [text](/user-guide/block-types/utility/sql/sql-select)
            content = re.sub(
                r'\]\((sql-select)\)',
                r'](/user-guide/block-types/utility/sql/\1)',
                content
            )
            
            # Fix 20: Fix specific relative paths that should be absolute
            # Pattern: [text](sql-insert) -> [text](/user-guide/block-types/utility/sql/sql-insert)
            content = re.sub(
                r'\]\((sql-insert)\)',
                r'](/user-guide/block-types/utility/sql/\1)',
                content
            )
            
            # Fix 21: Fix specific relative paths that should be absolute
            # Pattern: [text](sql-update) -> [text](/user-guide/block-types/utility/sql/sql-update)
            content = re.sub(
                r'\]\((sql-update)\)',
                r'](/user-guide/block-types/utility/sql/\1)',
                content
            )
            
            # Fix 22: Fix specific relative paths that should be absolute
            # Pattern: [text](sql-upsert) -> [text](/user-guide/block-types/utility/sql/sql-upsert)
            content = re.sub(
                r'\]\((sql-upsert)\)',
                r'](/user-guide/block-types/utility/sql/\1)',
                content
            )
            
            # Fix 23: Fix specific relative paths that should be absolute
            # Pattern: [text](sql-delete) -> [text](/user-guide/block-types/utility/sql/sql-delete)
            content = re.sub(
                r'\]\((sql-delete)\)',
                r'](/user-guide/block-types/utility/sql/\1)',
                content
            )
            
            # Fix 24: Fix specific relative paths that should be absolute
            # Pattern: [text](sql-raw) -> [text](/user-guide/block-types/utility/sql/sql-raw)
            content = re.sub(
                r'\]\((sql-raw)\)',
                r'](/user-guide/block-types/utility/sql/\1)',
                content
            )
            
            if content != original_content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed links in: {md_file}")
                fixed_count += 1
        
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    print(f"\nFixed links in {fixed_count} files")

if __name__ == "__main__":
    fix_final_links()
