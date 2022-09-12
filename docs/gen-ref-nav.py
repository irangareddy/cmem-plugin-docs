"""Generate the code reference pages and navigation."""

from pathlib import Path

import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()

for path in sorted(Path("cmem_plugin_docs/").glob("**/*.py")):
    module_path = path.relative_to("cmem_plugin_docs/").with_suffix("")
    doc_path = path.relative_to("cmem_plugin_docs/").with_suffix(".md")
    full_doc_path = Path("reference", doc_path)

    parts = list(module_path.parts)
    try:
        if parts[-1] == "__init__":
            parts = parts[:-1]
            doc_path = doc_path.with_name("index.md")
            full_doc_path = full_doc_path.with_name("index.md")
        elif parts[-1] == "__main__":
            continue
        nav[parts] = doc_path
        print(doc_path)
    except ValueError:
        print(doc_path)
        print(f'Value Error at {full_doc_path}')

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        print(full_doc_path)
        ident = ".".join(parts)
        if len(ident) > 0:
            print("::: cmem_plugin_docs." + ident, file=fd)
        else:
            print("::: cmem_plugin_docs" + ident, file=fd)

    mkdocs_gen_files.set_edit_path(full_doc_path, path)

with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
