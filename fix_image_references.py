#!/usr/bin/env python3
"""
Script to fix image references in markdown files based on the image location checker results.
This script will replace incorrect image references with the correct paths.
"""

import re
import os
from pathlib import Path
from typing import Dict, List, Tuple

class ImageReferenceFixer:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.docs_dir = self.project_root / "docs"
        self.fixes_made = 0
        self.files_updated = set()
        
    def load_image_location_report(self) -> List[Dict]:
        """Load the image location report to get the fixes needed."""
        report_file = self.project_root / "image_location_report.txt"
        if not report_file.exists():
            print("Error: image_location_report.txt not found. Run check_image_locations.py first.")
            return []
        
        fixes = []
        current_file = None
        
        with open(report_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Look for file entries
            if line.startswith("File: "):
                current_file = line[6:]  # Remove "File: " prefix
            
            # Look for "Found elsewhere" entries
            elif line.startswith("Referenced at: ") and current_file:
                referenced_path = line[15:]  # Remove "Referenced at: " prefix
                
                # Get the next line which should be "Found at: "
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    if next_line.startswith("Found at: "):
                        found_at = next_line[11:]  # Remove "Found at: " prefix
                        
                        if found_at != "NOT_FOUND":
                            print(f"DEBUG: Parsed - File: {current_file}, Referenced: {referenced_path}, Found: '{found_at}'")
                            fixes.append({
                                'file': current_file,
                                'referenced_path': referenced_path,
                                'found_at': found_at
                            })
        
        return fixes
    
    def fix_image_references(self, fixes: List[Dict]) -> None:
        """Fix image references in markdown files."""
        print(f"Found {len(fixes)} image references to fix.")
        
        for fix in fixes:
            # Construct the full file path - the fix['file'] already includes docs/ prefix
            file_path = self.project_root / fix['file']
            if not file_path.exists():
                print(f"Warning: File not found: {fix['file']}")
                print(f"  Full path: {file_path}")
                continue
            
            print(f"Processing: {fix['file']}")
            print(f"  Referenced: {fix['referenced_path']}")
            print(f"  Should be: {fix['found_at']}")
            
            # Read the file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix HTML img tags
            old_src = fix['referenced_path']
            new_src = fix['found_at']
            
            # Pattern for HTML img tags: <img src="..." alt="..." />
            html_pattern = rf'<img([^>]+)src=["\']{re.escape(old_src)}["\']([^>]*)>'
            content = re.sub(html_pattern, rf'<img\1src="{new_src}"\2>', content)
            
            # Pattern for markdown images: ![alt](path)
            markdown_pattern = rf'!\[([^\]]*)\]\({re.escape(old_src)}\)'
            content = re.sub(markdown_pattern, rf'![\1]({new_src})', content)
            
            # Check if any changes were made
            if content != original_content:
                # Write the updated content back to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.fixes_made += 1
                self.files_updated.add(fix['file'])
                print(f"  ✓ Fixed")
            else:
                print(f"  ⚠ No changes made (pattern not found)")
        
        print(f"\nSummary:")
        print(f"  Files updated: {len(self.files_updated)}")
        print(f"  Total fixes made: {self.fixes_made}")
        
        if self.files_updated:
            print(f"\nFiles that were updated:")
            for file in sorted(self.files_updated):
                print(f"  - {file}")

def main():
    print("Image Reference Fixer for Docusaurus Project")
    print("=" * 50)
    
    # Get current directory
    current_dir = os.getcwd()
    print(f"Current directory: {current_dir}")
    
    # Initialize the fixer
    fixer = ImageReferenceFixer(current_dir)
    
    # Load the image location report
    print("Loading image location report...")
    fixes = fixer.load_image_location_report()
    
    if not fixes:
        print("No fixes needed or report not found.")
        return
    
    # Fix the image references
    print(f"\nStarting to fix {len(fixes)} image references...")
    fixer.fix_image_references(fixes)
    
    print("\nImage reference fixing complete!")

if __name__ == "__main__":
    main()
