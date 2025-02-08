
import os

def read_file(filename):
    """Read a file and return a set of non-empty, stripped lines."""
    with open(filename, encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())

def print_mismatches(header, mismatches):
    """Print header and mismatches in a formatted way."""
    count = len(mismatches)
    divider = "-" * 60
    print(divider)
    print(f"{header} ({count} mismatch{'es' if count != 1 else ''}):")
    print(divider)
    if mismatches:
        for line in mismatches:
            print(line)
    else:
        print("None")
    print("\n")

def main():
    #grammar_file = "grammar_titles_jap.txt"
    #markdown_file = "markdown_titles_jap.txt"

    grammar_file = "grammar_titles_kor.txt"
    markdown_file = "markdown_titles_kor.txt"



    # Check if files exist
    if not os.path.exists(grammar_file) or not os.path.exists(markdown_file):
        print("One or both input files not found.")
        return

    # Read both files into sets
    grammar_lines = read_file(grammar_file)
    markdown_lines = read_file(markdown_file)

    # Calculate mismatches (lines unique to each file)
    only_in_grammar = sorted(grammar_lines - markdown_lines)
    only_in_markdown = sorted(markdown_lines - grammar_lines)

    # Print mismatches for each file with formatted headers and counts.
    print_mismatches(f"Lines only in {grammar_file}", only_in_grammar)
    print_mismatches(f"Lines only in {markdown_file}", only_in_markdown)

if __name__ == "__main__":
    main()
