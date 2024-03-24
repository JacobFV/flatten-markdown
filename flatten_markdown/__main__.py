import argparse
from flatten_markdown.core import process_directory, process_file_flatten, process_file_unflatten

from flatten_markdown.utils import read_file, write_file



def main():
    parser = argparse.ArgumentParser(description="Flatten or unflatten Markdown files.")
    parser.add_argument('action', choices=['flatten', 'unflatten'], help="Action to perform")
    parser.add_argument('input', help="Input directory or file")
    parser.add_argument('output', help="Output file or directory")
    args = parser.parse_args()

    if args.action == 'flatten':
        flattened_content = process_directory(args.input, process_file_flatten, args.output)
        write_file(args.output, flattened_content)
        print(f"Flattened Markdown file created: {args.output}")
    elif args.action == 'unflatten':
        process_file_unflatten(args.input, args.output)
        print(f"Unflattened Markdown files created in: {args.output}")

if __name__ == "__main__":
    main()