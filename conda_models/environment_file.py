"""
WIP
"""
from typing import Dict, Iterable, Literal, Optional, Union

from pydantic import DirectoryPath

from ._base import ExtrasForbiddenModel
from .types import MatchSpecStr, NonEmptyStr, SubdirStr


class EnvironmentYaml(ExtrasForbiddenModel):
    name: Optional[str] = None
    "Name for the environment"
    channels: Optional[Iterable[NonEmptyStr]] = None
    "Channels to search for packages"
    dependencies: Union[
        NonEmptyStr,
        Iterable[Union[MatchSpecStr, Dict[Literal["pip"], Iterable[NonEmptyStr]]]],
    ] = ()
    "Packages to install into the environment, as a series of match specifications."
    variables: Optional[Dict[NonEmptyStr, str]] = None
    "Shell variables to define for the environment."
    prefix: Optional[DirectoryPath] = None
    "Path where the environment should be created."
    platforms: Optional[Iterable[SubdirStr]] = None
    "Platforms to search for packages."
