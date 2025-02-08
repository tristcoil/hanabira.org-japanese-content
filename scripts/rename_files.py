#!/usr/bin/env python3
import os

# Define the target directory where files will be renamed.
#TARGET_DIR = "/home/coil/Desktop/hanabira.org-japanese-content/markdown_grammar_japanese"
TARGET_DIR = "/home/coil/Desktop/hanabira.org-japanese-content/markdown_grammar_korean"


# The renaming matrix file.
#MATRIX_FILE = "renaming_matrix_jap.txt"
MATRIX_FILE = "renaming_matrix_kor.txt"

def main():
    # Ensure the matrix file exists.
    if not os.path.exists(MATRIX_FILE):
        print(f"Matrix file '{MATRIX_FILE}' not found.")
        return

    with open(MATRIX_FILE, encoding="utf-8") as f:
        lines = f.readlines()

    # Process each line in the matrix file.
    for line in lines:
        line = line.strip()
        if not line or "|" not in line:
            continue  # Skip empty lines or lines without delimiter.
        
        # Split the line into the old (current) filename and new filename.
        old_name, new_name = (part.strip() for part in line.split("|", 1))
        
        # Build the full file paths.
        old_path = os.path.join(TARGET_DIR, old_name)
        new_path = os.path.join(TARGET_DIR, new_name)
        
        # Check if the old file exists before attempting to rename.
        if not os.path.exists(old_path):
            print(f"File not found: {old_path}")
            continue
        
        # Rename the file.
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: '{old_name}' -> '{new_name}'")
        except Exception as e:
            print(f"Error renaming '{old_name}' to '{new_name}': {e}")

if __name__ == "__main__":
    main()
