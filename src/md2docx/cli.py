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

    args = parser.parse_args()

    try:
        output_path = convert(
            args.input,
            output_path=args.output,
            template_path=args.template,
        )
    except subprocess.CalledProcessError:
        # Pandoc has already written its error to stderr; just exit cleanly.
        sys.exit(1)
    except Exception as e:
        print(f"md2docx: error: {e}", file=sys.stderr)
        sys.exit(1)

    print(output_path)
