#!/bin/bash

# Check if the correct number of arguments is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <subdirectory>"
    exit 1
fi

# Assign the argument to a variable
subdirectory=$1

# Check if the directory exists
if [ ! -d "$subdirectory" ]; then
    echo "Error: Directory '$subdirectory' does not exist."
    exit 1
fi

# Navigate to the specified subdirectory
pushd "$subdirectory" > /dev/null || exit

# Find the response file with the pattern "filelist-response-xxxxx.csv"
response_file=$(ls -1 filelist-response-* 2>/dev/null | head -n 1)

# Check if the response file was found
if [ -z "$response_file" ]; then
    echo "Error: No file matching 'filelist-response-*.csv' found in $subdirectory."
    popd > /dev/null
    exit 1
fi

# Run the Python script with filelist.txt and the extracted argument
python3 ../../tools/forward-link.py filelist.txt "$response_file"

# Remove files ending with '-sav'
rm -f *-sav

# Return to the original directory
popd > /dev/null

echo "Completed operations in subdirectory: $subdirectory"

