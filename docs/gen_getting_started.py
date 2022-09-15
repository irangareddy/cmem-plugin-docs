""" Getting Started"""

import mkdocs_gen_files


def generate_installation_content():
    """Installation Commands"""
    return [
        '<h2> Installation </h2>',
        'Using `pip`',
        """
        pip install cmem-plugin-{{ copier["project_slug"] }}
        """,
        'Using `poetry`',
        """
        poetry add cmem-plugin-{{ copier["project_slug"] }}
        """,
    ]


def create_gs_file():
    """Create Index File in docs"""

    lines = [
        '# cmem-plugin-{{ copier["project_slug"] }}',
        '{{ copier["project_description"] }}',
    ]

    lines += generate_installation_content()

    with mkdocs_gen_files.open("getting-started.md", "w") as index_file:
        for line in lines:
            index_file.write(f'{line}\n\n')


create_gs_file()