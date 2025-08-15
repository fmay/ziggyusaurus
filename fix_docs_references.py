#!/usr/bin/env python3
"""
Script to fix documentation references in Docusaurus markdown files.
Fixes:
1. Width attributes from #width=800 format to {width=800} format
2. Image references to use proper Docusaurus paths
3. Markdown link references to use proper relative paths
"""

import os
import re
import glob
from pathlib import Path
from typing import List, Tuple, Dict

class DocsReferenceFixer:
    def __init__(self, docs_root: str = "docs", static_img_root: str = "static/img"):
        self.docs_root = Path(docs_root)
        self.static_img_root = Path(static_img_root)
        self.md_files = []
        self.image_files = set()
        self.fixed_files = []
        
    def scan_files(self):
        """Scan for markdown files and image files"""
        print("Scanning for markdown files...")
        self.md_files = list(self.docs_root.rglob("*.md"))
        print(f"Found {len(self.md_files)} markdown files")
        
        print("Scanning for image files...")
        for img_file in self.static_img_root.rglob("*.png"):
            self.image_files.add(img_file.name)
        print(f"Found {len(self.image_files)} PNG files")
        
    def fix_width_attributes(self, content: str) -> Tuple[str, bool]:
        """Fix width attributes from #width=800 format to {width=800} format"""
        original_content = content
        fixed = False
        
        # Pattern to match width attributes: #width=800
        width_pattern = r'#width=(\d+)'
        
        def replace_width(match):
            nonlocal fixed
            width_value = match.group(1)
            fixed = True
            print(f"  Fixed width attribute: #width={width_value} -> {{width={width_value}}}")
            return f'{{width={width_value}}}'
        
        content = re.sub(width_pattern, replace_width, content)
        
        # Also fix incorrectly placed width attributes inside parentheses
        # Pattern: ![alt](image.png{width=500}) -> ![alt](image.png){width=500}
        incorrect_width_pattern = r'!\[([^\]]*)\]\(([^)]*\.png)\{width=(\d+)\}\)'
        
        def fix_incorrect_width(match):
            nonlocal fixed
            alt_text = match.group(1)
            image_path = match.group(2)
            width_value = match.group(3)
            fixed = True
            print(f"  Fixed incorrectly placed width attribute: {image_path}{{width={width_value}}} -> {image_path}){{width={width_value}}}")
            return f'![{alt_text}]({image_path}){{width={width_value}}}'
        
        content = re.sub(incorrect_width_pattern, fix_incorrect_width, content)
        
        return content, fixed
    
    def fix_image_references(self, content: str, file_path: Path) -> Tuple[str, bool]:
        """Fix image references to use proper Docusaurus paths"""
        original_content = content
        fixed = False
        
        # Pattern to match image references: ![alt text](image.png)
        img_pattern = r'!\[([^\]]*)\]\(([^)]+\.png)\)'
        
        def replace_image(match):
            nonlocal fixed
            alt_text = match.group(1)
            image_name = match.group(2)
            
            # Check if image exists in static/img
            if image_name in self.image_files:
                # Convert to Docusaurus path format
                # Find the actual path of the image
                for img_path in self.static_img_root.rglob(image_name):
                    # Calculate relative path from docs root to static/img
                    relative_path = f"/img/{img_path.relative_to(self.static_img_root)}"
                    fixed = True
                    print(f"  Fixed image: {image_name} -> {relative_path}")
                    return f'![{alt_text}]({relative_path})'
            
            # If image not found, keep original but warn
            print(f"  Warning: Image not found: {image_name}")
            return match.group(0)
        
        content = re.sub(img_pattern, replace_image, content)
        return content, fixed
    
    def fix_markdown_links(self, content: str, file_path: Path) -> Tuple[str, bool]:
        """Fix markdown link references to use proper paths"""
        original_content = content
        fixed = False
        
        # Pattern to match markdown links: [text](filename.md) or [text](/incorrect/path)
        link_pattern = r'\[([^\]]*)\]\(([^)]+)\)'
        
        def replace_link(match):
            nonlocal fixed
            link_text = match.group(1)
            link_path = match.group(2)
            
            # Skip external links and anchors
            if link_path.startswith('http') or link_path.startswith('#') or link_path.startswith('mailto:'):
                return match.group(0)
            
            # Handle .md files (relative or absolute)
            if link_path.endswith('.md'):
                # Find the referenced file
                target_file = None
                for md_file in self.md_files:
                    if md_file.name == link_path or md_file.name == link_path.split('/')[-1]:
                        target_file = md_file
                        break
                
                if target_file:
                    # Convert to Docusaurus format (remove .md extension)
                    relative_path = f"/{target_file.relative_to(self.docs_root).with_suffix('')}"
                    fixed = True
                    print(f"  Fixed .md link: {link_path} -> {relative_path}")
                    return f'[{link_text}]({relative_path})'
                else:
                    print(f"  Warning: Referenced .md file not found: {link_path}")
                    return match.group(0)
            
            # Handle absolute paths that don't start with /user-guide/
            if link_path.startswith('/') and not link_path.startswith('/user-guide/'):
                # Try to find the file by name in the docs structure
                target_file = None
                path_parts = link_path.strip('/').split('/')
                
                # Look for files with matching names in the expected locations
                for md_file in self.md_files:
                    if md_file.name.replace('.md', '') == path_parts[-1]:
                        # Check if the path structure matches
                        file_path_parts = list(md_file.relative_to(self.docs_root).with_suffix('').parts)
                        
                        # If it's a block-types link, ensure it goes to user-guide/block-types
                        if 'block-types' in path_parts and 'block-types' in file_path_parts:
                            if 'user-guide' not in file_path_parts:
                                file_path_parts.insert(0, 'user-guide')
                        
                        # If it's a core/utility/hubspot/salesforce link, ensure proper structure
                        if any(part in path_parts for part in ['core', 'utility', 'hubspot', 'salesforce']):
                            if 'user-guide' not in file_path_parts:
                                file_path_parts.insert(0, 'user-guide')
                            if 'block-types' not in file_path_parts:
                                file_path_parts.insert(1, 'block-types')
                        
                        # If it's a user-guide topic, ensure it starts with /user-guide/
                        if any(part in path_parts for part in ['editor', 'connections', 'secrets', 'variables', 'batching', 'queuing', 'scheduled-flows', 'dev-prod-modes', 'memory-store', 'data-store', 'auditing', 'error-handling', 'data-browser', 'tags', 'tests', 'alerts', 'logging', 'global-settings', 'transferring-data', 'troubleshooting', 'security', 'deployment', 'monitoring', 'structures', 'launching']):
                            if 'user-guide' not in file_path_parts:
                                file_path_parts.insert(0, 'user-guide')
                        
                        target_file = md_file
                        break
                
                if target_file:
                    # Build the correct path
                    correct_path = f"/{'/'.join(file_path_parts)}"
                    fixed = True
                    print(f"  Fixed absolute path: {link_path} -> {correct_path}")
                    return f'[{link_text}]({correct_path})'
                else:
                    print(f"  Warning: Could not resolve absolute path: {link_path}")
                    return match.group(0)
            
            # Handle relative paths that need to be made absolute
            elif not link_path.startswith('/'):
                # Find the referenced file
                target_file = None
                for md_file in self.md_files:
                    if md_file.name == link_path or md_file.name == link_path.split('/')[-1]:
                        target_file = md_file
                        break
                
                if target_file:
                    # Convert to absolute path
                    relative_path = f"/{target_file.relative_to(self.docs_root).with_suffix('')}"
                    fixed = True
                    print(f"  Fixed relative path: {link_path} -> {relative_path}")
                    return f'[{link_text}]({relative_path})'
                else:
                    print(f"  Warning: Referenced file not found: {link_path}")
                    return match.group(0)
            
            return match.group(0)
        
        content = re.sub(link_pattern, replace_link, content)
        return content, fixed
    
    def process_file(self, file_path: Path) -> bool:
        """Process a single markdown file"""
        print(f"Processing: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            any_fixes = False
            
            # Step 1: Fix width attributes first
            content, width_fixed = self.fix_width_attributes(content)
            if width_fixed:
                any_fixes = True
            
            # Step 2: Fix image references
            content, images_fixed = self.fix_image_references(content, file_path)
            if images_fixed:
                any_fixes = True
            
            # Step 3: Fix markdown links
            content, links_fixed = self.fix_markdown_links(content, file_path)
            if links_fixed:
                any_fixes = True
            
            # Write back if changes were made
            if any_fixes:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.fixed_files.append(str(file_path))
                print(f"  ✅ Updated file")
                return True
            else:
                print(f"  ⏭️  No changes needed")
                return False
                
        except Exception as e:
            print(f"  ❌ Error processing file: {e}")
            return False
    
    def run(self):
        """Run the fixer on all markdown files"""
        print("🚀 Starting documentation reference fixer...")
        print("=" * 50)
        print("📋 Fix order:")
        print("   1. Width attributes (#width=800 -> {width=800})")
        print("   2. Image references (-> proper Docusaurus paths)")
        print("   3. Markdown links (-> proper relative paths)")
        print("=" * 50)
        
        self.scan_files()
        print()
        
        print("🔧 Processing files...")
        print("-" * 30)
        
        processed_count = 0
        fixed_count = 0
        
        for md_file in self.md_files:
            if self.process_file(md_file):
                fixed_count += 1
            processed_count += 1
            print()
        
        print("=" * 50)
        print(f"📊 Summary:")
        print(f"   Files processed: {processed_count}")
        print(f"   Files updated: {fixed_count}")
        print(f"   Files unchanged: {processed_count - fixed_count}")
        
        if self.fixed_files:
            print(f"\n📝 Updated files:")
            for file_path in self.fixed_files:
                print(f"   - {file_path}")
        
        print("\n✨ Done!")

def main():
    """Main function"""
    fixer = DocsReferenceFixer()
    fixer.run()

if __name__ == "__main__":
    main()
