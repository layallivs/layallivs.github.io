import os
from scripts.generate_static_subpages import generate_static_subpages
from scripts.generate_journalism import generate_journalism
from scripts.generate_press import generate_press

def main():
    print("Starting website build process...")
    
    # Create necessary directories
    os.makedirs('docs', exist_ok=True)
    
    # Run the build steps
    generate_static_subpages()
    generate_journalism()
    generate_press()
    
    print("Build completed successfully!")
    print("The website is ready in the 'docs' directory.")

if __name__ == "__main__":
    main() 