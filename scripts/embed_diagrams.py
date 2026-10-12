"""Copy the SVG diagrams from slides/img/ into the notebooks.

Colab opens a single uploaded .ipynb, so the notebooks cannot link to image files. Each diagram
lives in its own markdown cell whose metadata names the source file, for example
{"diagram": "circuit-anatomy.svg"}. This script rewrites those cells as a base64 data URI,
keeping the existing alt text, so the slides and notebooks share one copy of each diagram.

Run it from the repository root after editing any SVG in slides/img/:

    python scripts/embed_diagrams.py
"""

import base64
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "slides" / "img"
NOTEBOOKS = sorted((ROOT / "notebooks").glob("*.ipynb")) + sorted((ROOT / "notebooks" / "solutions").glob("*.ipynb"))
ALT = re.compile(r"!\[([^\]]*)\]\(")


def embed(path: Path) -> int:
    nb = json.loads(path.read_text(encoding="utf-8"))
    changed = 0
    for cell in nb["cells"]:
        name = cell.get("metadata", {}).get("diagram")
        if cell["cell_type"] != "markdown" or not name:
            continue
        match = ALT.search("".join(cell["source"]))
        alt = match.group(1) if match else Path(name).stem.replace("-", " ")
        data = base64.b64encode((IMG / name).read_bytes()).decode("ascii")
        source = [f"![{alt}](data:image/svg+xml;base64,{data})"]
        if cell["source"] != source:
            cell["source"] = source
            changed += 1
    if changed:
        path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return changed


if __name__ == "__main__":
    for notebook in NOTEBOOKS:
        print(f"{notebook.relative_to(ROOT)}: {embed(notebook)} diagram cell(s) updated")
