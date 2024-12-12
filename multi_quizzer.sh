#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

dir=$1
output_dir="quiz_$dir"

if [ ! -d "$dir" ]; then
    echo "Directory $dir does not exist."
    exit 1
fi

mkdir -p "$output_dir"

for input in "$dir"/*; do
    if [ -f "$input" ]; then
        output="$output_dir/$(basename "$input").quizpack.json"
        ./quizzer.py "$input" | ./packer.py > "$output"
    fi
done