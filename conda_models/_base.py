from pydantic import BaseModel, Extra
from pydantic.main import ModelMetaclass


class ExtrasForbiddenModel(BaseModel):
    class Config:
        extra = Extra.forbid


class AllOptional(ModelMetaclass):
    def __new__(mcls, name, bases, namespaces, **kwargs):
        cls = super().__new__(mcls, name, bases, namespaces, **kwargs)
        for field in cls.__fields__.values():
            field.required = False
        return cls


def export_to_json(model, path):
    with open(path, "w") as f:
        f.write(model.json(indent=2))
