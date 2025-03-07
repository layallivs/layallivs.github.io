import pandas as pd
from scripts.utils import read_template

def generate_journalism():
    """Generate the journalism page."""
    # Read the template
    template = read_template('journalism_template.html')
    
    # Read the journalism data
    df = pd.read_excel('data/journalism.xlsx')
    
    # Generate the content
    content = ''

    for _, row in df.iterrows():
        content += f'''
        <div class="m-3 rounded shadow-lg overflow-hidden flex flex-col h-full h-64 hover:shadow-2xl transition-shadow duration-300">
            <a href="{row['link']}" target="_blank" class="flex flex-col h-full">
                <div class="text-center m-1 px-3 py-2 text-gray-600">
                    {row['title']}
                </div>
                
                <div class="text-center font-bold text-xl m-1 px-2 py-2 mt-auto">
                    {row['publication']}
                </div>
            </a>
        </div>
        '''

    # Replace the content placeholder in the template
    final_html = template.replace('{{content}}', content)
    
    # Write the output file
    with open('docs/content/journalism.html', 'w', encoding='utf-8') as file:
        file.write(final_html) 

    print("Journalism page has been generated.")