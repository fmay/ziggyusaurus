#!/usr/bin/env python3
"""
Script to scan markdown files for broken internal links and fix them.
This script finds links like [Queue](Queuing.md) and validates the target file exists.
If the target doesn't exist, it searches the docs folder for the correct path.
"""

import re
import os
from pathlib import Path
from typing import Dict, List, Tuple, Set

class MarkdownLinkFixer:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.docs_dir = self.project_root / "docs"
        self.all_md_files = set()
        self.links_fixed = 0
        self.files_updated = set()
        self.broken_links = []
        
    def scan_all_markdown_files(self) -> None:
        """Scan and collect all markdown files in the docs directory."""
        print("Scanning for all markdown files...")
        for file_path in self.docs_dir.rglob("*.md"):
            # Store relative paths from docs directory
            relative_path = file_path.relative_to(self.docs_dir)
            self.all_md_files.add(str(relative_path))
        print(f"Found {len(self.all_md_files)} markdown files")
    
    def find_file_by_name(self, target_name: str) -> str:
        """Find a file by name in the docs directory, returning the relative path."""
        # Handle anchor links by extracting just the file path
        if '#' in target_name:
            file_path = target_name.split('#')[0]
        else:
            file_path = target_name
            
        # First try exact match
        if file_path in self.all_md_files:
            return target_name  # Return full path with anchor if it was there
        
        # Try without .md extension
        if file_path.endswith('.md'):
            name_without_ext = file_path[:-3]
        else:
            name_without_ext = file_path
        
        # Search for files that match the name (case-insensitive)
        for md_file_path in self.all_md_files:
            file_name = Path(md_file_path).stem  # filename without extension
            if file_name.lower() == name_without_ext.lower():
                # Reconstruct the full path with anchor if it was there
                if '#' in target_name:
                    anchor = target_name.split('#')[1]
                    return f"{md_file_path}#{anchor}"
                else:
                    return md_file_path
        
        # If still not found, try partial matches
        for md_file_path in self.all_md_files:
            file_name = Path(md_file_path).stem
            if name_without_ext.lower() in file_name.lower():
                # Reconstruct the full path with anchor if it was there
                if '#' in target_name:
                    anchor = target_name.split('#')[1]
                    return f"{md_file_path}#{anchor}"
                else:
                    return md_file_path
        
        return None
    
    def fix_links_in_file(self, file_path: Path) -> bool:
        """Fix broken links in a single markdown file."""
        print(f"Processing: {file_path.relative_to(self.project_root)}")
        
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern to match markdown links: [text](path)
        # This regex captures:
        # - link text: ([^\]]+)
        # - link path: ([^)]+)
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        
        def replacement(match):
            link_text = match.group(1)
            link_path = match.group(2)
            
            # Skip external links (http, https, mailto, etc.)
            if link_path.startswith(('http://', 'https://', 'mailto:', 'tel:', '#')):
                return match.group(0)  # Keep original
            
            # Skip links that are already absolute paths from docs root
            if link_path.startswith('/'):
                link_path = link_path[1:]  # Remove leading slash
                if link_path in self.all_md_files:
                    return match.group(0)  # Keep original
            
            # Check if the target file exists
            target_file = self.find_file_by_name(link_path)
            
            if target_file and target_file != link_path:
                # Found a different path, fix the link
                new_link = f'[{link_text}]({target_file})'
                print(f"  Fixed: [{link_text}]({link_path}) -> [{link_text}]({target_file})")
                
                # Record the fix
                self.broken_links.append({
                    'file': str(file_path.relative_to(self.project_root)),
                    'old_link': f'[{link_text}]({link_path})',
                    'new_link': f'[{link_text}]({target_file})',
                    'target_found': target_file
                })
                
                self.links_fixed += 1
                return new_link
            elif not target_file:
                # Could not find the target file
                print(f"  ⚠ Broken link: [{link_text}]({link_path}) - target not found")
                self.broken_links.append({
                    'file': str(file_path.relative_to(self.project_root)),
                    'old_link': f'[{link_text}]({link_path})',
                    'new_link': None,
                    'target_found': None
                })
                return match.group(0)  # Keep original
            
            return match.group(0)  # Keep original
        
        # Apply the replacement
        content = re.sub(link_pattern, replacement, content)
        
        # Check if any changes were made
        if content != original_content:
            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.files_updated.add(str(file_path.relative_to(self.project_root)))
            print(f"  ✓ File updated")
            return True
        else:
            print(f"  ⚠ No broken links found")
            return False
    
    def run_link_fixing(self) -> None:
        """Run the link fixing process on all markdown files."""
        print("Markdown Link Fixer")
        print("=" * 50)
        print(f"Project root: {self.project_root}")
        print(f"Docs directory: {self.docs_dir}")
        
        # First scan all markdown files
        self.scan_all_markdown_files()
        
        # Find all markdown files to process
        markdown_files = []
        for file_path in self.docs_dir.rglob("*.md"):
            markdown_files.append(file_path)
        
        print(f"\nFound {len(markdown_files)} markdown files to process")
        
        # Process each file
        print("\nStarting link fixing process...")
        for file_path in markdown_files:
            self.fix_links_in_file(file_path)
            print()  # Add spacing between files
        
        # Print summary
        print("=" * 50)
        print("LINK FIXING SUMMARY")
        print("=" * 50)
        print(f"Files processed: {len(markdown_files)}")
        print(f"Files updated: {len(self.files_updated)}")
        print(f"Total links fixed: {self.links_fixed}")
        
        if self.broken_links:
            print(f"\nDETAILED REPORT:")
            print(f"=" * 50)
            
            # Group by status
            fixed_links = [link for link in self.broken_links if link['new_link']]
            unfixed_links = [link for link in self.broken_links if not link['new_link']]
            
            if fixed_links:
                print(f"\n✅ LINKS THAT WERE FIXED ({len(fixed_links)}):")
                for link in fixed_links:
                    print(f"  File: {link['file']}")
                    print(f"    Old: {link['old_link']}")
                    print(f"    New: {link['new_link']}")
                    print(f"    Target found at: {link['target_found']}")
                    print()
            
            if unfixed_links:
                print(f"\n❌ LINKS THAT COULD NOT BE FIXED ({len(unfixed_links)}):")
                for link in unfixed_links:
                    print(f"  File: {link['file']}")
                    print(f"    Broken link: {link['old_link']}")
                    print(f"    Target not found")
                    print()
        
        if self.files_updated:
            print(f"\nFiles that were updated:")
            for file in sorted(self.files_updated):
                print(f"  - {file}")
        
        if self.links_fixed == 0:
            print("\nNo broken links were found or fixed.")
        else:
            print(f"\nLink fixing complete! {self.links_fixed} links were fixed.")

def main():
    # Get current directory
    current_dir = os.getcwd()
    
    # Initialize the link fixer
    link_fixer = MarkdownLinkFixer(current_dir)
    
    # Run the link fixing process
    link_fixer.run_link_fixing()

if __name__ == "__main__":
    main()
