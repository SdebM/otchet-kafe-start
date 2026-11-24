import csv  # noqa: D100
from collections.abc import Iterator
from pathlib import Path


def read_rows(path: Path) -> Iterator[dict[str, str]]:
    """_summary_.
    
    Args:
        path: _description_
    """
    with open(path, encoding="utf-8", newline="") as file:
        yield from csv.DictReader(file)
