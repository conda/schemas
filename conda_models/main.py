"""
Generate JSON Schema files from existing models
"""

import json
from pathlib import Path

from . import __all__ as Models

HERE = Path(__file__).parent
ROOT = HERE.parent


def main():
    schemas_dir = ROOT / "schemas"
    schemas_dir.mkdir(parents=True, exist_ok=True)
    for Model in Models:
        data = Model.model_json_schema()
        data["$schema"] = "https://json-schema.org/draft/2020-12/schema"
        text = json.dumps(data, indent=2, sort_keys=True) + "\n"
        (schemas_dir / f"{Model.__name__.lower()}.json").write_text(text)


if __name__ == "__main__":
    main()
