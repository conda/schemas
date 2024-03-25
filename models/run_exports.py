from typing import Iterable

from pydantic import BaseModel, schema_json_of, constr, Field, Extra

CURRENT_VERSION = 1

ArtifactFilenameAny = constr(
    min_length=5, 
    regex=r"^[a-zA-Z0-9_\-\.]+-[a-zA-Z0-9_\.]+-[a-zA-Z0-9_\.]+\.[\S+]$"
)
ArtifactFilenameConda = constr(
    min_length=5, 
    regex=r"^[a-zA-Z0-9_\-\.]+-[a-zA-Z0-9_\.]+-[a-zA-Z0-9_\.]+\.conda$"
)
ArtifactFilenameTarBz2 = constr(
    min_length=5, 
    regex=r"^[a-zA-Z0-9_\-\.]+-[a-zA-Z0-9_\.]+-[a-zA-Z0-9_\.]+\.tar\.bz2$"
)
MatchSpecStr = constr(min_length=1)


class _OurBaseModel(BaseModel):
    class Config:
        extra = Extra.forbid


class RunExportsMap(_OurBaseModel):
    weak: Iterable[MatchSpecStr] = None
    strong: Iterable[MatchSpecStr] = None
    weak_constrains: Iterable[MatchSpecStr] = None
    strong_constrains: Iterable[MatchSpecStr] = None
    noarch: Iterable[MatchSpecStr] = None


class InfoHeader(_OurBaseModel):
    platform: str
    arch: str
    subdir: str
    version: int = CURRENT_VERSION


class RunExports(_OurBaseModel):
    class Config:
        extra = Extra.forbid

    info: InfoHeader
    packages: dict[ArtifactFilenameTarBz2, RunExportsMap] = Field(
        default_factory=dict,
    )
    packages_conda: dict[ArtifactFilenameConda, RunExportsMap] = Field(
        None,
        alias="packages.conda",
    )


if __name__ == "__main__":
    from pathlib import Path

    fn = f"run_exports-{CURRENT_VERSION}.schema.json"
    (Path(__file__).parent / "../schemas" / fn).write_text(
schema_json_of(RunExports, indent=2)
    )
