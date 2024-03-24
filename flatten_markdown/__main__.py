import os
from pathlib import Path
import typer

app = typer.Typer()

def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_markdown_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def flatten_markdown_files(directory, output_file, base_level=1):
    output_content = ""

    for item in os.listdir(directory):
        item_path = Path(directory) / item

        if item_path.is_file() and item_path.suffix == '.md':
            content = read_markdown_file(item_path)
            heading_level = '#' * base_level
            output_content += f"{heading_level} {item_path.stem}\n\n{content}\n\n"

        elif item_path.is_dir():
            heading_level = '#' * base_level
            output_content += f"{heading_level} {item}\n\n"
            output_content += flatten_markdown_files(item_path, output_file, base_level + 1)

    return output_content

@app.command()
def main(directory: str = typer.Argument('.', help="Directory to flatten")):
    output_file = 'flattened_markdown.md'
    flattened_content = flatten_markdown_files(directory, output_file)
    write_markdown_file(output_file, flattened_content)
    print(f"Flattened Markdown file created: {output_file}")

if __name__ == "__main__":
    app()