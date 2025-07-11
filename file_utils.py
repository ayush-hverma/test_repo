import os

def read_file(file_path):
    """Read file content."""
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as f:
        return f.read()

def write_file(file_path, content):
    """Write content to file."""
    with open(file_path, 'w') as f:
        f.write(content)

def append_file(file_path, content):
    """Append content to file."""
    with open(file_path, 'a') as f:
        f.write(content + "\n")

def list_files(directory):
    """List all files in a directory."""
    return os.listdir(directory)
