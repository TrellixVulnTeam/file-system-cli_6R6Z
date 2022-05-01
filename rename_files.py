# Import libraries
import os

folder = os.path('/Users/nikpi/Desktop/Files')

# Accept a pattern and a replacement string
def rename_files(folder, pattern, replacement):
    for filename in os.listdir(folder):
        if pattern in filename:
            os.rename(os.path.join(folder, filename), os.path.join(folder, filename.replace(pattern, replacement)))

# Modify Date Order for Better Sorting

