"""
WIP
"""
from typing import Dict, Iterable, Union

from pydantic import DirectoryPath, validator

from ._base import ExtrasForbiddenModel
from .types import MatchSpecStr, NonEmptyStr, PackageNameStr, SubdirStr


class EnvironmentYaml(ExtrasForbiddenModel):
    name: str = None
    "Name for the environment"
    channels: Iterable[NonEmptyStr] = None
    "Channels to search for packages"
    dependencies: Union[
        str,
        Iterable[Union[MatchSpecStr, Dict[PackageNameStr, Iterable[str]]]],
    ] = ()
    "Packages to install into the environment, as a series of match specifications."
    variables: Dict[NonEmptyStr, str] = None
    "Shell variables to define for the environment."
    prefix: DirectoryPath = None
    "Path where the environment should be created."
    platforms: Iterable[SubdirStr] = None
    "Platforms to search for packages"

    @validator("dependencies")
    def only_pip_key_allowed(cls, v):
        for item in v:
            if isinstance(item, dict) and item.keys() != {"pip"}:
                msg = "Only 'pip: [str]' is allowed in 'dependencies'"
                raise ValueError(msg)
        return v
