"""index.md generator"""

from pathlib import Path

import mkdocs.utils

def get_copier_element() -> dict:
    return mkdocs.utils.yaml_load(Path('../.copier-answers.yml').read_text(encoding="utf-8"))


def get_badges():
    """Add badges"""
    # TODO: get badges from https://shields.io/ or copy from the coverage file
    return """
<p align="center">
<a href="https://github.com/tiangolo/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster" target="_blank">
    <img src="https://img.shields.io/github/languages/code-size/irangareddy/cmem-plugin-docs?style=plastic" alt="Test">
</a>
</p>
    """


def create_index_file():
    """Create Index File in docs"""

    # config = get_copier_element()

    lines = [
        f'{{ config["project_slug"] }}'

        # '{{project_description}}',
        # '<h5> Badges </h5>',
        # get_badges(),
        # "{{ macro_info() }}"
        # '<h5> Author Details </h5>'
        # ':fontawesome-brands-dev: {{author_name}}',
        # ':material-email: {{author_mail}}'
    ]

    with open("index.md", "w", encoding="utf-8") as index_file:
        for line in lines:
            print(line)
            index_file.write(f'{line}\n\n')


create_index_file()
