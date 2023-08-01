#!/bin/bash

# Define the directory path here
DIR_PATH="/path/to/directory"

cd $DIR_PATH

# Get unique prefixes
prefixes=$(ls | grep -o '.*-part' | sed 's/-part.*//' | sort | uniq)

for prefix in $prefixes
do
  # Find all files with the current prefix, tar and gzip them
  tar -czf "${prefix}.tar.gz" "${prefix}-part"*
done
