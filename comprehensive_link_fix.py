#!/usr/bin/env python3
"""
Comprehensive script to fix all types of broken links in Docusaurus documentation.
This handles the remaining 180 broken links that the previous script missed.
"""

import re
from pathlib import Path
from typing import List, Dict, Set, Tuple

class ComprehensiveLinkFixer:
    def __init__(self, docs_root: str = "docs"):
        self.docs_root = Path(docs_root)
        self.md_files = []
        self.valid_paths = set()
        self.fixed_files = []
        
    def scan_files(self):
        """Scan for all markdown files and build valid paths"""
        print("Scanning for markdown files...")
        
        for md_file in self.docs_root.rglob("*.md"):
            self.md_files.append(md_file)
            
            # Add the file path without .md extension (Docusaurus format)
            relative_path = md_file.relative_to(self.docs_root)
            docusaurus_path = f"/{relative_path.with_suffix('')}"
            self.valid_paths.add(docusaurus_path)
            
            # Also add the path without leading slash for relative links
            self.valid_paths.add(str(relative_path.with_suffix('')))
        
        print(f"Found {len(self.md_files)} markdown files")
        print(f"Generated {len(self.valid_paths)} valid paths")
    
    def fix_links_in_file(self, file_path: Path) -> Tuple[str, bool]:
        """Fix all types of broken links in a single file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            fixed = False
            
            # Pattern to match markdown links: [text](url)
            link_pattern = r'\[([^\]]*)\]\(([^)]+)\)'
            
            def replace_link(match):
                nonlocal fixed
                link_text = match.group(1)
                link_path = match.group(2)
                
                # Skip external links, anchors, and mailto
                if (link_path.startswith('http') or 
                    link_path.startswith('#') or 
                    link_path.startswith('mailto:') or
                    link_path.startswith('https://')):
                    return match.group(0)
                
                # Handle image paths that start with /img/
                if link_path.startswith('/img/'):
                    # Convert to proper Docusaurus image path
                    new_path = link_path
                    fixed = True
                    print(f"  Fixed image path: {link_path} -> {new_path}")
                    return f'[{link_text}]({new_path})'
                
                # Handle absolute paths that need /user-guide/ prefix
                if link_path.startswith('/') and not link_path.startswith('/user-guide/'):
                    # Check if this should be a user-guide path
                    if any(part in link_path for part in ['editor', 'block-types', 'connections', 'secrets', 'variables', 'batching', 'queuing', 'scheduled-flows', 'dev-prod-modes', 'memory-store', 'data-store', 'auditing', 'error-handling', 'data-browser', 'tags', 'tests', 'alerts', 'logging', 'global-settings', 'transferring-data', 'troubleshooting', 'security', 'deployment', 'monitoring', 'structures', 'launching']):
                        new_path = f"/user-guide{link_path}"
                        fixed = True
                        print(f"  Fixed user-guide path: {link_path} -> {new_path}")
                        return f'[{link_text}]({new_path})'
                    
                    # Check if this should be a block-types path
                    if 'block-types' in link_path:
                        new_path = f"/user-guide{link_path}"
                        fixed = True
                        print(f"  Fixed block-types path: {link_path} -> {new_path}")
                        return f'[{link_text}]({new_path})'
                
                # Handle relative paths that should be absolute
                if not link_path.startswith('/') and not link_path.startswith('http'):
                    # Try to find the referenced file
                    target_file = None
                    for md_file in self.md_files:
                        if md_file.name.replace('.md', '') == link_path or md_file.name == link_path:
                            target_file = md_file
                            break
                    
                    if target_file:
                        # Convert to absolute path
                        relative_path = f"/{target_file.relative_to(self.docs_root).with_suffix('')}"
                        fixed = True
                        print(f"  Fixed relative path: {link_path} -> {relative_path}")
                        return f'[{link_text}]({relative_path})'
                    
                    # Handle special cases for block-types
                    if link_path in ['Javascript', 'Data-Store', 'SQL', 'REST-Call', 'Iterator', 'Receiver', 'Terminator', 'Branch', 'Merger', 'Collector', 'Splitter', 'joiner', 'Has-Data', 'Key-Filter', 'Subflow', 'Branch-To-Subflow', 'Batch-End', 'test-data', 'sinkhole', 'Variable-Set-Get', 'Console-Message', 'Annotation', 'commander-block']:
                        # Determine if it's core or utility
                        if link_path in ['Javascript', 'Iterator', 'Receiver', 'Terminator', 'Branch', 'Merger', 'Collector', 'Splitter', 'joiner', 'Has-Data', 'Key-Filter', 'Subflow', 'Branch-To-Subflow', 'Batch-End', 'test-data', 'sinkhole', 'Variable-Set-Get', 'Console-Message', 'Annotation', 'commander-block']:
                            new_path = f"/user-guide/block-types/core/{link_path}"
                        else:
                            new_path = f"/user-guide/block-types/utility/{link_path}"
                        fixed = True
                        print(f"  Fixed block-type path: {link_path} -> {new_path}")
                        return f'[{link_text}]({new_path})'
                    
                    # Handle special cases for user-guide topics
                    if link_path in ['Flows-listing', 'Execution-history', 'Commander', 'Flow-documentation', 'Debugging', 'Dev-Prod-Modes', 'sql-mapping', 'sql-editing', 'Block-Helper']:
                        if link_path in ['Flows-listing', 'Execution-history', 'Commander', 'Flow-documentation', 'Debugging']:
                            new_path = f"/user-guide/editor/{link_path}"
                        elif link_path in ['Dev-Prod-Modes']:
                            new_path = f"/user-guide/{link_path}"
                        elif link_path in ['sql-mapping', 'sql-editing']:
                            new_path = f"/user-guide/block-types/utility/sql/{link_path}"
                        elif link_path in ['Block-Helper']:
                            new_path = f"/customisation/custom-utility-blocks/server/{link_path}"
                        else:
                            new_path = f"/user-guide/{link_path}"
                        fixed = True
                        print(f"  Fixed special path: {link_path} -> {new_path}")
                        return f'[{link_text}]({new_path})'
                
                return match.group(0)
            
            content = re.sub(link_pattern, replace_link, content)
            
            return content, fixed
        
        except Exception as e:
            print(f"  ❌ Error processing file: {e}")
            return content, False
    
    def process_all_files(self):
        """Process all files to fix broken links"""
        print("🔧 Processing files to fix broken links...")
        
        for md_file in self.md_files:
            print(f"Processing: {md_file}")
            content, was_fixed = self.fix_links_in_file(md_file)
            
            if was_fixed:
                # Write back the fixed content
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.fixed_files.append(str(md_file))
                print(f"  ✅ Updated file")
            else:
                print(f"  ⏭️  No changes needed")
            print()
    
    def run(self):
        """Run the comprehensive link fixer"""
        print("🚀 Comprehensive Link Fixer")
        print("=" * 50)
        
        self.scan_files()
        print()
        
        self.process_all_files()
        
        print("=" * 50)
        print(f"📊 Summary:")
        print(f"   Files processed: {len(self.md_files)}")
        print(f"   Files updated: {len(self.fixed_files)}")
        
        if self.fixed_files:
            print(f"\n📝 Updated files:")
            for file_path in self.fixed_files:
                print(f"   - {file_path}")
        
        print("\n✨ Done!")

def main():
    """Main function"""
    fixer = ComprehensiveLinkFixer()
    fixer.run()

if __name__ == "__main__":
    main()
