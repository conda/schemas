import shutil
from pathlib import Path

import requests
from jinja2 import Template
from ruamel.yaml import YAML
from markdown import markdown

HERE = Path(__file__).parent
BUILD = HERE / ".." / "_build"
BUILD.mkdir(exist_ok=True)
yaml = YAML(typ="safe")


with open(HERE / "config.yml") as f:
    config = yaml.load(f)

for section in config["sections"]:
    dirname = section.get("dirname", "")
    for item in section["items"]:
        source = item["schema"]
        if source.startswith(("http://", "https://")):
            r = requests.get(source)
            r.raise_for_status()
            text = r.text
        else:
            text = (HERE / ".." / source).read_text()
        name = source.rsplit("/", 1)[-1]
        output_path = f"{dirname}/{name}" if dirname else name
        if dirname:
            (BUILD / dirname).mkdir(parents=True, exist_ok=True)
        (BUILD / output_path).write_text(text)
        item["name"] = name
        item["url"] = f"/{output_path}"


template = Template(Path(HERE / "index.j2.html").read_text())
template.globals["markdown"] = markdown
(BUILD / "index.html").write_text(template.render(config))
for path in (HERE / "_static").glob("*"):
    shutil.copy(path, BUILD)
