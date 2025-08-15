#!/usr/bin/env python3
"""
Backup script for docs before running the fixer
"""

import shutil
import datetime
from pathlib import Path

def backup_docs():
    """Create a backup of the docs folder"""
    docs_path = Path("docs")
    if not docs_path.exists():
        print("❌ Docs folder not found!")
        return
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = Path(f"docs_backup_{timestamp}")
    
    print(f"🔄 Creating backup: {backup_path}")
    shutil.copytree(docs_path, backup_path)
    print(f"✅ Backup created successfully at: {backup_path}")

if __name__ == "__main__":
    backup_docs()
