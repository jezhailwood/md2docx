import subprocess
from pathlib import Path


def convert(input_path: str | Path, output_path: str | Path | None = None) -> Path:
    input_path = Path(input_path)

    if output_path is None:
        output_path = input_path.with_suffix(".docx")
    else:
        output_path = Path(output_path)

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
        ],
        check=True,
    )

    return output_path
