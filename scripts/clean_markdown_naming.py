
import os

# Define the target directory
TARGET_DIR = "/home/coil/Desktop/hanabira.org-japanese-content/markdown_grammar_korean"

def main():
    # List all files in the target directory
    for filename in os.listdir(TARGET_DIR):
        # Process only Markdown files
        if filename.endswith(".md") and "'" in filename:
            # Create the new filename by replacing "'" with "_"
            new_filename = filename.replace("'", "_")
            old_path = os.path.join(TARGET_DIR, filename)
            new_path = os.path.join(TARGET_DIR, new_filename)
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_filename}")
            except Exception as e:
                print(f"Error renaming {filename}: {e}")

if __name__ == "__main__":
    main()
