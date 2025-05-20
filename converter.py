import markdown
import sys
import os


def markdown_to_html(markdown_file, output_file=None):
    """
    Convert a Markdown file to HTML.

    Args:
        markdown_file (str): Path to the Markdown file
        output_file (str, optional): Path to save the HTML output.
                                    If None, will use the same name with .html extension.

    Returns:
        str: Path to the generated HTML file
    """
    # Determine output file name if not provided
    if output_file is None:
        base_name = os.path.splitext(markdown_file)[0]
        output_file = base_name + '.html'

    # Read the markdown file
    try:
        with open(markdown_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
    except Exception as e:
        print(f"Error reading markdown file: {e}")
        return None

    # Convert markdown to HTML
    html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite'])

    # Create a complete HTML document
    html_doc = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{os.path.basename(markdown_file)}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }}
        pre {{
            background-color: #f5f5f5;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }}
        code {{
            background-color: #f5f5f5;
            padding: 2px 4px;
            border-radius: 3px;
        }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""
    # add colorful code coloring for code blocks embedded in triple backticks
    html_doc = html_doc.replace('```', '<pre><code>```')
    # Write the HTML file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_doc)
        print(f"Successfully converted '{markdown_file}' to '{output_file}'")
        return output_file
    except Exception as e:
        print(f"Error writing HTML file: {e}")
        return None


if __name__ == "__main__":
    # Check if file path was provided as command line argument
    if len(sys.argv) < 2:
        print("Usage: python markdown_to_html.py <markdown_file> [output_file]")
        sys.exit(1)

    markdown_file = sys.argv[1]

    # Check if output file path was provided
    output_file = sys.argv[2] if len(sys.argv) >= 3 else None

    markdown_to_html(markdown_file, output_file)