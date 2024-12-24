#!/bin/bash

# Check if the file name is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <file_name>"
  exit 1
fi

# Assign the first argument to a variable
file_name=$1

# Check if the file exists and is readable
if [ ! -r "$file_name" ]; then
  echo "Error: File '$file_name' does not exist or is not readable."
  exit 1
fi

# Print the second line of the file
sed -n '2p' "$file_name"

