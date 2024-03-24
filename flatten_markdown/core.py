
import os
from pathlib import Path
import argparse

from flatten_markdown.utils import read_file, write_file


def process_directory(directory, process_file_func, output_file, base_level=1):
    output_content = ""
    for item in os.listdir(directory):
        item_path = Path(directory) / item
        if item_path.is_file() and item_path.suffix == '.md':
            content = process_file_func(item_path, base_level)
            output_content += content
        elif item_path.is_dir():
            heading_level = '#' * base_level
            output_content += f"{heading_level} {item}\n\n"
            output_content += process_directory(item_path, process_file_func, output_file, base_level + 1)
    return output_content

def process_file_flatten(file_path, base_level):
    content = read_file(file_path)
    heading_level = '#' * base_level
    return f"{heading_level} {file_path.stem}\n\n{content}\n\n"

def process_file_unflatten(file_path, output_directory):
    content = read_file(file_path)
    lines = content.split('\n')
    current_directory = output_directory
    current_file = None
    current_file_content = []

    for line in lines:
        if line.startswith('#'):
            heading_level = line.count('#')
            heading_text = line.lstrip('#').strip()
            if heading_level == 1:
                if current_file:
                    write_file(current_file, '\n'.join(current_file_content))
                current_file = current_directory / f"{heading_text}.md"
                current_file_content = []
            else:
                if current_file:
                    write_file(current_file, '\n'.join(current_file_content))
                    current_file = None
                    current_file_content = []
                current_directory = current_directory / heading_text
        else:
            if current_file is not None:
                current_file_content.append(line)

    if current_file:
        write_file(current_file, '\n'.join(current_file_content))
    content = read_file(file_path)
    lines = content.split('\n')
    current_directory = output_directory
    current_file = None
    current_file_content = []

    for line in lines:
        if line.startswith('#'):
            heading_level = line.count('#')
            heading_text = line.lstrip('#').strip()
            if heading_level == 1:
                if current_file:
                    write_file(current_file, '\n'.join(current_file_content))
                current_file = current_directory / f"{heading_text}.md"
                current_file_content = []
            else:
                if current_file:
                    write_file(current_file, '\n'.join(current_file_content))
                current_directory = current_directory / heading_text
                current_file = None
                current_file_content = []
        else:
            current_file_content.append(line)

    if current_file:
        write_file(current_file, '\n'.join(current_file_content))