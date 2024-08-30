import os
import click

@click.command()
@click.option('--name', prompt='Layihənin adı', help='Yaradılacaq Django layihəsinin adı.')
def create_project(name, docker):
    """Django layihəsi yaradır və konfiqurasiya edir."""
    
    # Django layihəsini yaradın
    os.system(f"django-admin startproject {name}")

    # "src" papkası yaradın
    os.makedirs(f"{name}/src")

    # Şablon faylını oxuyun
    with open("docker-compose-template.yml", "r") as template_file:
        template_content = template_file.read()
    
    # Şablonu istifadəçinin daxil etdiyi layihə adı ilə əvəz edin
    docker_compose_content = template_content.format(project_name=name)
    
    # Yaradılmış məzmunu yeni docker-compose.yml faylına yazın
    with open(f"{name}/docker-compose.yml", "w") as f:
        f.write(docker_compose_content)
    
    click.echo("Docker faylları yaradıldı.")

    click.echo(f"{name} layihəsi uğurla yaradıldı!")

if __name__ == '__main__':
    create_project()