from pydantic import BaseModel, Extra


class ExtrasForbiddenModel(BaseModel):
    class Config:
        extra = Extra.forbid
