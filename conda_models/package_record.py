"""
Definitions for the repodata.json files served in conda channels.
"""

from collections.abc import Iterable

from pydantic import PositiveInt

from ._base import ExtrasForbiddenModel
from .types import (
    BuildNumber,
    BuildStr,
    MD5Str,
    NameVersionBuildMatchSpecStr,
    NoarchStr,
    NonEmptyStr,
    PackageNameStr,
    SHA256Str,
    SubdirStr,
    VersionStr,
)


class PackageRecord(ExtrasForbiddenModel):
    """
    A single record in the conda repodata.

    A single record refers to a single binary distribution of a package on a conda channel.
    """

    arch: str | None = None
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
    features: NonEmptyStr | None = None
    """
    Features are a deprecated way to specify different feature sets for the conda solver. This is
    not supported anymore and should not be used. Instead, `mutex` packages should be used to
    specify mutually exclusive features.
    """
    legacy_bz2_md5: NonEmptyStr | None = None
    "A deprecated md5 hash"
    legacy_bz2_size: PositiveInt | None = None
    "A deprecated package archive size"
    license: NonEmptyStr | None = None
    "The specific license of the package"
    license_family: NonEmptyStr | None = None
    "The specific license of the package"
    md5: MD5Str | None = None
    "The md5 hash of the package archive"
    name: PackageNameStr
    "The name of the package"
    noarch: NoarchStr
    "Whether the package is architecture independent, and in which way."
    platform: str | None = None
    "The platform the package supports"
    sha256: SHA256Str | None = None
    "The sha256 hash of the package archive"
    size: PositiveInt | None = None
    "The size of the package archive, in bytes"
    subdir: SubdirStr
    "The subdirectory of the channel this package is in"
    timestamp: PositiveInt | None = None
    "The date this entry was created"
    track_features: NonEmptyStr | Iterable[NonEmptyStr] | None = None
    """
    Nowadays only used to downweight package variants (ie. give a variant less priority). To that
    effect, the number of track features is counted (number of commas) and the package is
    downweighted by the number of track_features.
    """
    version: VersionStr
    "The version of the package"
    preferred_env: str | None = None
    "Unused"
    date: str | None = None
    "Unused"
    package_type: str | None = None
    "Unused"
