import os

def remove_layout_default(root_dir='.'):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()

                    with open(file_path, 'w', encoding='utf-8') as f:
                        for line in lines:
                            if "layout: default" not in line:
                                f.write(line)
                except UnicodeDecodeError:
                    print(f"Unicode decode error encountered in file {file_path}")

remove_layout_default()
