from __future__ import annotations

import sys
from pathlib import Path

from pyshacl import validate
from rdflib import Graph


BASE = Path(__file__).resolve().parent
DATA_FILES = [
    BASE / "decision-core.ttl",
    BASE / "decision-core-core.ttl",
    BASE / "decision-core-evidence.ttl",
    BASE / "decision-core-workflows.ttl",
]
SHAPES_FILE = BASE / "decision-core.shacl.ttl"


def load_graph(paths: list[Path]) -> Graph:
    graph = Graph()
    for path in paths:
        graph.parse(path)
    return graph


def main(argv: list[str]) -> int:
    extra = [Path(arg).resolve() for arg in argv[1:]]
    data_graph = load_graph(DATA_FILES + extra)
    shapes_graph = load_graph([SHAPES_FILE])

    conforms, _, report_text = validate(
        data_graph,
        shacl_graph=shapes_graph,
        inference="rdfs",
        abort_on_first=False,
        allow_infos=True,
        allow_warnings=True,
    )

    print("RDFLIB_PARSE_OK")
    print(f"SHACL_CONFORMS={str(conforms).lower()}")
    print(report_text)
    return 0 if conforms else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
