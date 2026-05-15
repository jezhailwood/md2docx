import subprocess
import sys
from argparse import ArgumentParser
from pathlib import Path

from md2docx.converter import convert


def main() -> None:
    parser = ArgumentParser(
        prog="md2docx",
        description="Convert a Markdown file to a Word document",
    )
    parser.add_argument(
        "input",
        metavar="INPUT",
        type=Path,
        help="markdown file to convert",
    )
    parser.add_argument(
        "-o",
        "--output",
        metavar="OUTPUT",
        type=Path,
        default=None,
        help="output path (default: INPUT with .docx extension)",
    )
    parser.add_argument(
        "--template",
        metavar="TEMPLATE",
        type=Path,
        default=None,
        help="custom Word reference document (.docx)",
    )
    parser.add_argument(
        "--toc",
        action="store_true",
        help="include a table of contents",
    )
    parser.add_argument(
        "--toc-depth",
        metavar="DEPTH",
        type=int,
        default=3,
        help="depth of table of contents (default: 3)",
    )

    args = parser.parse_args()

    try:
        output_path = convert(
            input_path=args.input,
            output_path=args.output,
            template_path=args.template,
            toc=args.toc,
            toc_depth=args.toc_depth,
        )
    except subprocess.CalledProcessError:
        # Pandoc has already written its error to stderr; just exit cleanly.
        sys.exit(1)
    except Exception as e:
        print(f"md2docx: error: {e}", file=sys.stderr)
        sys.exit(1)

    print(output_path)
