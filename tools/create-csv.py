import csv
import sys

def main():
    # Check if the required command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python3 mk-csv.py <input_file> <output_file>")
        sys.exit(1)

    # Get input and output file paths from command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # URL prefix to prepend to each input line
    url_prefix = "https://github.com/cpsource/UFT/blob/main/mdgithub/"

    try:
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

        print(f"CSV file '{output_file}' created successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")

if __name__ == "__main__":
    main()

