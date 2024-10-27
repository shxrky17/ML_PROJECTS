import os
from pathlib import Path
import logging

# Configure logging to display info level messages
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# List of files to create
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trias.ipynb"
]

# Loop through each file path in the list
for filepath in list_of_files:
    file_path = Path(filepath)  # Create a Path object
    filedir, filename = os.path.split(filepath)  # Split the path into directory and filename

    # If there is a directory component, create it
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create directories if they don't exist
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Check if the file does not exist or is empty
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:  # Create an empty file
            pass  # Nothing to write in the file
        logging.info(f"Creating empty file: {filepath}")  # Log the file creation
    else:
        logging.info(f"{filename} already exists")  # Log that the file exists
