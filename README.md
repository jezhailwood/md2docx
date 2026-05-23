# md2docx

A command-line tool for converting Markdown files to Word documents. Conversion is delegated to [Pandoc](https://pandoc.org), which applies a bundled Word reference document to control styles and layout. The package installs an `md2docx` command; `python -m md2docx` is equivalent.

## Installation

Install from GitHub using pip:

```shell
pip install "md2docx @ git+https://github.com/jezhailwood/md2docx.git@v0.1.0"
```

Alternatively, add as a dependency in `pyproject.toml`:

```toml
dependencies = [
    "md2docx @ git+https://github.com/jezhailwood/md2docx.git@v0.1.0",
]
```

Replace `v0.1.0` with the [latest release tag](https://github.com/jezhailwood/md2docx/tags).

## Quickstart

Run `md2docx --help` for a full list of options.

Pass a Markdown file to convert it to a Word document. The output file is written to the same directory as the input file, with the same name and a `.docx` extension:

```shell
md2docx document.md
```

### Output path

To write the output to a specific location, pass `--output` (or `-o`):

```shell
md2docx document.md --output reports/report.docx
```

The output directory must already exist.

### Template

By default, `md2docx` applies a bundled Word reference document that controls styles and layout. To use a custom reference document instead, pass `--template`:

```shell
md2docx document.md --template my-template.docx
```

The template must be a `.docx` file.

### Table of contents

Pass `--toc` to include a table of contents. Use `--toc-depth` to set how many heading levels it covers (1–6, default 3):

```shell
md2docx document.md --toc
md2docx document.md --toc --toc-depth 2
```

## Notes

- **Pandoc required.** `md2docx` delegates conversion to [Pandoc](https://pandoc.org), which must be installed separately and available on `PATH`. The package does not install Pandoc automatically.

## API reference

Full documentation is available at [jezhailwood.github.io/md2docx](https://jezhailwood.github.io/md2docx).

## Licence

Released under the [MIT Licence](LICENSE).
