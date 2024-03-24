import os
from pathlib import Path
import tempfile

from flatten_markdown.core import process_directory, process_file_flatten, process_file_unflatten
from flatten_markdown.utils import read_file, write_file

def test_flatten_unflatten():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a temporary directory structure
        os.makedirs(Path(temp_dir) / 'dir1')
        os.makedirs(Path(temp_dir) / 'dir2')
        write_file(Path(temp_dir) / 'file1.md', '# File 1\nContent of file 1.')
        write_file(Path(temp_dir) / 'dir1' / 'file2.md', '# File 2\nContent of file 2.')
        write_file(Path(temp_dir) / 'dir2' / 'file3.md', '# File 3\nContent of file 3.')

        # Run the flatten function
        flattened_file = Path(temp_dir) / 'flattened.md'
        flattened_content = process_directory(temp_dir, process_file_flatten, flattened_file)
        write_file(flattened_file, flattened_content)

        # Run the unflatten function
        unflattened_dir = Path(temp_dir) / 'unflattened'
        process_file_unflatten(flattened_file, unflattened_dir)

        # Compare the original directory structure with the unflattened one
        assert os.path.exists(unflattened_dir / 'file1.md')
        assert os.path.exists(unflattened_dir / 'dir1' / 'file2.md')
        assert os.path.exists(unflattened_dir / 'dir2' / 'file3.md')

        assert read_file(unflattened_dir / 'file1.md') == 'Content of file 1.'
        assert read_file(unflattened_dir / 'dir1' / 'file2.md') == 'Content of file 2.'
        assert read_file(unflattened_dir / 'dir2' / 'file3.md') == 'Content of file 3.'
