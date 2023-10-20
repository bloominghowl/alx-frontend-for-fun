#!/usr/bin/python3
"""
Converts a Markdown file to HTML.
"""

import sys
import markdown

# Check if the correct number of arguments is provided
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

# Get file names from command line arguments
md_file = sys.argv[1]
html_file = sys.argv[2]

try:
    # Read the content of the Markdown file
    with open(md_file, 'r') as f:
        markdown_content = f.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content)

    # Write HTML content to the output file
    with open(html_file, 'w') as f:
        f.write(html_content)

except FileNotFoundError:
    print(f"Missing {md_file}", file=sys.stderr)
    sys.exit(1)

sys.exit(0)
