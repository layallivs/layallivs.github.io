import os
import shutil
from scripts.utils import read_template

def generate_static_subpages():
    """Create the distribution folder with all necessary files."""
    # Create docs directory
    os.makedirs('docs', exist_ok=True)
    os.makedirs('docs/content', exist_ok=True)
    
    # List of other files to copy
    files_to_copy = [
        ('src/templates/index.html', 'index.html'),
        ('src/content/index.html', 'content/index.html'),
        ('src/content/about.html', 'content/about.html'),
        ('src/content/books.html', 'content/books.html'),
        ('src/content/contact.html', 'content/contact.html'),
        ('src/content/impressum.html', 'content/impressum.html'),
        ('src/styles/tailwind.css', 'tailwind.css'),
        ('src/styles/styles.css', 'styles.css'),
        ('src/styles/tailwind.config.js', 'tailwind.config.js'),
        ('CNAME', 'CNAME'),
        ('favicon.ico', 'favicon.ico')
    ]
    
    # List of directories to copy
    dirs_to_copy = [
        ('data/images', 'images'),
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
