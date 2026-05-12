import subprocess
from importlib.resources import as_file, files
from pathlib import Path


def convert(
    input_path: str | Path,
    output_path: str | Path | None = None,
    template_path: str | Path | None = None,
) -> Path:
    input_path = Path(input_path)

    if output_path is None:
        output_path = input_path.with_suffix(".docx")
    else:
        output_path = Path(output_path)

    if template_path is not None:
        _run_pandoc(input_path, output_path, Path(template_path))
    else:
        with as_file(files("md2docx.templates").joinpath("default.docx")) as default:
            _run_pandoc(input_path, output_path, default)

    return output_path


def _run_pandoc(input_path: Path, output_path: Path, template_path: Path) -> None:
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
