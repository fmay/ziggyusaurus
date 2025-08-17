#!/usr/bin/env python3
"""
Script to scan all markdown files referenced in the sidebar and check for broken links and image references.
This script parses the sidebars.js file to get all referenced markdown files, then scans each one for:
1. Broken internal links in format [text](path)
2. Broken image references in format <img src="path"> or ![alt](path)
"""

import re
import os
import json
from pathlib import Path
from typing import List, Dict, Set, Tuple

class SidebarFileScanner:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.docs_dir = self.project_root / "docs"
        self.sidebar_file = self.project_root / "sidebars.js"
        self.broken_links = []
        self.broken_images = []
        self.links_fixed = []
        self.scanned_files = set()
        
    def extract_sidebar_files(self) -> List[str]:
        """Extract all markdown file references from sidebars.js."""
        print("Extracting markdown file references from sidebars.js...")
        
        try:
            with open(self.sidebar_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract all file references (they don't have .md extension in sidebar)
            # Pattern: 'user-guide/block-types/core/Receiver' (without .md)
            file_pattern = r"'([^']+)'"
            matches = re.findall(file_pattern, content)
            
            # Filter out non-file references (like category labels)
            file_references = []
            for match in matches:
                # Skip if it's just a label or doesn't look like a file path
                if '/' in match and not match.startswith('case-studies') and not match.startswith('user-guide'):
                    continue
                if match in ['About', 'Case Studies', 'User Guide', 'Editor', 'Block Types', 'Core', 'Utility', 'SQL', 'HubSpot', 'Salesforce', 'Store Helpers']:
                    continue
                file_references.append(match)
            
            print(f"Found {len(file_references)} file references in sidebar")
            return file_references
            
        except Exception as e:
            print(f"Error reading sidebars.js: {e}")
            return []
    
    def resolve_file_path(self, sidebar_ref: str) -> Path:
        """Convert sidebar reference to actual file path."""
        # Add .md extension if not present
        if not sidebar_ref.endswith('.md'):
            sidebar_ref += '.md'
        
        # Construct full path
        file_path = self.docs_dir / sidebar_ref
        
        return file_path
    
    def check_file_exists(self, file_path: Path) -> bool:
        """Check if a file exists."""
        return file_path.exists() and file_path.is_file()
    
    def scan_file_for_links(self, file_path: Path) -> List[Dict]:
        """Scan a markdown file for internal links and check if they exist."""
        broken_links = []
        links_fixed = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Pattern to match markdown links: [text](path) - NOT images
            # This regex specifically excludes images by using negative lookbehind for !
            link_pattern = r'(?<!!)\[([^\]]+)\]\(([^)]+)\)'
            matches = re.findall(link_pattern, content)
            
            for alt_text, link_path in matches:
                # Skip external links
                if link_path.startswith(('http://', 'https://', 'mailto:', '#')):
                    continue
                
                original_link = f'[{alt_text}]({link_path})'
                new_link_path = link_path
                
                # Convert absolute paths to relative paths
                if link_path.startswith('/'):
                    # Remove leading slash to make it relative
                    new_link_path = link_path[1:]
                    
                    # If the link is to a file in the same directory as current file
                    current_dir = file_path.parent
                    target_file = self.docs_dir / new_link_path
                    
                    # Check if target file exists
                    if target_file.exists():
                        # Calculate relative path from current file to target
                        try:
                            relative_path = target_file.relative_to(current_dir)
                            new_link_path = str(relative_path)
                            
                            # Record the fix
                            links_fixed.append({
                                'file': str(file_path.relative_to(self.project_root)),
                                'link_text': alt_text,
                                'old_path': link_path,
                                'new_path': new_link_path,
                                'type': 'absolute_to_relative'
                            })
                            
                            # Replace the link in content
                            new_link = f'[{alt_text}]({new_link_path})'
                            content = content.replace(original_link, new_link)
                            
                        except ValueError:
                            # If we can't calculate relative path, just remove the leading slash
                            pass
                
                # Handle anchor tags by separating file path from anchor
                file_path_part = new_link_path
                anchor_part = ""
                if '#' in new_link_path:
                    file_path_part, anchor_part = new_link_path.split('#', 1)
                    anchor_part = f"#{anchor_part}"
                
                # Construct expected file path - handle relative paths correctly
                if file_path_part.startswith('/'):
                    # Absolute path from docs root
                    if file_path_part.endswith('.md'):
                        expected_path = self.docs_dir / file_path_part[1:]  # Remove leading slash
                    else:
                        expected_path = self.docs_dir / f"{file_path_part[1:]}.md"
                else:
                    # Relative path - try multiple resolution strategies like Docusaurus does
                    # Strategy 1: Try relative to current file's directory
                    current_dir = file_path.parent
                    if file_path_part.endswith('.md'):
                        expected_path = current_dir / file_path_part
                    else:
                        expected_path = current_dir / f"{file_path_part}.md"
                    
                    # Strategy 2: If not found, try relative to docs root
                    if not expected_path.exists():
                        if file_path_part.endswith('.md'):
                            expected_path = self.docs_dir / file_path_part
                        else:
                            expected_path = self.docs_dir / f"{file_path_part}.md"
                
                # Check if file exists
                if not self.check_file_exists(expected_path):
                    broken_links.append({
                        'file': str(file_path.relative_to(self.project_root)),
                        'link_text': alt_text,
                        'link_path': new_link_path,
                        'expected_path': str(expected_path.relative_to(self.project_root)),
                        'type': 'broken_link'
                    })
            
            # Write the updated content back to the file if any links were fixed
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                    
        except Exception as e:
            print(f"Error scanning file {file_path}: {e}")
        
        return broken_links, links_fixed
    
    def scan_file_for_images(self, file_path: Path) -> List[Dict]:
        """Scan a markdown file for image references and check if they exist."""
        broken_images = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Pattern 1: HTML img tags: <img src="path" ...> (but not inside code blocks)
            html_img_pattern = r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>'
            html_matches = re.findall(html_img_pattern, content)
            
            for img_src in html_matches:
                # Check if this image is inside a code block
                if not self.is_inside_code_block(content, img_src):
                    if not self.check_image_exists(img_src):
                        broken_images.append({
                            'file': str(file_path.relative_to(self.project_root)),
                            'image_src': img_src,
                            'type': 'html_img',
                            'line': self.find_line_number(content, img_src)
                        })
            
            # Pattern 2: Markdown images: ![alt](path) (but not inside code blocks)
            md_img_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
            md_matches = re.findall(md_img_pattern, content)
            
            for alt_text, img_path in md_matches:
                # Check if this image is inside a code block
                if not self.is_inside_code_block(content, f'![{alt_text}]({img_path})'):
                    if not self.check_image_exists(img_path):
                        broken_images.append({
                            'file': str(file_path.relative_to(self.project_root)),
                            'image_src': img_path,
                            'alt_text': alt_text,
                            'type': 'markdown_img',
                            'line': self.find_line_number(content, img_path)
                        })
                    
        except Exception as e:
            print(f"Error scanning file {file_path}: {e}")
        
        return broken_images
    
    def check_image_exists(self, img_src: str) -> bool:
        """Check if an image file exists at the specified path."""
        # Remove leading slash if present
        if img_src.startswith('/'):
            img_src = img_src[1:]
        
        # Construct full path - images are stored in static/img/
        img_path = self.project_root / 'static' / img_src
        
        return img_path.exists() and img_path.is_file()
    
    def find_line_number(self, content: str, search_text: str) -> int:
        """Find the line number where text appears in content."""
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            if search_text in line:
                return i
        return 0
    
    def is_inside_code_block(self, content: str, search_text: str) -> bool:
        """Check if the search text is inside a code block (```...```)."""
        lines = content.split('\n')
        in_code_block = False
        code_block_start = -1
        
        for i, line in enumerate(lines):
            # Check for code block markers
            if line.strip().startswith('```'):
                if not in_code_block:
                    # Starting a code block
                    in_code_block = True
                    code_block_start = i
                else:
                    # Ending a code block
                    in_code_block = False
                    code_block_start = -1
                continue
            
            # If we're in a code block and find the search text, return True
            if in_code_block and search_text in line:
                return True
        
        return False
    
    def scan_all_sidebar_files(self) -> None:
        """Scan all files referenced in the sidebar for broken links and images."""
        print("Sidebar File Scanner")
        print("=" * 60)
        
        # Extract files from sidebar
        sidebar_files = self.extract_sidebar_files()
        
        if not sidebar_files:
            print("No files found in sidebar configuration")
            return
        
        print(f"\nScanning {len(sidebar_files)} files referenced in sidebar...")
        print("-" * 60)
        
        # Scan each file
        for sidebar_ref in sidebar_files:
            file_path = self.resolve_file_path(sidebar_ref)
            
            if not self.check_file_exists(file_path):
                print(f"⚠️  Sidebar references non-existent file: {file_path}")
                continue
            
            print(f"Scanning: {file_path.relative_to(self.project_root)}")
            self.scanned_files.add(str(file_path.relative_to(self.project_root)))
            
            # Check for broken links and fix absolute paths
            broken_links, links_fixed = self.scan_file_for_links(file_path)
            self.broken_links.extend(broken_links)
            self.links_fixed.extend(links_fixed)
            
            # Check for broken images
            broken_images = self.scan_file_for_images(file_path)
            self.broken_images.extend(broken_images)
            
            if broken_links or broken_images:
                print(f"  Found {len(broken_links)} broken links, {len(broken_images)} broken images")
            else:
                print(f"  ✓ No issues found")
        
        # Print summary
        self.print_summary()
    
    def print_summary(self) -> None:
        """Print a summary of all findings."""
        print("\n" + "=" * 60)
        print("SCANNING SUMMARY")
        print("=" * 60)
        print(f"Files scanned: {len(self.scanned_files)}")
        print(f"Total broken links found: {len(self.broken_links)}")
        print(f"Total broken images found: {len(self.broken_images)}")
        print(f"Total links fixed (absolute to relative): {len(self.links_fixed)}")
        
        if self.broken_links:
            print(f"\nBROKEN LINKS ({len(self.broken_links)}):")
            print("-" * 40)
            for link in self.broken_links:
                print(f"File: {link['file']}")
                print(f"  Link: [{link['link_text']}]({link['link_path']})")
                print(f"  Expected: {link['expected_path']}")
                print()
        
        if self.links_fixed:
            print(f"\nLINKS FIXED - ABSOLUTE TO RELATIVE ({len(self.links_fixed)}):")
            print("-" * 50)
            for link in self.links_fixed:
                print(f"File: {link['file']}")
                print(f"  Link: [{link['link_text']}]({link['old_path']})")
                print(f"  Fixed to: [{link['link_text']}]({link['new_path']})")
                print()
        
        if self.broken_images:
            print(f"\nBROKEN IMAGES ({len(self.broken_images)}):")
            print("-" * 40)
            for img in self.broken_images:
                print(f"File: {img['file']}")
                if img['type'] == 'html_img':
                    print(f"  HTML Image: <img src=\"{img['image_src']}\">")
                else:
                    print(f"  Markdown Image: ![{img.get('alt_text', '')}]({img['image_src']})")
                if img.get('line'):
                    print(f"  Line: {img['line']}")
                print()

def main():
    # Get current directory
    current_dir = os.getcwd()
    
    # Initialize the scanner
    scanner = SidebarFileScanner(current_dir)
    
    # Run the scanning process
    scanner.scan_all_sidebar_files()

if __name__ == "__main__":
    main()
