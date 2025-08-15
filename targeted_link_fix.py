#!/usr/bin/env python3
"""
Targeted script to fix the specific broken links identified in the Docusaurus build output.
"""

import re
from pathlib import Path

def fix_targeted_links():
    """Fix the specific broken links identified in the build output"""
    docs_root = Path("docs")
    
    # Find all markdown files
    md_files = list(docs_root.rglob("*.md"))
    
    fixed_count = 0
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            file_fixed = False
            
            # Fix 1: Add /user-guide/ prefix to paths that need it
            # Pattern: [text](/connections) -> [text](/user-guide/connections)
            content = re.sub(
                r'\]\(/(connections|secrets|variables|structures|batching|error-handling|memory-store|data-store|monitoring|global-settings|tests|tags|deployment|security|troubleshooting|logging|alerts|launching|transferring-data|auditing|data-browser)\)',
                r'](/user-guide/\1)',
                content
            )
            
            # Fix 2: Fix specific block-type paths
            # Pattern: [text](block-types/utility/Data-Store) -> [text](/user-guide/block-types/utility/Data-Store)
            content = re.sub(
                r'\]\((block-types/[^)]+)\)',
                r'](/user-guide/\1)',
                content
            )
            
            # Fix 3: Fix specific relative paths that should be absolute
            # Pattern: [text](global-settings/Global-Settings) -> [text](/user-guide/global-settings/Global-Settings)
            content = re.sub(
                r'\]\((global-settings/[^)]+)\)',
                r'](/user-guide/\1)',
                content
            )
            
            # Fix 4: Fix specific relative paths that should be absolute
            # Pattern: [text](Memory-Store) -> [text](/user-guide/memory-store/Memory-Store)
            content = re.sub(
                r'\]\((Memory-Store)\)',
                r'](/user-guide/memory-store/\1)',
                content
            )
            
            # Fix 5: Fix specific relative paths that should be absolute
            # Pattern: [text](Connections) -> [text](/user-guide/connections/Connections)
            content = re.sub(
                r'\]\((Connections)\)',
                r'](/user-guide/connections/\1)',
                content
            )
            
            # Fix 6: Fix specific relative paths that should be absolute
            # Pattern: [text](Secrets) -> [text](/user-guide/secrets/Secrets)
            content = re.sub(
                r'\]\((Secrets)\)',
                r'](/user-guide/secrets/\1)',
                content
            )
            
            # Fix 7: Fix specific relative paths that should be absolute
            # Pattern: [text](Alerts) -> [text](/user-guide/alerts/Alerts)
            content = re.sub(
                r'\]\((Alerts)\)',
                r'](/user-guide/alerts/\1)',
                content
            )
            
            # Fix 8: Fix specific relative paths that should be absolute
            # Pattern: [text](Batching) -> [text](/user-guide/batching/Batching)
            content = re.sub(
                r'\]\((Batching)\)',
                r'](/user-guide/batching/\1)',
                content
            )
            
            # Fix 9: Fix specific relative paths that should be absolute
            # Pattern: [text](Structures-and-mapping) -> [text](/user-guide/structures/Structures-and-mapping)
            content = re.sub(
                r'\]\((Structures-and-mapping)\)',
                r'](/user-guide/structures/\1)',
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
            # Pattern: [text](Tests) -> [text](/user-guide/tests/Tests)
            content = re.sub(
                r'\]\((Tests)\)',
                r'](/user-guide/tests/\1)',
                content
            )
            
            # Fix 12: Fix specific relative paths that should be absolute
            # Pattern: [text](Editor) -> [text](/user-guide/editor/Editor)
            content = re.sub(
                r'\]\((Editor)\)',
                r'](/user-guide/editor/\1)',
                content
            )
            
            # Fix 13: Fix specific relative paths that should be absolute
            # Pattern: [text](Auditing) -> [text](/user-guide/auditing/Auditing)
            content = re.sub(
                r'\]\((Auditing)\)',
                r'](/user-guide/auditing/\1)',
                content
            )
            
            # Fix 14: Fix specific relative paths that should be absolute
            # Pattern: [text](Launching-flows) -> [text](/user-guide/launching/Launching-flows)
            content = re.sub(
                r'\]\((Launching-flows)\)',
                r'](/user-guide/launching/\1)',
                content
            )
            
            # Fix 15: Fix specific relative paths that should be absolute
            # Pattern: [text](Transferring-Data) -> [text](/user-guide/transferring-data/Transferring-Data)
            content = re.sub(
                r'\]\((Transferring-Data)\)',
                r'](/user-guide/transferring-data/\1)',
                content
            )
            
            # Fix 16: Fix specific relative paths that should be absolute
            # Pattern: [text](Data-and-Memory-Store-Browser) -> [text](/user-guide/data-browser/Data-and-Memory-Store-Browser)
            content = re.sub(
                r'\]\((Data-and-Memory-Store-Browser)\)',
                r'](/user-guide/data-browser/\1)',
                content
            )
            
            # Fix 17: Fix specific relative paths that should be absolute
            # Pattern: [text](store-helpers) -> [text](/user-guide/block-types/store-helpers/store-helpers)
            content = re.sub(
                r'\]\((store-helpers)\)',
                r'](/user-guide/block-types/store-helpers/store-helpers)',
                content
            )
            
            if content != original_content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed links in: {md_file}")
                fixed_count += 1
                file_fixed = True
        
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    print(f"\nFixed links in {fixed_count} files")

if __name__ == "__main__":
    fix_targeted_links()
