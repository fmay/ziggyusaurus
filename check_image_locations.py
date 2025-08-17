#!/usr/bin/env python3
"""
Script to scan markdown files for image references and check their locations.
Reports images that weren't found at the specified path but were found elsewhere in subfolders.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple, Set

class ImageLocationChecker:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.docs_dir = self.project_root / "docs"
        self.static_img_dir = self.project_root / "static" / "img"
        
        # Track image references and their locations
        self.image_references: Dict[str, List[Dict]] = {}
        self.not_found_at_location: List[Dict] = []
        self.found_elsewhere: List[Dict] = []
        
        # All image files in static/img (for searching subfolders)
        self.all_static_images: Set[str] = set()

    def scan_static_images(self) -> None:
        """Scan all image files in static/img directory."""
        print("Scanning static/img directory for all images...")
        
        if not self.static_img_dir.exists():
            print(f"Warning: {self.static_img_dir} does not exist")
            return
            
        for img_file in self.static_img_dir.rglob("*"):
            if img_file.is_file() and img_file.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg']:
                # Store relative path from static/img
                relative_path = img_file.relative_to(self.static_img_dir)
                self.all_static_images.add(str(relative_path))

    def find_image_in_subfolders(self, image_name: str) -> str:
        """Search for an image in subfolders and return the found path."""
        # Try exact match first
        if image_name in self.all_static_images:
            return str(image_name)
        
        # Try matching just the filename
        filename = Path(image_name).name
        for static_path in self.all_static_images:
            if Path(static_path).name == filename:
                return str(static_path)
        
        return ""

    def clean_image_path(self, path: str) -> str:
        """Clean and validate an image path."""
        # Remove any whitespace or newlines
        path = path.strip()
        
        # Skip if path is too short or contains obvious non-path characters
        if len(path) < 3 or '\n' in path or '\r' in path:
            return ""
        
        # Skip if it looks like content rather than a path
        if len(path) > 200 or ' ' in path:
            return ""
            
        return path

    def scan_markdown_files(self) -> None:
        """Scan all markdown files for image references."""
        print("Scanning markdown files for image references...")
        
        for file_path in self.docs_dir.rglob("*.md"):
            relative_path = file_path.relative_to(self.project_root)
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            
            self.image_references[str(relative_path)] = []
            
            # Pattern 1: <img src="..." alt="..." />
            img_pattern = r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>'
            img_matches = re.findall(img_pattern, content)
            
            for img_src in img_matches:
                clean_path = self.clean_image_path(img_src)
                if clean_path:
                    self.image_references[str(relative_path)].append({
                        'type': 'html',
                        'src': clean_path,
                        'file': str(relative_path)
                    })
            
            # Pattern 2: ![alt](path)
            markdown_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
            markdown_matches = re.findall(markdown_pattern, content)
            
            for alt_text, img_path in markdown_matches:
                clean_path = self.clean_image_path(img_path)
                if clean_path:
                    self.image_references[str(relative_path)].append({
                        'type': 'markdown',
                        'src': clean_path,
                        'file': str(relative_path)
                    })

    def check_image_locations(self) -> None:
        """Check if referenced images exist at their specified locations."""
        print("Checking image locations...")
        
        for file_path, references in self.image_references.items():
            for ref in references:
                img_src = ref['src']
                
                # Skip external URLs
                if img_src.startswith(('http://', 'https://', '//')):
                    continue
                
                # Clean the path - keep the img/ prefix as it's correct
                if img_src.startswith('/'):
                    img_src = img_src[1:]  # Remove leading slash
                
                # Check if image exists at the referenced location
                # The img_src contains the img/ prefix (e.g., "img/flows/launching/execution-keys.png")
                # We need to check if it exists at static/img/img/flows/launching/execution-keys.png
                # But since your actual structure is static/img/flows/launching/execution-keys.png,
                # we need to remove the img/ prefix when checking existence
                check_path = img_src
                if check_path.startswith('img/'):
                    check_path = check_path[4:]  # Remove 'img/' prefix
                
                expected_path = self.static_img_dir / check_path
                
                if expected_path.exists():
                    # Image found at the correct location - this is good!
                    continue
                else:
                    # Image not found at specified location, search in subfolders
                    found_path = self.find_image_in_subfolders(check_path)
                    
                    if found_path:
                        # Found elsewhere in subfolders
                        self.found_elsewhere.append({
                            'file': ref['file'],
                            'type': ref['type'],
                            'referenced_path': img_src,
                            'found_at': f'img/{found_path}'  # Add img/ prefix to match reference format
                        })
                    else:
                        # Not found anywhere
                        self.not_found_at_location.append({
                            'file': ref['file'],
                            'type': ref['type'],
                            'referenced_path': img_src,
                            'found_at': 'NOT_FOUND'
                        })

    def generate_report(self) -> None:
        """Generate a report of findings."""
        print("\n" + "="*80)
        print("IMAGE LOCATION ANALYSIS REPORT")
        print("="*80)
        
        total_refs = sum(len(refs) for refs in self.image_references.values())
        found_elsewhere_count = len(self.found_elsewhere)
        not_found_count = len(self.not_found_at_location)
        
        print(f"\nSUMMARY:")
        print(f"  Total image references found: {total_refs}")
        print(f"  Found elsewhere in subfolders: {found_elsewhere_count}")
        print(f"  Not found anywhere: {not_found_count}")
        
        if self.found_elsewhere:
            print(f"\nIMAGES FOUND ELSEWHERE IN SUBFOLDERS:")
            print("(These were referenced at one path but found at another)")
            for item in self.found_elsewhere:
                print(f"  File: {item['file']}")
                print(f"    Type: {item['type']}")
                print(f"    Referenced at: {item['referenced_path']}")
                print(f"    Found at: {item['found_at']}")
                print()
        
        if self.not_found_at_location:
            print(f"\nIMAGES NOT FOUND ANYWHERE:")
            print("(These references point to non-existent images)")
            for item in self.not_found_at_location:
                print(f"  File: {item['file']}")
                print(f"    Type: {item['type']}")
                print(f"    Referenced at: {item['referenced_path']}")
                print()

    def save_report_to_file(self, filename: str = "image_location_report.txt") -> None:
        """Save the report to a text file."""
        with open(filename, 'w', encoding='utf-8') as f:
            # Redirect print output to file
            import sys
            original_stdout = sys.stdout
            sys.stdout = f
            
            self.generate_report()
            
            # Restore stdout
            sys.stdout = original_stdout
        
        print(f"\nReport saved to: {filename}")

    def run_analysis(self) -> None:
        """Run the complete image location analysis."""
        print("Starting image location analysis...")
        print(f"Project root: {self.project_root}")
        print(f"Docs directory: {self.docs_dir}")
        print(f"Static img directory: {self.static_img_dir}")
        
        self.scan_static_images()
        self.scan_markdown_files()
        self.check_image_locations()
        self.generate_report()

def main():
    """Main function to run the image location analysis."""
    current_dir = os.getcwd()
    
    print("Image Location Checker for Docusaurus Project")
    print("=" * 50)
    print(f"Current directory: {current_dir}")
    
    # Check if we're in the right directory
    if not os.path.exists("docs") or not os.path.exists("static"):
        print("Error: This script should be run from the root of your Docusaurus project")
        print("Make sure you have 'docs' and 'static' directories")
        return
    
    # Create checker and run analysis
    checker = ImageLocationChecker(current_dir)
    checker.run_analysis()
    
    # Save report to file
    checker.save_report_to_file()
    
    print("\nAnalysis complete!")
    print("\nNEXT STEPS:")
    print("1. Review the report above")
    print("2. Check the 'image_location_report.txt' file for detailed information")
    print("3. Update image references to point to correct locations")
    print("4. Copy missing images to the appropriate locations")

if __name__ == "__main__":
    main()
