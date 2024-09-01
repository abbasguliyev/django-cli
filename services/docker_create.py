import os
import click

def create_docker_files(project_path, project_name):
    """Creates Docker files for the project."""

    # Define the paths to the template files
    template_path = os.path.dirname(__file__)
    compose_template = os.path.join(template_path, '../templates/docker-compose-template.txt')
    compose_local_template = os.path.join(template_path, '../templates/docker-compose-local-template.txt')

    # Create docker-compose.yml file
    with open(compose_template, 'r') as f:
        content = f.read().replace("{project_name}", project_name)
    with open(os.path.join(project_path, 'docker-compose.yml'), 'w') as f:
        f.write(content)

    # Create docker-compose-local.yml file
    with open(compose_local_template, 'r') as f:
        content = f.read().replace("{project_name}", project_name)
    with open(os.path.join(project_path, 'docker-compose-local.yml'), 'w') as f:
        f.write(content)

    dockerfile_content = os.path.join(template_path, '../templates/dockerfile.txt')

    with open(dockerfile_content, 'r') as f:
        content = f.read().replace("{project_name}", project_name)
    with open(os.path.join(project_path, 'src', 'Dockerfile'), 'w') as f:
        f.write(content)

    click.echo("Docker files created.")
