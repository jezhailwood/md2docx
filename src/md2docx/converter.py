"""Core conversion logic.

Provides the `convert` function and its internal Pandoc helper.
"""

import subprocess
from importlib.resources import as_file, files
from pathlib import Path


def convert(
    input_path: str | Path,
    output_path: str | Path | None = None,
    template_path: str | Path | None = None,
    toc: bool = False,
    toc_depth: int = 3,
) -> Path:
    """Convert a Markdown file to a Word document.

    Args:
        input_path: Path to the source Markdown file.
        output_path: Destination path for the generated .docx file. Defaults to the
            input path with a .docx extension.
        template_path: Path to a custom Word reference document. If omitted, the bundled
            default template is used.
        toc: Whether to include a table of contents.
        toc_depth: Depth of the table of contents.

    Returns:
        The path to the generated .docx file.

    Raises:
        FileNotFoundError: If the input file or a supplied template cannot be found, or
            if Pandoc is not installed.
        NotADirectoryError: If the output directory does not exist.
        subprocess.CalledProcessError: If Pandoc exits with a non-zero status.
    """
    input_path = Path(input_path)

    if not input_path.exists():
        raise FileNotFoundError(f"input file not found: {input_path}")

    if output_path is None:
        output_path = input_path.with_suffix(".docx")
    else:
        output_path = Path(output_path)

    if not output_path.parent.exists():
        raise NotADirectoryError(
            f"output directory does not exist: {output_path.parent}"
        )

    if template_path is not None:
        template_path = Path(template_path)
        if not template_path.exists():
            raise FileNotFoundError(f"template file not found: {template_path}")
        _run_pandoc(input_path, output_path, template_path, toc, toc_depth)
    else:
        with as_file(files("md2docx.templates").joinpath("default.docx")) as default:
            _run_pandoc(input_path, output_path, default, toc, toc_depth)

    return output_path


def _run_pandoc(
    input_path: Path,
    output_path: Path,
    template_path: Path,
    toc: bool,
    toc_depth: int,
) -> None:
    cmd = [
        "pandoc",
        str(input_path),
        "-o",
        str(output_path),
        "-f",
        "markdown",
        "-t",
        "docx",
        "--reference-doc",
        str(template_path),
    ]
    if toc:
        cmd += ["--toc", f"--toc-depth={toc_depth}"]

    try:
        subprocess.run(cmd, check=True, stderr=subprocess.PIPE)
    except FileNotFoundError:
        raise FileNotFoundError(
            "pandoc is not installed or not on PATH — see https://pandoc.org"
        ) from None
