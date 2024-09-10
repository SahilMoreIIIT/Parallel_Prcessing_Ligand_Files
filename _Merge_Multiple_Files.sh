#!/bin/bash

# Define the directory containing the input files
input_dir="Result_Files"
output_file="94_Part_ZincDB_.sdf"

# Create or clear the output file
: > "$output_file"

# Loop through the sorted list of input files
for input_file in $(ls "$input_dir" | sort -V); do
    # Append the contents of the current input file to the output file
    cat "$input_dir/$input_file" >> "$output_file"
done

echo "All files have been merged into $output_file"