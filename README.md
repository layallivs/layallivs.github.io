# Layal Liverpool Personal Website

A personal website built with HTML, Tailwind CSS, and Python for content generation.

## Structure
- `docs/` - **Generated website (output directory) !!!DO NOT MODIFY CONTENT HERE!!!**
- `data/` - Excel spreadsheets for content
  - `images` - folder with images used on the website
  - `journalism.xlsx` - Journalism articles data
  - `press.xlsx` - Press mentions data
- `src/` - Source files directory
  - `content/` - HTML subpages
    - `about.html` - About page template
    - `books.html` - Book page template
    - `contact.html` - Contact page template
    - `impressum.html` - Impressum template
    - `index.html` - Home page template
  - `templates/` - HTML templates
    - `index.html` - Base template with common structure
    - `journalism_template.html` - Template for journalism page
    - `press_template.html` - Template for press page
  - `styles/` - CSS and Tailwind configuration
    - `tailwind.css` - Tailwind CSS styles
    - `styles.css` - Custom CSS styles
    - `tailwind.config.js` - Tailwind configuration
- `scripts/` - Python scripts for site generation
  - `generate_static_subpages.py` - Generates static HTML pages
  - `generate_journalism.py` - Generates journalism page from data
  - `generate_press.py` - Generates press page from data
  - `utils.py` - Utility functions for page generation
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
python3 build.py
```

2. The generated website will be created in the `docs/` directory.

3. To preview the website locally:
```bash
cd docs
python3 -m http.server 8000
```

## Development

The website uses:
- HTML5 for structure
- Tailwind CSS for styling
- Python for content generation
- No JavaScript frameworks

## Deployment

The website can be deployed to any static hosting service like GitHub Pages, Netlify, or Vercel.
The included CNAME file supports custom domain configuration. 