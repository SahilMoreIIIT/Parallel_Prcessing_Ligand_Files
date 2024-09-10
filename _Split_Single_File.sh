#!/bin/bash

# Make Directory
mkdir -p "Input_Files"

input_file="94_Part_ZincDB_.csv"  # Path to your input file
output_prefix="file"  # Prefix for output files

# Get total number of cores
# Number of parts to create
# Number of lines per output file
lines_per_file=$(nproc)
file_counter=1          # Counter for output files

# Create a directory to store the output files
mkdir -p "Input_Files"

# Loop through the input file
while IFS= read -r line; do
    # Write the current line to the output file
    echo "$line" >> "Input_Files/${output_prefix}_${file_counter}.smi"

    # Increment the counter
    ((file_counter++))

    # Reset the counter if it exceeds the specified lines per file
    if [ "$file_counter" -gt "$lines_per_file" ]; then
        file_counter=1
    fi
done < "$input_file"
