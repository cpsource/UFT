import csv
import sys

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

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")

if __name__ == "__main__":
    main()

