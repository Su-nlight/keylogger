#!/bin/bash

# Define variables
repo_owner="owner"          # Replace with the repository owner
repo_name="repo"            # Replace with the repository name
release_tag="v1.0.0"        # Replace with the desired release tag
asset_name="example"        # Replace with the asset file name you want to download
download_url="https://github.com/$repo_owner/$repo_name/releases/download/$release_tag/$asset_name"

# Get the current directory
current_dir=$(pwd)

# Define paths
temp_file="$current_dir/$asset_name"

# Download the file
echo "Downloading $download_url to $temp_file..."
wget -O "$temp_file" "$download_url"

# Make the file executable (if it's not already)
chmod +x "$temp_file"

# Execute the file in the background
echo "Executing $temp_file..."
"$temp_file" &>/dev/null &
