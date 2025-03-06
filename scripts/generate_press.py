import pandas as pd
from scripts.utils import read_template

def generate_press():
    """Generate the press page."""
    # Read the template
    template = read_template('press_template.html')
    
    # Read the press data
    df = pd.read_excel('data/press.xlsx')
    
    # Generate the content
    content = ''
    
    for _, row in df.iterrows():
        content += f'''
        <div class=" m-3 rounded shadow-lg overflow-hidden flex flex-col h-full">
            <a href="{row['Link']}" target="_blank" class="flex flex-col h-full">
                <div class="text-center font-bold text-xl m-1 px-2 py-2">
                    {row['Outlet']}
                </div>
                <div class="text-center px-2 text-gray-600 flex-grow flex items-center justify-center">
                    {row['Title']}
                </div>
                <div class="text-center m-1 px-2 py-1 text-gray-400">
                    {row['Date'].strftime('%d %B %Y')}
                </div>
            </a>
        </div>
        '''
    
    # Replace the content placeholder in the template
    final_html = template.replace('{{content}}', content)
    
    # Write the output file
    with open('docs/press.html', 'w', encoding='utf-8') as file:
        file.write(final_html) 