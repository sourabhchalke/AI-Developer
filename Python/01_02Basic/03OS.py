import os

# Specify the directory path. Use '.' for the current directory.
directory_path = '../Basic'

# Get the list of all entries
contents = os.listdir(directory_path)

# Print the contents
print(f"Contents of '{directory_path}':")
for item in contents:
    print(item)