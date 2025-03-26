import shutil
import tomllib
from pathlib import Path

import requests
from jinja2 import Template
from commonmark import commonmark

HERE = Path(__file__).parent
BUILD = HERE / ".." / "_build"
BUILD.mkdir(exist_ok=True)


config = tomllib.loads((HERE / "config.toml").read_text())

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
        item["url"] = output_path


template = Template(Path(HERE / "index.j2.html").read_text())
template.globals["markdown"] = commonmark
(BUILD / "index.html").write_text(template.render(config))
for path in (HERE / "_static").glob("*"):
    shutil.copy(path, BUILD)
