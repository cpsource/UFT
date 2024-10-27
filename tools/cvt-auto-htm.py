import os
import glob
import markdown
import filecmp

def convert_md_to_html(input_md, output_html):
    # Load the Markdown content
    with open(input_md, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)

    # Add MathJax script for LaTeX rendering
    html_with_mathjax = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Markdown with MathJax</title>
        <script type="text/javascript">
            MathJax = {{
                tex: {{
                    inlineMath: [['\\(', '\\)']],
                    displayMath: [['\\[', '\\]']]
                }},
                svg: {{
                    fontCache: 'global'
                }}
            }};
        </script>
        <script type="text/javascript" async
                src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.0.1/es5/tex-mml-chtml.js">
        </script>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Write the output HTML content
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_with_mathjax)
    print(f"Converted {input_md} to {output_html} with MathJax support.")

def main():
    # Define directories
    src_dir = "src"
    output_dir = "mdgithub"

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Find all .md files in the src directory
    for input_md in glob.glob(os.path.join(src_dir, "*.md")):
        # Define the corresponding output file path in the mdgithub directory
        base_name = os.path.basename(input_md)
        output_html = os.path.join(output_dir, base_name.replace(".md", ".htm"))

        # Check if the output file exists
        if os.path.exists(output_html):
            # Compare the existing output file with the newly generated content
            temp_output = os.path.join(output_dir, f"temp_{base_name.replace('.md', '.htm')}")
            convert_md_to_html(input_md, temp_output)
            if filecmp.cmp(temp_output, output_html, shallow=False):
                print(f"No update needed for {output_html}; it is up to date.")
                os.remove(temp_output)
            else:
                print(f"Updating {output_html} with new content.")
                os.replace(temp_output, output_html)
        else:
            # Convert and create the output file if it doesn’t exist
            print(f"Creating new output file: {output_html}")
            convert_md_to_html(input_md, output_html)

if __name__ == "__main__":
    main()

