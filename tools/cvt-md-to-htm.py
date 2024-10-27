import markdown
import sys

def convert_md_to_html(input_md, output_html):
    # Load the Markdown content
    with open(input_md, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)

    # Add MathJax script with custom configuration
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

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input.md> <output.htm>")
    else:
        input_md = sys.argv[1]
        output_html = sys.argv[2]
        convert_md_to_html(input_md, output_html)

