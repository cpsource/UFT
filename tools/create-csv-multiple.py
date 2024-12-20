import os
import csv
import sys

def main():
    # Check if the required command-line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python3 create-csv.py <directory>")
        sys.exit(1)

    # Get the target directory from command-line arguments
    target_directory = sys.argv[1]

    # Save the current directory
    original_directory = os.getcwd()

    try:
        # Change to the target directory
        os.chdir(target_directory)

        # File names within the target directory
        input_file = "filelist.txt"
        output_file = "filelist.csv"

        # Ensure input file exists
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' not found in {target_directory}.")
            sys.exit(1)

        # Update the URL prefix to include the sub-directory
        url_prefix = f"https://github.com/cpsource/UFT/blob/main/mdgithub/{os.path.basename(target_directory)}/"

        # Open the input file for reading
        with open(input_file, 'r') as infile:
            # Read all lines from the input file and strip whitespace
            lines = [line.strip() for line in infile if line.strip()]

        # Open the output CSV file for writing
        with open(output_file, 'w', newline='') as outfile:
            csv_writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
            # Write the header row
            csv_writer.writerow(["URL", "title"])
            
            # Process each line and write to the CSV file
            for line in lines:
                url = f'{url_prefix}{line}'
                title = line
                csv_writer.writerow([url, title])

        print(f"CSV file '{output_file}' created successfully in {target_directory}.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")
    finally:
        # Return to the original directory
        os.chdir(original_directory)

if __name__ == "__main__":
    main()

