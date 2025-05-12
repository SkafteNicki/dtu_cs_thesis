from invoke import task, Context


@task
def clean(ctx: Context):
    """Clean the project by removing build artifacts."""
    ctx.run("rm -rf build dist *.egg-info")
    ctx.run("rm -rf project_name")
    ctx.run("rm -rf .ruff_cache")


@task
def template(ctx: Context):
    """Generate a new project from template."""
    ctx.run("uv run cookiecutter . -f --no-input --verbose", echo=True)
