# How to write a DTU Compute thesis

This repository contains the documentation on how to write a thesis at DTU Compute. The documentation is created by
[Nicki Skafte Detlefsen](https://skaftenicki.github.io/) and mostly based on his experiences from supervising students
writing their thesis at DTU Compute. It is built using [Zensical](https://zensical.org/). The documentation is hosted on
[GitHub Pages](https://pages.github.com/). To build the documentation locally, follow the instructions below.

```
# Clone the repository
git clone https://github.com/SkafteNicki/dtu_cs_thesis
cd dtu_cs_thesis
# either install with pip
pip install pyproject.toml
zensical serve
# or install and run with uv
uv sync
uv run zensical serve
```

Documentation is online here: <https://skaftenicki.github.io/dtu_cs_thesis/>

## Checking links

CI checks all links with [lychee](https://lychee.cli.rs) on every pull request and once a week. It checks the built
site, so `#anchor` links are resolved exactly as readers see them, plus this README and the Markdown in the cookiecutter
template. Settings and the list of excluded sites (with the reason for each) are in `lychee.toml`. To run the same check
locally, [install lychee](https://lychee.cli.rs/guides/getting-started/) and run from the repository root:

```
uv run zensical build --clean
lychee site README.md '{{ cookiecutter.project_name }}/**/*.md'
```
