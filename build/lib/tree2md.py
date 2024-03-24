#!/usr/bin/env python3
import os
import argparse

def convert_tree_to_markdown(root_dir, output_file, heading_offset=0):
    with open(output_file, 'w') as f:
        _convert_tree_to_markdown_recursive(root_dir, f, heading_offset)

def _convert_tree_to_markdown_recursive(current_dir, output_file, heading_offset):
    files = os.listdir(current_dir)
    files.sort()

    for file in files:
        file_path = os.path.join(current_dir, file)

        if os.path.isdir(file_path):
            output_file.write(f"{'#' * (heading_offset + 1)} {file}\n\n")
            _convert_tree_to_markdown_recursive(file_path, output_file, heading_offset + 1)
        else:
            if file.lower() in ['index.md', 'readme.md']:
                with open(file_path, 'r') as f:
                    content = f.read()
                output_file.write(content + '\n\n')
            else:
                output_file.write(f"{'#' * (heading_offset + 2)} {file}\n\n")
                with open(file_path, 'r') as f:
                    content = f.read()
                output_file.write(content + '\n\n')

def main():
    parser = argparse.ArgumentParser(prog="tree2md", description='Convert a nested markdown documentation tree to a single markdown document.')
    parser.add_argument('root_dir', help='Path to the root directory of the documentation tree.')
    parser.add_argument('output_file', help='Path to the output markdown file.')
    args = parser.parse_args()

    convert_tree_to_markdown(args.root_dir, args.output_file)
    print(f"Conversion complete. Output file: {args.output_file}")

if __name__ == '__main__':
    main()