import os
import click

def create_gitignore(project_path):
    """.gitignore file creation."""

    template_path = os.path.dirname(__file__)
    gitignore_content = os.path.join(template_path, '../templates/gitignore.txt')

    with open(os.path.join(project_path, '.gitignore'), 'w') as f:
        f.write(gitignore_content)
    
    click.echo(".gitignore file created.")
