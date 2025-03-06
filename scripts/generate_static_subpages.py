import os
import shutil
from scripts.utils import read_template

def generate_static_subpages():
    """Create the distribution folder with all necessary files."""
    # Create docs directory
    os.makedirs('docs', exist_ok=True)

    # List of HTML files to process
    html_files = [
        ('src/templates/index.html', 'index.html'),
        ('src/templates/about.html', 'about.html'),
        ('src/templates/books.html', 'books.html'),
        ('src/templates/contact.html', 'contact.html'),
        ('src/templates/impressum.html', 'impressum.html'),
    ]
    
    # Process HTML files
    for src, dest in html_files:
        if os.path.exists(src):
            # Read the content file
            full_html = read_template(dest)

            # Write to docs
            with open(os.path.join('docs', dest), 'w', encoding='utf-8') as f:
                f.write(full_html)
    
    # List of other files to copy
    files_to_copy = [
        ('src/styles/tailwind.css', 'tailwind.css'),
        ('src/styles/styles.css', 'styles.css'),
        ('src/styles/tailwind.config.js', 'tailwind.config.js'),
        ('CNAME', 'CNAME'),
        ('favicon.ico', 'favicon.ico')
    ]
    
    # List of directories to copy
    dirs_to_copy = [
        ('src/assets/images', 'images'),
    ]
    
    # Copy files
    for src, dest in files_to_copy:
        if os.path.exists(src):
            shutil.copy2(src, os.path.join('docs', dest))
    
    # Copy directories
    for src, dest in dirs_to_copy:
        if os.path.exists(src):
            shutil.copytree(src, os.path.join('docs', dest), dirs_exist_ok=True)
    
    print("Static files have been copied to the docs folder.")
