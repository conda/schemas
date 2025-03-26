# Conda Schemas

> **Warning**
> The schemas within this repository are considered works in
> progress/drafts.  Their contents may not fully reflect the current state of
> `conda` and associated tools.

Schemas for the conda ecosystem.

This repository is published to https://schemas.conda.org.

## Contribution workflow

The website logic is available at `site/`.

1. Create a new environment with `python >=3.12` and the requirements in `site/requirements.txt`. For example: `conda create -n schemas "python>=3.12" --file site/requirements.txt`.
2. With the activated environment, regenerate the site with `python site/publish.py`.
3. The generated contents are available at `_build/`. Serve it in your browser with `python -m http.server -d -build/`.

Details about each `site/` item:

- `index.j2.html`: HTML document templated with Jinja.
- `config.toml`: The variables used to render the HTML template.
- `_static/`: Anything in this directory is copied as is to `_build/`.
- `publish.py`: Python script to load the HTML template and render it with the contents in `config.toml`. It also handles `_static/` contents.
- `requirements.txt`: The dependencies needed by `publish.py`.

## Conventions for schema locations

- Ecosystem-wide schemas go in the "General" section. Example: `repodata.json`.
- Application-specific schemas go under a dedicated section. Example: `menuinst` schemas.
