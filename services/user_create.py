import os
import click


def create_custom_user_app(project_path):
    """Creates the account app with a custom User model."""

    app_path = os.path.join(project_path, 'src', 'account')
    os.makedirs(app_path, exist_ok=True)

    os.system(f"django-admin startapp account {app_path}")

    models_content = """
        from django.contrib.auth.models import AbstractUser
        from django.db import models

        class User(AbstractUser):
            # Additional fields can be defined here
            pass
    """

    with open(os.path.join(app_path, 'models.py'), 'w') as f:
        f.write(models_content)

    click.echo("Account app with custom User model created.")
