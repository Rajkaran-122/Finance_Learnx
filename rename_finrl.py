import os
import shutil

# First, rename the main directory
try:
    os.rename('flx', 'flx')
    print('Renamed flx directory to flx')
except Exception as e:
    print('Rename failed:', e)

# Now traverse all files and replace 'flx' with 'flx'
def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace variations of flx
        new_content = content.replace('flx.', 'flx.')
        new_content = new_content.replace('from flx ', 'from flx ')
        new_content = new_content.replace('from flx\n', 'from flx\n')
        new_content = new_content.replace('import flx', 'import flx')
        new_content = new_content.replace('\"flx\"', '\"flx\"')
        new_content = new_content.replace('\'flx\'', '\'flx\'')
        new_content = new_content.replace('flx/', 'flx/')
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {filepath}')
    except Exception as e:
        pass

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'venv' in root or '__pycache__' in root or 'node_modules' in root.lower() or 'results' in root:
        continue
    for file in files:
        if file.endswith('.py') or file.endswith('.md') or file.endswith('.rst') or file.endswith('.ipynb') or file.endswith('.toml'):
            replace_in_file(os.path.join(root, file))

