from typing import Any
import random

from dataclasses import dataclass
from pathlib import Path


try:
    import tomllib
except ImportError:
    import tomli as tomllib

PATTERNS_FILE = Path(__file__).parent / "patterns.toml"

def get_pattern(name, filename=PATTERNS_FILE):
    data = tomllib.loads(filename.read_text(encoding="utf-8"))
    return Pattern.from_toml(name, toml_data=data[name])

def get_all_patterns(filename=PATTERNS_FILE):
    data = tomllib.loads(filename.read_text(encoding="utf-8"))
    return [
        Pattern.from_toml(name, toml_data) for name, toml_data in data.items()
    ]

@dataclass
class Pattern:
    name:str
    alive_cells: Any # set[tuple[int, int]]

    @classmethod
    def from_toml(cls, name, toml_data):
        return cls(
            name,
            alive_cells={tuple(cell) for cell in toml_data["alive_cells"]},
        )

    @classmethod
    def from_random(cls):
        cells = set()

        start_col, start_row, end_col, end_row = (0, 0, 20, 20)
        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                alive = random.choice((True, False))
                if alive:
                    cells.add((col, row))


        return cls(
            'Random',
            alive_cells=cells,
        )
     
    