from invoke import task, Context

common_options = {"echo": True}


@task
def clean(ctx: Context):
    """Clean the project by removing build artifacts."""
    ctx.run("rm -rf build dist *.egg-info", **common_options)
    ctx.run("rm -rf project_name", **common_options)
    ctx.run("rm -rf .ruff_cache", **common_options)
    # remove all files in the template directory that are ignored by git
    ctx.run(
        "cd \{\{\ cookiecutter.project_name\ \}\}/ && find . -type f | git check-ignore --stdin | xargs rm -f",
        **common_options,
    )


@task()
def template(ctx: Context):
    """Generate a new project from template."""
    ctx.run("uv run cookiecutter . -f --no-input --verbose", **common_options)


@task()
def docs(ctx: Context, live: bool = True):
    """Build the documentation."""
    ctx.run(f"mkdocs {'serve' if live else 'build'}", **common_options)
