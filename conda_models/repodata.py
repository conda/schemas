"""
Definitions for the repodata.json files served in conda channels.
"""
from pydantic import AnyUrl, Field

from ._base import ExtrasForbiddenModel, make_optional
from .package_record import PackageRecord
from .types import (
    CondaPackageFileNameStr,
    NonEmptyStr,
    PackageFileNameStr,
    Subdir,
    TarBz2PackageFileNameStr,
)


class RepodataRecord(PackageRecord):
    """
    A single record in the conda repodata.

    A single record refers to a single binary distribution of a package on a conda channel.
    """

    filename: str = Field(..., alias="fn")
    "The filename of the package archive"
    url: AnyUrl
    "The canonical URL from where to get this package"
    channel: NonEmptyStr
    """
    String representation of the channel where the package comes from.
    It can be a URL (preferred) or a channel name.
    """
    revoked: bool = None
    "DEPRECATED."


OptionalRepodataRecord = make_optional(RepodataRecord)


class ChannelInfo(ExtrasForbiddenModel):
    """ """

    subdir: Subdir


class Repodata(ExtrasForbiddenModel):
    """ """

    info: ChannelInfo
    "Information about the repodata"
    packages: dict[TarBz2PackageFileNameStr, OptionalRepodataRecord]
    "The .tar.bz2 packages in the repodata"
    packages_conda: dict[CondaPackageFileNameStr, OptionalRepodataRecord] = Field(
        ...,
        alias="packages.conda",
    )
    "The .conda packages in the repodata"
    removed: set[PackageFileNameStr]
    "The packages that have been removed from the repodata"
    version: int = Field(..., alias="repodata_version")
    "The version of the repodata"
