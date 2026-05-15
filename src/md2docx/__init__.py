"""A command-line tool for converting Markdown files to Word documents.

Conversion is delegated to Pandoc, which applies a bundled Word reference document to
control styles and layout. The package installs an `md2docx` command;
`python -m md2docx` is equivalent.

Run `md2docx --help` for usage, or see `md2docx.cli` for full option details.
"""

from .converter import convert

__all__ = ["convert"]
