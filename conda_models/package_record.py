"""
Definitions for the repodata.json files served in conda channels.
"""
from typing import Iterable, Union

from ._base import ExtrasForbiddenModel
from .types import (
    BuildNumber,
    BuildStr,
    NameVersionBuildMatchSpecStr,
    NaturalInt,
    Noarch,
    Subdir,
    VersionStr,
)


class RepodataRecord(ExtrasForbiddenModel):
    """
    A single record in the conda repodata.

    A single record refers to a single binary distribution of a package on a conda channel.
    """

    arch: str = None
    "Optionally the architecture the package supports"
    build: BuildStr
    "The build string of the package."
    build_number: BuildNumber
    "The build number of the package."
    constrains: Iterable[NameVersionBuildMatchSpecStr]
    """
    Additional constraints on packages. `constrains` are different from `depends` in that packages
    specified in `depends` must be installed next to this package, whereas packages specified in
    `constrains` are not required to be installed, but if they are installed they must follow these
    constraints.
    """
    depends: Iterable[NameVersionBuildMatchSpecStr]
    "Specification of packages this package depends on."
    features: str = None
    """
    Features are a deprecated way to specify different feature sets for the conda solver. This is
    not supported anymore and should not be used. Instead, `mutex` packages should be used to
    specify mutually exclusive features.
    """
    legacy_bz2_md5: str = None
    "A deprecated md5 hash"
    legacy_bz2_size: NaturalInt = None
    "A deprecated package archive size"
    license: str = None
    "The specific license of the package"
    license_family: str = None
    "The specific license of the package"
    md5: str = None
    "The md5 hash of the package archive"
    name: str
    "The name of the package"
    noarch: Noarch
    "Whether the package is architecture independent, and in which way."
    platform: str = None
    "The platform the package supports"
    sha256: str = None
    "The sha256 hash of the package archive"
    size: NaturalInt = None
    "The size of the package archive, in bytes"
    subdir: Subdir
    "The subdirectory of the channel this package is in"
    timestamp: int = None
    "The date this entry was created"
    track_features: Union[str, Iterable[str]] = None
    """
    Nowadays only used to downweight package variants (ie. give a variant less priority). To that
    effect, the number of track features is counted (number of commas) and the package is
    downweighted by the number of track_features.
    """
    version: VersionStr
    "The version of the package"
    preferred_env: str = None
    "Unused"
    date: str = None
    "Unused"
    package_type: str = None
    "Unused"
