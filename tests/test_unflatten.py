import os
from pathlib import Path
import tempfile

from flatten_markdown.core import process_directory, process_file_flatten, process_file_unflatten
from flatten_markdown.utils import read_file, write_file

def test_unflatten():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a temporary flattened file
        flattened_file = Path(temp_dir) / 'flattened.md'
        flattened_content = '# file1\n\nContent of file 1.\n\n# dir1\n\n## file2\n\nContent of file 2.\n\n# dir2\n\n## file3\n\nContent of file 3.\n\n'
        write_file(flattened_file, flattened_content)

        # Run the unflatten function
        output_dir = Path(temp_dir) / 'unflattened'
        process_file_unflatten(flattened_file, output_dir)

        # Check the unflattened directory structure and file contents
        assert os.path.exists(output_dir / 'file1.md')
        assert os.path.exists(output_dir / 'dir1' / 'file2.md')
        assert os.path.exists(output_dir / 'dir2' / 'file3.md')

        assert read_file(output_dir / 'file1.md') == 'Content of file 1.'
        assert read_file(output_dir / 'dir1' / 'file2.md') == 'Content of file 2.'
        assert read_file(output_dir / 'dir2' / 'file3.md') == 'Content of file 3.'
