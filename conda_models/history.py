"""
WIP
"""
from typing import Iterable, Union

from pydantic import Field

from ._base import ExtrasForbiddenModel
from .match_spec import MatchSpec
from .package_record import PackageRecord
from .types import MatchSpecStr


class HistoryRecord(ExtrasForbiddenModel):
    """
    A single record in the conda history.
    """
    timestamp: int
    "Date when the action was recorded"
    command: str
    "The command that was run"
    specs: Iterable[Union[MatchSpec, MatchSpecStr]]
    "The specs that the user asked for explicitly"
    added: Iterable[PackageRecord] = ()
    "The packages that were added to the environment as a result of the transaction"
    removed: Iterable[PackageRecord] = ()
    "The packages that were removed from the environment as a result of the transaction"
    info: dict[str, str] = Field(default_factory=dict)
    "Arbitrary metadata to be stored with the history record, like the conda client version"

    @classmethod
    def from_str(cls, value: str):
        raise NotImplementedError("TODO")


class History(ExtrasForbiddenModel):
    """
    Placed in conda-meta/history, holds a series of actions formatted like:

    ```
    ==> 2019-01-29 21:16:11 <==
    # cmd: /abs/path/to/bin/conda install -c conda-forge numpy
    # conda version: 4.6.1
    -conda-forge::certifi-2018.11.29-py36_1000
    -defaults::blas-1.0-mkl
    -defaults::chardet-3.0.4-py36h0f667ec_1
    -defaults::numpy-1.12.1-py36he24570b_1
    +conda-forge::blas-1.1-openblas
    +conda-forge::wheel-0.32.3-py37_0
    +defaults::python-3.7.2-h0371630_0
    # update specs: ['numpy']
    ```
    """
    records: Iterable[HistoryRecord]

    @classmethod
    def from_str(cls, value: str):
        raise NotImplementedError("TODO")
