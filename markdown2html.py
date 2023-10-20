#!/usr/bin/python3
"""
Converts a Markdown file to HTML.
"""

import sys
import markdown

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

md_file = sys.argv[1]
html_file = sys.argv[2]

try:
    with open(md_file, 'r') as f:
        markdown_content = f.read()

    html_content = markdown.markdown(markdown_content)

    with open(html_file, 'w') as f:
        f.write(html_content)

except FileNotFoundError:
    print(f"Missing {md_file}", file=sys.stderr)
    sys.exit(1)

sys.exit(0)
