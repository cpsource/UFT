import csv
import sys
import os

def main():
    # Check if the required command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python3 forward-link.py <input_file> <csv_file>")
        sys.exit(1)

    # Get input and CSV file paths from command-line arguments
    input_file = sys.argv[1]
    csv_file = sys.argv[2]

    # Dictionary to hold the results
    result_dict = {}

    try:
        # Read the CSV file and create a dictionary mapping title to the Short URL
        csv_data = {}
        with open(csv_file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                if len(row) >= 3:
                    title = row[1].strip()
                    short_url = row[2].strip()
                    csv_data[title] = short_url

        # Read the input file and build the result dictionary in order of appearance
        ordered_items = []
        with open(input_file, 'r') as infile:
            for line in infile:
                item = line.strip()
                if item and item in csv_data:
                    result_dict[item] = f'[{item}]({csv_data[item]})'
                    ordered_items.append(item)

        # Display the result dictionary in the order of the input file
        print("Generated Dictionary (in order of appearance):")
        for item in ordered_items:
            print(f"{item}: {result_dict[item]}")

        # Create .tmp files for each item and rename files
        for i, item in enumerate(ordered_items):
            try:
                with open(item, 'r') as infile, open(f"{item}.tmp", 'w') as outfile:

                    # say who we are
                    outline = f'({result_dict[item]})\n---\n'
                    outfile.write(outline)
                    
                    # Copy the input file to the output file
                    for line in infile:
                        outfile.write(line)
                    
                    # Add the new content at the end of the output file
                    outfile.write('\n---\n\n')
                    if i < len(ordered_items) - 1:
                        next_item = ordered_items[i + 1]
                        outfile.write(f'{result_dict[next_item]}\n')
                    else:
                        outfile.write('[Home](https://t2m.io/VwvDcuw)\n')

                # Rename the original file to <item>.md-sav and rename the .tmp file to the original name
                os.rename(item, f"{item}-sav")
                os.rename(f"{item}.tmp", item)

            except FileNotFoundError:
                print(f"Error: The file '{item}' was not found.")
            except IOError as e:
                print(f"I/O error({e.errno}): {e.strerror}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")

if __name__ == "__main__":
    main()

