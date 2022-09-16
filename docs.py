"""Docs Generator"""
import os
from pathlib import Path
import mkdocs_gen_files

PROJECT_NAME = 'cmem-plugin-{{ copier["project_slug"] }}'
PROJECT_DESCRIPTION = '{{ copier["project_description"] }}'


def project_details():
    """Returns Project name and project description"""
    return [
        f'<h1> {PROJECT_NAME} </h1>',
        f'<p1> {PROJECT_DESCRIPTION} </p1>'
    ]


def get_badges():
    """Add badges"""
    # TODO: get badges from https://shields.io/ or copy from the coverage file
    return """
<p align="center">
<a href="{{config.repo_url}}" target="_blank">
    <img src="https://img.shields.io/github/languages/code-size/irangareddy/cmem-plugin-docs?style=plastic" alt="Test">
</a>
</p>
    """


def generate_index_file():
    """Generate Index File in docs"""

    lines = project_details() + [
        '<h5> Badges </h5>',
        get_badges(),
        '<h5> Author Details </h5>',
        ':fontawesome-brands-dev: {{copier["author_name"]}}',
        ':fontawesome-solid-envelope: {{copier["author_mail"]}}'
    ]

    with mkdocs_gen_files.open("index.md", "w") as index_file:
        for line in lines:
            index_file.write(f'{line}\n\n')


def generate_installation_content():
    """Installation Commands"""
    return [
        '<h2> Installation </h2>',
        'Using `pip`',
        f"""
        pip install {PROJECT_NAME}
        """,
        'Using `poetry`',
        f"""
        poetry add {PROJECT_NAME}
        """,
    ]


def generate_getting_started():
    """Generate Getting Started Doc"""

    getting_started_content = project_details() + generate_installation_content()

    with mkdocs_gen_files.open("getting-started.md", "w") as index_file:
        for line in getting_started_content:
            index_file.write(f'{line}\n\n')


def generate_nav_bar_content(src_path: str, destination_path: str):
    """Generates Dynamic Nav Bar Content"""

    nav = mkdocs_gen_files.Nav()

    for path in sorted(Path(f'{src_path}/').glob("**/*.py")):
        module_path = path.relative_to(f'{src_path}/').with_suffix("")
        doc_path = path.relative_to(f'{src_path}/').with_suffix(".md")
        full_doc_path = Path(destination_path, doc_path)

        parts = list(module_path.parts)
        try:
            if parts[-1] == "__init__":
                parts = parts[:-1]
                doc_path = doc_path.with_name("index.md")
                full_doc_path = full_doc_path.with_name("index.md")
            elif parts[-1] == "__main__":
                continue
            nav[parts] = str(doc_path)
        except ValueError:
            # FIXME: Handle index file at package level
            pass

        with mkdocs_gen_files.open(full_doc_path, "w") as fd:
            ident = ".".join(parts)
            if len(ident) > 0:
                print(f"::: {src_path}." + ident, file=fd)
            else:
                print(f"::: {src_path}" + ident, file=fd)

        mkdocs_gen_files.set_edit_path(full_doc_path, path)

    with mkdocs_gen_files.open(f"{destination_path}/SUMMARY.md", "w") as nav_file:
        nav_file.writelines(nav.build_literate_nav())


generate_index_file()
generate_getting_started()
generate_nav_bar_content(src_path=f'cmem_plugin_{os.environ.get("project_slug")}',
                         destination_path='reference')
generate_nav_bar_content(src_path='tests', destination_path='how-to-guides')



