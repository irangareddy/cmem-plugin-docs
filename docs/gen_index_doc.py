"""index.md generator"""


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


def create_index_file():
    """Create Index File in docs"""

    lines = [
        '# cmem-plugin-{{ copier["project_slug"] }}',
        '{{ copier["project_description"] }}',
        '<h5> Badges </h5>',
        get_badges(),
        '<h5> Author Details </h5>'
        ':fontawesome-brands-dev: {{copier["author_name"]}}',
        ':material-email: {{copier["author_mail"]}}'
    ]

    with open("docs/index.md", "w", encoding="utf-8") as index_file:
        for line in lines:
            index_file.write(f'{line}\n\n')


create_index_file()
