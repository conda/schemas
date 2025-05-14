from functools import cache

from pydantic import BaseModel, ConfigDict, create_model


class ExtrasForbiddenModel(BaseModel):
    model_config: ConfigDict = ConfigDict(
        extra="forbid",
        use_attribute_docstrings=True,
    )


@cache
def make_optional(baseclass: type[BaseModel]) -> type[BaseModel]:
    """Extracts the fields and validators from the baseclass and make fields optional"""
    fields = baseclass.model_fields
    # validators = {"__validators__": baseclass.__validators__}
    optional_fields = {
        key: (item.annotation | None, None) for key, item in fields.items()
    }
    return create_model(
        f"Optional{baseclass.__name__}",
        **optional_fields,
        # __validators__=validators,
    )
