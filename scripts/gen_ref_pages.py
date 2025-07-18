"""Generate the code reference pages and navigation."""

from pathlib import Path

import mkdocs_gen_files

root = Path(__file__).parent.parent
src = root / "src" / "pyoframe"

for path in sorted(src.rglob("*.py")):
    module_path = path.relative_to(src).with_suffix("")
    doc_path = path.relative_to(src).with_suffix(".md")
    full_doc_path = Path("reference", "internal", doc_path)

    parts = ("pyoframe",) + tuple(module_path.parts)

    if parts[-1].startswith("_"):
        continue

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        ident = ".".join(parts)
        fd.write(f"# {module_path} \n\n::: {ident}")

    mkdocs_gen_files.set_edit_path(full_doc_path, Path("../") / path.relative_to(root))
