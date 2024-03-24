# tree2md

`tree2md` is a command-line tool that converts a nested markdown documentation tree to a single markdown document. It recursively traverses the directory structure and combines the contents of markdown files into a single output file.

## Installation

The recommended way to install `tree2md` is using [pipx](https://github.com/pipxproject/pipx), which allows you to install and run Python applications in isolated environments.

1. Install pipx if you haven't already:

   ```bash
   python3 -m pip install --user pipx
   python3 -m pipx ensurepath
   ```

2. Install `tree2md` using pipx:

   ```bash
   pipx install git+https://github.com/JacobFV/tree2md.git
   ```

## Usage

```bash
tree2md root_dir output_file
```

- `root_dir`: Path to the root directory of the documentation tree.
- `output_file`: Path to the output markdown file.

Example:

```bash
tree2md docs/ output.md
```

This command will convert the markdown files in the `docs/` directory and its subdirectories into a single markdown file named `output.md`.

## Updating

To update `tree2md` to the latest version, run:

```bash
pipx upgrade tree2md
```

## Uninstallation

To uninstall `tree2md`, run:

```bash
pipx uninstall tree2md
```

## Contributing

If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/JacobFV/tree2md).

## License

This project is licensed under the [MIT License](LICENSE).
