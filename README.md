# Layal Liverpool Personal Website

A personal website built with HTML, Tailwind CSS, and Python for content generation.

## Structure

- `src/` - Source files directory
  - `templates/` - HTML templates
    - `base_template.html` - Base template with common structure
    - `index.html` - Home page template
    - `about.html` - About page template
    - `book.html` - Book page template
    - `contact.html` - Contact page template
    - `journalism_template.html` - Template for journalism page
    - `press_template.html` - Template for press page
  - `styles/` - CSS and Tailwind configuration
    - `tailwind.css` - Tailwind CSS styles
    - `styles.css` - Custom CSS styles
    - `tailwind.config.js` - Tailwind configuration
  - `assets/` - Static assets like images
- `scripts/` - Python scripts for site generation
  - `generate_static_subpages.py` - Generates static HTML pages
  - `generate_journalism.py` - Generates journalism page from data
  - `generate_press.py` - Generates press page from data
  - `utils.py` - Utility functions for page generation
- `data/` - Excel spreadsheets for content
  - `journalism.xlsx` - Journalism articles data
  - `press.xlsx` - Press mentions data
- `docs/` - Generated website (output directory)
- `build.py` - Main build script

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure Excel spreadsheets are in the `data/` directory:
   - `journalism.xlsx` with columns: title, publication, date, description, link
   - `press.xlsx` with columns: title, source, date, description, link

## Usage

1. To generate the website:
```bash
python build.py
```

2. The generated website will be created in the `docs/` directory.

## Development

The website uses:
- HTML5 for structure
- Tailwind CSS for styling
- Python for content generation
- No JavaScript frameworks

## Deployment

The website can be deployed to any static hosting service like GitHub Pages, Netlify, or Vercel.
The included CNAME file supports custom domain configuration. 