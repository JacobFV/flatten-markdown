import os
from pathlib import Path
import tempfile

from flatten_markdown.core import process_directory, process_file_flatten, process_file_unflatten
from flatten_markdown.utils import read_file, write_file

def test_flatten():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a temporary directory structure
        os.makedirs(Path(temp_dir) / 'dir1')
        os.makedirs(Path(temp_dir) / 'dir2')
        write_file(Path(temp_dir) / 'file1.md', '# File 1\nContent of file 1.')
        write_file(Path(temp_dir) / 'dir1' / 'file2.md', '# File 2\nContent of file 2.')
        write_file(Path(temp_dir) / 'dir2' / 'file3.md', '# File 3\nContent of file 3.')

        # Run the flatten function
        output_file = Path(temp_dir) / 'flattened.md'
        flattened_content = process_directory(temp_dir, process_file_flatten, output_file)
        write_file(output_file, flattened_content)

        # Check the flattened file content
        expected_content = '# file1\n\nContent of file 1.\n\n# dir1\n\n## file2\n\nContent of file 2.\n\n# dir2\n\n## file3\n\nContent of file 3.\n\n'
        assert read_file(output_file) == expected_content
