#!/usr/bin/env python3
"""
Script to find and fix unclosed markdown image references.
This script searches for images like ![alt](path that are missing the closing )
and fixes them by adding the missing parenthesis.
"""

import re
import os
from pathlib import Path
from typing import List

class UnclosedImageFixer:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.docs_dir = self.project_root / "docs"
        self.fixes_made = 0
        self.files_updated = set()
        
    def find_markdown_files(self) -> List[Path]:
        """Find all markdown files in the docs directory."""
        markdown_files = []
        for file_path in self.docs_dir.rglob("*.md"):
            markdown_files.append(file_path)
        return markdown_files
    
    def fix_unclosed_images(self, file_path: Path) -> bool:
        """Fix unclosed markdown image references in a single markdown file."""
        print(f"Processing: {file_path.relative_to(self.project_root)}")
        
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern to match unclosed markdown images: ![alt](path (missing closing )
        # This regex captures:
        # - alt text: ([^\]]*)
        # - path: ([^)]*)
        # But ensures the path doesn't end with a closing parenthesis
        unclosed_pattern = r'!\[([^\]]*)\]\(([^)]*?)(?<!\))$'
        
        # Also look for unclosed images that might be followed by other content
        # This is more complex as we need to find where the image should end
        # Look for patterns like ![alt](path followed by whitespace, newline, or other content
        unclosed_with_content_pattern = r'!\[([^\]]*)\]\(([^)]*?)(?=\s|$|\.|,|;|\)|\[|\]|\{|\})'
        
        def replacement(match):
            alt_text = match.group(1)
            image_path = match.group(2)
            
            # Check if this is actually an unclosed image (missing closing parenthesis)
            if not image_path.endswith(')'):
                new_image = f'![{alt_text}]({image_path})'
                print(f"  Fixed unclosed image: ![{alt_text}]({image_path} -> ![{alt_text}]({image_path})")
                
                self.fixes_made += 1
                return new_image
            
            return match.group(0)  # Keep original if it's already correct
        
        # Apply the replacement
        content = re.sub(unclosed_pattern, replacement, content, flags=re.MULTILINE)
        
        # Also look for unclosed images that might be followed by other content
        # This requires a more sophisticated approach
        lines = content.split('\n')
        for i, line in enumerate(lines):
            # Look for lines that start with ![ but don't have a closing )
            if line.strip().startswith('![') and '](' in line and not line.strip().endswith(')'):
                # This might be an unclosed image
                print(f"  Potential unclosed image found on line {i+1}: {line.strip()}")
        
        # Check if any changes were made
        if content != original_content:
            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.files_updated.add(str(file_path.relative_to(self.project_root)))
            print(f"  ✓ File updated")
            return True
        else:
            print(f"  ⚠ No unclosed images found")
            return False
    
    def run_fixing(self) -> None:
        """Run the unclosed image fixing process on all markdown files."""
        print("Unclosed Markdown Image Fixer")
        print("=" * 50)
        print(f"Project root: {self.project_root}")
        print(f"Docs directory: {self.docs_dir}")
        
        # Find all markdown files
        markdown_files = self.find_markdown_files()
        print(f"\nFound {len(markdown_files)} markdown files")
        
        # Process each file
        print("\nStarting unclosed image fixing process...")
        for file_path in markdown_files:
            self.fix_unclosed_images(file_path)
            print()  # Add spacing between files
        
        # Print summary
        print("=" * 50)
        print("UNCLOSED IMAGE FIXING SUMMARY")
        print("=" * 50)
        print(f"Files processed: {len(markdown_files)}")
        print(f"Files updated: {len(self.files_updated)}")
        print(f"Total unclosed images fixed: {self.fixes_made}")
        
        if self.files_updated:
            print(f"\nFiles that were updated:")
            for file in sorted(self.files_updated):
                print(f"  - {file}")
        
        if self.fixes_made == 0:
            print("\nNo unclosed markdown images were found or fixed.")
        else:
            print(f"\nUnclosed image fixing complete! {self.fixes_made} images were fixed.")

def main():
    # Get current directory
    current_dir = os.getcwd()
    
    # Initialize the fixer
    fixer = UnclosedImageFixer(current_dir)
    
    # Run the fixing process
    fixer.run_fixing()

if __name__ == "__main__":
    main()
