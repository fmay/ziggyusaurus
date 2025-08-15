#!/usr/bin/env python3
"""
Script to remove sidebar_position from frontmatter in all markdown files.
Since we're now using manual sidebar configuration, these are no longer needed.
"""

import re
from pathlib import Path
from typing import List

class SidebarPositionRemover:
    def __init__(self, docs_root: str = "docs"):
        self.docs_root = Path(docs_root)
        self.updated_files = []
        self.errors = []
        
    def remove_sidebar_position(self, file_path: Path) -> bool:
        """Remove sidebar_position from a file's frontmatter"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if sidebar_position exists
            if 'sidebar_position:' not in content:
                print(f"⏭️  {file_path.name} has no sidebar_position")
                return False
            
            # Remove sidebar_position line from frontmatter
            if content.startswith('---'):
                # Find the end of frontmatter
                end_index = content.find('---', 3)
                if end_index != -1:
                    # Get the frontmatter section
                    frontmatter = content[:end_index]
                    
                    # Remove sidebar_position line
                    lines = frontmatter.split('\n')
                    new_lines = []
                    for line in lines:
                        if not line.strip().startswith('sidebar_position:'):
                            new_lines.append(line)
                    
                    # Reconstruct the file
                    new_frontmatter = '\n'.join(new_lines)
                    new_content = new_frontmatter + content[end_index:]
                    
                    # Write back to file
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    self.updated_files.append(str(file_path))
                    print(f"✅ Removed sidebar_position from {file_path.name}")
                    return True
                else:
                    print(f"⚠️  Could not find end of frontmatter in {file_path.name}")
                    return False
            else:
                print(f"⚠️  No frontmatter found in {file_path.name}")
                return False
                
        except Exception as e:
            error_msg = f"Error updating {file_path}: {e}"
            self.errors.append(error_msg)
            print(f"❌ {error_msg}")
            return False
    
    def process_all_files(self):
        """Process all markdown files to remove sidebar positions"""
        print("🚀 Removing sidebar_position from frontmatter...")
        print("=" * 60)
        
        # Find all markdown files
        md_files = list(self.docs_root.rglob("*.md"))
        
        # Process each file
        for file_path in md_files:
            self.remove_sidebar_position(file_path)
        
        print("\n" + "=" * 60)
        print("📊 SIDEBAR POSITION REMOVAL SUMMARY:")
        print(f"   Files updated: {len(self.updated_files)}")
        print(f"   Errors: {len(self.errors)}")
        
        if self.updated_files:
            print(f"\n📝 Updated files:")
            for file_path in self.updated_files:
                print(f"   - {file_path}")
        
        if self.errors:
            print(f"\n❌ Errors:")
            for error in self.errors:
                print(f"   {error}")
        
        print("\n✨ Sidebar positions removed!")
        print("\n💡 The manual sidebar configuration in sidebars.js now controls page ordering.")

def main():
    """Main function"""
    remover = SidebarPositionRemover()
    remover.process_all_files()

if __name__ == "__main__":
    main()
