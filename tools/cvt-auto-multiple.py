import os
import sys
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

    # Add the specified lines to the top of the output
    header = "[Home](https://t2m.io/VwvDcuw)\n---\n\n"
    content = header + content

    # Write the converted content to the output file
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Converted LaTeX to GitHub format in {output_md}")

def main():

    # Check for command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <sub_directory>")
        sys.exit(1)

    # Get the sub-directory name from the command-line argument
    sub_directory = sys.argv[1]
    
    # Define directories
    src_dir    = os.path.join("src"     , sub_directory)
    output_dir = os.path.join("mdgithub", sub_directory)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # GitHub repository base URL for link generation
    github_base_url = f"https://github.com/cpsource/UFT/blob/main/mdgithub/{sub_directory}"

    print(f"Source Directory: {src_dir}")
    print(f"Output Directory: {output_dir}")
    print(f"GitHub Base URL: {github_base_url}")

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
                # Update the file and print the GitHub link
                os.replace(temp_output, output_md)
                print(f"Updated file: {output_md}")
                print(f"{github_base_url}/{base_name}")
        else:
            # Convert and create the output file if it doesn’t exist
            print(f"Creating new output file: {output_md}")
            convert_to_github_latex_format(input_md, output_md)
            print(f"{github_base_url}/{base_name}")

if __name__ == "__main__":
    main()

