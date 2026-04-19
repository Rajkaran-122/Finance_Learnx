import os

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace FLX with FLX
        new_content = content.replace('FLX', 'FLX')
        new_content = new_content.replace('flx', 'flx')
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
    except Exception as e:
        pass

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'venv' in root or '__pycache__' in root or 'node_modules' in root.lower() or 'results' in root:
        continue
    for file in files:
        if file.endswith('.py') or file.endswith('.md') or file.endswith('.rst') or file.endswith('.ipynb') or file.endswith('.toml'):
            replace_in_file(os.path.join(root, file))

# Rename docs directory components if needed
try:
    os.rename('docs/source/flx_meta', 'docs/source/flx_meta')
except:
    pass
