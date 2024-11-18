import os

def replace_spaces_with_underscore(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            new_file = file.replace(" ", "_")
            if new_file != file:
                os.rename(os.path.join(root, file), os.path.join(root, new_file))
        for dir in dirs:
            new_dir = dir.replace(" ", "_")
            if new_dir != dir:
                os.rename(os.path.join(root, dir), os.path.join(root, new_dir))

# Replace spaces with underscore in the current working directory
replace_spaces_with_underscore(os.getcwd())