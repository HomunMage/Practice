import os

def replace_url_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace the specified URL pattern
    new_content = content.replace('posetmage.com/SettingBook/', 'posetmage.com/Novel/')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                replace_url_in_file(os.path.join(root, file))

# Replace with the directory you want to process
process_directory('.')
