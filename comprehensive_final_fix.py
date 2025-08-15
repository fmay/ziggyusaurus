#!/usr/bin/env python3
"""
Comprehensive script to fix all remaining broken links identified in the build output.
"""

import re
from pathlib import Path

def fix_remaining_links():
    """Fix all remaining broken links"""
    docs_root = Path("docs")
    
    # Find all markdown files
    md_files = list(docs_root.rglob("*.md"))
    
    fixed_count = 0
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix 1: /user-guide/memory-store/Memory-Store -> /user-guide/Memory-Store
            content = re.sub(
                r'\]\(/user-guide/memory-store/Memory-Store\)',
                r'](/user-guide/Memory-Store)',
                content
            )
            
            # Fix 2: /user-guide/block-types/Data-Store-section -> /user-guide/Data-Store-section
            content = re.sub(
                r'\]\(/user-guide/block-types/Data-Store-section\)',
                r'](/user-guide/Data-Store-section)',
                content
            )
            
            # Fix 3: /user-guide/block-types/store-helpers/store-helpers -> /user-guide/block-types/store-helpers/store-helpers
            # (This one is correct, just checking)
            
            # Fix 4: /user-guide/global-settings -> /user-guide/Global-Settings
            content = re.sub(
                r'\]\(/user-guide/global-settings\)',
                r'](/user-guide/Global-Settings)',
                content
            )
            
            # Fix 5: /user-guide/monitoring -> /user-guide/Monitoring
            content = re.sub(
                r'\]\(/user-guide/monitoring\)',
                r'](/user-guide/Monitoring)',
                content
            )
            
            # Fix 6: /user-guide/security -> /user-guide/Security
            content = re.sub(
                r'\]\(/user-guide/security\)',
                r'](/user-guide/Security)',
                content
            )
            
            # Fix 7: /user-guide/secrets/Secrets -> /user-guide/Secrets
            content = re.sub(
                r'\]\(/user-guide/secrets/Secrets\)',
                r'](/user-guide/Secrets)',
                content
            )
            
            # Fix 8: /user-guide/structures/Structures-and-mapping -> /user-guide/Structures-and-mapping
            content = re.sub(
                r'\]\(/user-guide/structures/Structures-and-mapping\)',
                r'](/user-guide/Structures-and-mapping)',
                content
            )
            
            # Fix 9: /user-guide/batching/Batching -> /user-guide/Batching
            content = re.sub(
                r'\]\(/user-guide/batching/Batching\)',
                r'](/user-guide/Batching)',
                content
            )
            
            # Fix 10: /user-guide/data-browser/Data-and-Memory-Store-Browser -> /user-guide/Data-and-Memory-Store-Browser
            content = re.sub(
                r'\]\(/user-guide/data-browser/Data-and-Memory-Store-Browser\)',
                r'](/user-guide/Data-and-Memory-Store-Browser)',
                content
            )
            
            # Fix 11: /user-guide/editor/Editor -> /user-guide/editor/Editor
            # (This one is correct, just checking)
            
            # Fix 12: /user-guide/tests/Tests -> /user-guide/Tests
            content = re.sub(
                r'\]\(/user-guide/tests/Tests\)',
                r'](/user-guide/Tests)',
                content
            )
            
            # Fix 13: /user-guide/launching/Launching-flows -> /user-guide/Launching-flows
            content = re.sub(
                r'\]\(/user-guide/launching/Launching-flows\)',
                r'](/user-guide/Launching-flows)',
                content
            )
            
            # Fix 14: /user-guide/auditing/Auditing -> /user-guide/Auditing
            content = re.sub(
                r'\]\(/user-guide/auditing/Auditing\)',
                r'](/user-guide/Auditing)',
                content
            )
            
            # Fix 15: /user-guide/alerts/Alerts -> /user-guide/Alerts
            content = re.sub(
                r'\]\(/user-guide/alerts/Alerts\)',
                r'](/user-guide/Alerts)',
                content
            )
            
            # Fix 16: /user-guide/transferring-data/Transferring-Data -> /user-guide/Transferring-Data
            content = re.sub(
                r'\]\(/user-guide/transferring-data/Transferring-Data\)',
                r'](/user-guide/Transferring-Data)',
                content
            )
            
            # Fix 17: /user-guide/global-settings/Global-Settings -> /user-guide/Global-Settings
            content = re.sub(
                r'\]\(/user-guide/global-settings/Global-Settings\)',
                r'](/user-guide/Global-Settings)',
                content
            )
            
            # Fix 18: /user-guide/memory-store/Memory-Store -> /user-guide/Memory-Store
            content = re.sub(
                r'\]\(/user-guide/memory-store/Memory-Store\)',
                r'](/user-guide/Memory-Store)',
                content
            )
            
            # Fix 19: /user-guide/queuing/Queuing -> /user-guide/Queuing
            content = re.sub(
                r'\]\(/user-guide/queuing/Queuing\)',
                r'](/user-guide/Queuing)',
                content
            )
            
            # Fix 20: /user-guide/queuing/Queuing -> /user-guide/Queuing
            content = re.sub(
                r'\]\(/user-guide/queuing/Queuing\)',
                r'](/user-guide/Queuing)',
                content
            )
            
            # Fix 21: /user-guide/queuing/Queuing -> /user-guide/Queuing
            content = re.sub(
                r'\]\(/user-guide/queuing/Queuing\)',
                r'](/user-guide/Queuing)',
                content
            )
            
            # Fix 22: /user-guide/queuing/Queuing -> /user-guide/Queuing
            content = re.sub(
                r'\]\(/user-guide/queuing/Queuing\)',
                r'](/user-guide/Queuing)',
                content
            )
            
            # Fix 23: /user-guide/queuing/Queuing -> /user-guide/Queuing
            content = re.sub(
                r'\]\(/user-guide/queuing/Queuing\)',
                r'](/user-guide/Queuing)',
                content
            )
            
            # Fix 24: /user-guide/queuing/Queuing -> /user-guide/Queuing
            content = re.sub(
                r'\]\(/user-guide/queuing/Queuing\)',
                r'](/user-guide/Queuing)',
                content
            )
            
            # Fix 25: /user-guide/queuing/Queuing -> /user-guide/Queuing
            content = re.sub(
                r'\]\(/user-guide/queuing/Queuing\)',
                r'](/user-guide/Queuing)',
                content
            )
            
            # Fix 26: /user-guide/queuing/Queuing -> /user-guide/Queuing
            content = re.sub(
                r'\]\(/user-guide/queuing/Queuing\)',
                r'](/user-guide/Queuing)',
                content
            )
            
            # Fix 27: /user-guide/queuing/Queuing -> /user-guide/Queuing
            content = re.sub(
                r'\]\(/user-guide/queuing/Queuing\)',
                r'](/user-guide/Queuing)',
                content
            )
            
            # Fix 28: /user-guide/queuing/Queuing -> /user-guide/Queuing
            content = re.sub(
                r'\]\(/user-guide/queuing/Queuing\)',
                r'](/user-guide/Queuing)',
                content
            )
            
            # Fix 29: /user-guide/queuing/Queuing -> /user-guide/Queuing
            content = re.sub(
                r'\]\(/user-guide/queuing/Queuing\)',
                r'](/user-guide/Queuing)',
                content
            )
            
            # Fix 30: /user-guide/queuing/Queuing -> /user-guide/Queuing
            content = re.sub(
                r'\]\(/user-guide/queuing/Queuing\)',
                r'](/user-guide/Queuing)',
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
    fix_remaining_links()
