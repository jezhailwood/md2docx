import subprocess
from importlib.resources import as_file, files
from pathlib import Path


def convert(
    input_path: str | Path,
    output_path: str | Path | None = None,
    template_path: str | Path | None = None,
) -> Path:
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
        _run_pandoc(input_path, output_path, template_path)
    else:
        with as_file(files("md2docx.templates").joinpath("default.docx")) as default:
            _run_pandoc(input_path, output_path, default)

    return output_path


def _run_pandoc(input_path: Path, output_path: Path, template_path: Path) -> None:
    try:
        subprocess.run(
            [
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
            ],
            check=True,
        )
    except FileNotFoundError:
        raise FileNotFoundError(
            "pandoc is not installed or not on PATH — see https://pandoc.org"
        ) from None
