from functools import cache

from pydantic import BaseModel, Extra, create_model


class ExtrasForbiddenModel(BaseModel):
    class Config:
        extra = Extra.forbid


@cache
def make_optional(baseclass: type[BaseModel]) -> type[BaseModel]:
    """Extracts the fields and validators from the baseclass and make fields optional"""
    fields = baseclass.__fields__
    validators = {"__validators__": baseclass.__validators__}
    optional_fields = {key: (item.type_ | None, None) for key, item in fields.items()}
    return create_model(
        f"Optional{baseclass.__name__}",
        **optional_fields,
        __validators__=validators,
    )


def export_to_json(model, path):
    with open(path, "w") as f:
        f.write(model.json(indent=2))
