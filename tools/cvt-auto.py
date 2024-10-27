import os
import re
import glob
import filecmp

def convert_to_github_latex_format(input_md, output_md):
    with open(input_md, 'r', encoding='utf-8') as f:
        content = f.read()

    # Convert inline math from \( ... \) to $...$ without extra spaces
    content = re.sub(r'\\\(\s*(.+?)\s*\\\)', r'$\1$', content)

    # Convert block math from \[ ... \] to $$...$$ without extra spaces
    content = re.sub(r'\\\[\s*(.+?)\s*\\\]', r'$$\1$$', content)

    # Write the converted content to the output file
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Converted LaTeX to GitHub format in {output_md}")

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
        output_md = os.path.join(output_dir, base_name)

        # Check if the output file exists
        if os.path.exists(output_md):
            # Convert to GitHub format and write to a temporary file for comparison
            temp_output = os.path.join(output_dir, f"temp_{base_name}")
            convert_to_github_latex_format(input_md, temp_output)
            if filecmp.cmp(temp_output, output_md, shallow=False):
                print(f"No update needed for {output_md}; it is up to date.")
                os.remove(temp_output)
            else:
                print(f"Updating {output_md} with new content.")
                os.replace(temp_output, output_md)
        else:
            # Convert and create the output file if it doesn’t exist
            print(f"Creating new output file: {output_md}")
            convert_to_github_latex_format(input_md, output_md)

if __name__ == "__main__":
    main()

