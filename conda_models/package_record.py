"""
Definitions for the repodata.json files served in conda channels.
"""

from collections.abc import Iterable
from enum import Enum
from typing import Literal

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
    noarch: NoarchStr | None = None
    "Whether the package is architecture independent, and in which way."
    platform: str | None = None
    "The platform the package supports"
    sha256: SHA256Str | None = None
    "The sha256 hash of the package archive"
    size: PositiveInt | None = None
    "The size of the package archive, in bytes"
    subdir: SubdirStr
    "The subdirectory of the channel this package is in"
    timestamp: PositiveInt = 0
    "The date this entry was created, as a Unix timestamp in milliseconds"
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


class LinkType(Enum):
    hardlink = 1
    softlink = 2
    copy = 3
    directory = 4


class PathType(Enum):
    hardlink = "hardlink"
    softlink = "softlink"
    directory = "directory"


class PathDataV1(ExtrasForbiddenModel):
    _path: NonEmptyStr = ...
    file_mode: Literal["text", "binary"] | None = None
    inode_paths: list[NonEmptyStr] | None = None
    no_link: bool | None = None
    path_type: PathType | None = None
    prefix_placeholder: NonEmptyStr | None = None
    sha256_in_prefix: SHA256Str | None = None
    sha256: SHA256Str | None = None
    size_in_bytes: PositiveInt | None = None


class PathsDataV1(ExtrasForbiddenModel):
    paths_version: Literal[1] = 1
    paths: list[PathDataV1] = []


class Link(ExtrasForbiddenModel):
    source: NonEmptyStr = ...
    type: LinkType = ...


class PrefixRecord(PackageRecord):
    """
    A package installed in an environment.

    Extends `PackageRecord` with additional details about how the package was installed
    in the target environment.
    """

    extracted_package_dir: str = ...
    "Full path to the local extracted package"

    package_tarball_full_path: str = ...
    "Full path to the local package file"

    files: list[NonEmptyStr] = []
    "The list of all files comprising the package as relative paths from the prefix root"

    paths_data: PathsDataV1 = PathsDataV1()
    "List with additional information about the files, e.g. checksums and link type"

    link: Link = ...
    "Information about how the package was linked into the prefix"

    requested_spec: NonEmptyStr | None = None
    "The `MatchSpec` requested for this package by the user, if any."
