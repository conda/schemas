"""
WIP
"""

from collections.abc import Iterable
from typing import Literal

from pydantic import DirectoryPath

from ._base import ExtrasForbiddenModel
from .types import MatchSpecStr, NonEmptyStr, SubdirStr


class EnvironmentYaml(ExtrasForbiddenModel):
    name: str | None = None
    "Name for the environment"
    channels: Iterable[NonEmptyStr] | None = None
    "Channels to search for packages"
    dependencies: (
        NonEmptyStr
        | Iterable[MatchSpecStr | dict[Literal["pip"], Iterable[NonEmptyStr]]]
    ) = ()
    "Packages to install into the environment, as a series of match specifications."
    variables: dict[NonEmptyStr, str] | None = None
    "Shell variables to define for the environment."
    prefix: DirectoryPath | None = None
    "Path where the environment should be created."
    platforms: Iterable[SubdirStr] | None = None
    "Platforms to search for packages."
