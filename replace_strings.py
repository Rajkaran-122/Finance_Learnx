import os

replacements = {
    'DigitalMetro': 'DigitalMetro',
    'DigitalMetro': 'DigitalMetro',
    'DigitalMetro': 'DigitalMetro',
    'DigitalMetro': 'DigitalMetro',
    'DigitalMetro': 'DigitalMetro',
    'DigitalMetro/Finance_pro': 'DigitalMetro/Finance_pro',
    'finance-pro.readthedocs.io': 'finance-pro.readthedocs.io'
}

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        for k, v in replacements.items():
            new_content = new_content.replace(k, v)
            
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {filepath}')
    except Exception as e:
        pass

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'venv' in root or '__pycache__' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.py') or file.endswith('.md') or file.endswith('.rst') or file.endswith('.ipynb') or file.endswith('.toml'):
            replace_in_file(os.path.join(root, file))
