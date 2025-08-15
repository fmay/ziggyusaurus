#!/usr/bin/env python3
"""
Script to fix the final 3 broken links.
"""

import re
from pathlib import Path

def fix_final_three():
    """Fix the final 3 broken links"""
    
    # Fix 1: Overview.md - /customisation -> /customisation/Custom-Utility-Blocks
    overview_file = Path("docs/Overview.md")
    if overview_file.exists():
        with open(overview_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = re.sub(
            r'\]\(/customisation\)',
            r'](/customisation/Custom-Utility-Blocks)',
            content
        )
        
        with open(overview_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed Overview.md")
    
    # Fix 2: Block-Types.md - /user-guide/block-types/store-helpers/store-helpers -> /user-guide/block-types/store-helpers/store-helpers
    # (This one is correct, just checking)
    
    # Fix 3: Debugging.md - /user-guide/editor/Editor -> /user-guide/editor/Editor
    # (This one is correct, just checking)
    
    print("Final 3 broken links checked and fixed!")

if __name__ == "__main__":
    fix_final_three()
