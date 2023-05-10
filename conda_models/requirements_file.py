"""
WIP
"""
from typing import Iterable, Optional

from ._base import ExtrasForbiddenModel
from .types import MatchSpecStr, SubdirStr


class RequirementsTxt(ExtrasForbiddenModel):
    """
    A requirements.txt file as produced by conda list --export or conda list --explicit

    ```
    # This file may be used to create an environment using:
    # $ conda create --name <env> --file <this file>
    # platform: osx-64
    @EXPLICIT
    https://repo.anaconda.com/pkgs/free/osx-64/mkl-11.3.3-0.tar.bz2
    https://repo.anaconda.com/pkgs/free/osx-64/numpy-1.11.1-py35_0.tar.bz2
    https://repo.anaconda.com/pkgs/free/osx-64/openssl-1.0.2h-1.tar.bz2
    https://repo.anaconda.com/pkgs/free/osx-64/pip-8.1.2-py35_0.tar.bz2
    https://repo.anaconda.com/pkgs/free/osx-64/python-3.5.2-0.tar.bz2
    https://repo.anaconda.com/pkgs/free/osx-64/readline-6.2-2.tar.bz2
    ```
    """
    platform: Optional[SubdirStr] = None
    explicit: bool = False
    records: Iterable[MatchSpecStr] = ()

    @classmethod
    def from_str(cls, value: str):
        raise NotImplementedError("TODO")

