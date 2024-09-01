import os
import click
import shutil
from services.docker_create import create_docker_files
from services.gitignore_create import create_gitignore
from services.user_create import create_custom_user_app

@click.command()
def create_project():
    """Creates a new Django project and configures it."""
    
    project_name = click.prompt('Project name', type=str)
    project_path = f"./{project_name}"

    # Create project and src directories
    os.makedirs(f"{project_path}/src", exist_ok=True)
    
    # Initialize Django project
    os.system(f"django-admin startproject {project_name} {project_path}/src")

    # Create Docker files if the option is selected
    create_docker_files(project_path, project_name)
    
    # Create .gitignore file
    create_gitignore(project_path)

    # Create account app and customize the User model
    create_custom_user_app(project_path)

    # Prompt user for additional apps to create
    while True:
        add_app = click.confirm('Would you like to add a new app?', default=True)
        if not add_app:
            break
        app_name = click.prompt('App name', type=str)
        create_app_structure(project_path, app_name)
    
    # Configure Django settings module
    setup_settings_module(project_path)

    click.echo(f"Project {project_name} created successfully!")



def create_app_structure(project_path, app_name):
    """Creates a new Django app with the specified folder structure."""
    
    app_path = os.path.join(project_path, 'src', app_name)
    os.makedirs(app_path, exist_ok=True)
    
    os.system(f"django-admin startapp {app_name} {app_path}")

    # Create API structure
    os.makedirs(os.path.join(app_path, 'api', 'serializers'), exist_ok=True)
    os.makedirs(os.path.join(app_path, 'api', 'selectors'), exist_ok=True)
    os.makedirs(os.path.join(app_path, 'api', 'services'), exist_ok=True)

    # Create empty files
    open(os.path.join(app_path, 'api', 'serializers', '__init__.py'), 'w').close()
    open(os.path.join(app_path, 'api', 'selectors', '__init__.py'), 'w').close()
    open(os.path.join(app_path, 'api', 'services', '__init__.py'), 'w').close()
    open(os.path.join(app_path, 'api', 'urls.py'), 'w').close()
    open(os.path.join(app_path, 'api', 'views.py'), 'w').close()
    
    click.echo(f"App {app_name} created and structured.")

def setup_settings_module(project_path):
    """Sets up the settings package and configures the settings files."""
    
    settings_path = os.path.join(project_path, 'src', 'config', 'settings')
    os.makedirs(settings_path, exist_ok=True)

    original_settings_path = os.path.join(project_path, 'src', 'config', 'settings.py')

    # Create base.py and move default settings content here
    base_settings_path = os.path.join(settings_path, 'base.py')
    with open(base_settings_path, 'w') as f:
        f.write("from pathlib import Path\n\n")
        f.write("# Base settings\n")
    
        if os.path.exists(original_settings_path):
            with open(original_settings_path, 'r') as original_settings:
                f.write(original_settings.read())

    # Add AUTH_USER_MODEL setting to base.py
    with open(base_settings_path, 'a') as f:
        f.write("\n\n# Custom User Model\n")
        f.write("AUTH_USER_MODEL = 'account.User'\n")

    # Create dev.py and prod.py
    with open(os.path.join(settings_path, 'dev.py'), 'w') as f:
        f.write("from .base import *\n")
        f.write("# Development settings\n")

    with open(os.path.join(settings_path, 'prod.py'), 'w') as f:
        f.write("from .base import *\n")
        f.write("# Production settings\n")
    
    # Remove settings.py file
    if os.path.exists(original_settings_path):
        os.remove(original_settings_path)

    click.echo("Settings module configured.")

if __name__ == '__main__':
    create_project()
