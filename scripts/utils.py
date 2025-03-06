import os

def read_file(file_path):
    """Read a file and return its contents."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def read_template(template_path):
    """Read a template file and return its contents."""
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to the project root
    project_root = os.path.dirname(script_dir)
    
    # Read base template
    base_template = read_file(os.path.join(project_root, 'src', 'templates', 'base_template.html'))
    
    # Read the specific template
    template = read_file(os.path.join(project_root, 'src', 'templates', template_path))
    
    # Combine templates
    return base_template.replace('{{content}}', template) 