from pydantic import BaseModel, Extra


class ExtrasForbiddenModel(BaseModel):
    class Config:
        extra = Extra.forbid


def export_to_json(model, path):
    with open(path, "w") as f:
        f.write(model.json(indent=2))
