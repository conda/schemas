from typing import Iterable, Optional

from pydantic import AnyUrl, Field

from ._base import ExtrasForbiddenModel
from .run_exports import RunExports
from .types import PackageNameStr, VersionStr


class ChannelDataPackage(ExtrasForbiddenModel):
    has_activate_scripts: bool = Field(..., alias="activate.d")
    "Whether the package contains activation scripts"
    has_deactivate_scripts: bool = Field(..., alias="deactivate.d")
    "Whether the package contains deactivation scripts"
    binary_prefix: bool
    "Whether the package contains binary files that hardcode the installation prefix"
    description: Optional[str] = None
    "The description of the package"
    dev_url: Optional[Iterable[AnyUrl]] = None
    "The URL to the development page of the package"
    doc_url: Optional[Iterable[AnyUrl]] = None
    "The URL to the documentation page of the package"
    home: Optional[Iterable[AnyUrl]] = None
    "The URL to the homepage of the package"
    source_url: Optional[Iterable[AnyUrl]] = None
    "The URL to the latest source code of the package"
    license: Optional[str] = None
    "The license of the package"
    has_post_link_scripts: bool
    "Whether the package contains post-link scripts"
    has_pre_link_scripts: bool
    "Whether the package contains pre-link scripts"
    has_pre_unlink_scripts: bool
    "Whether the package contains pre-unlink scripts"
    run_exports: dict[VersionStr, RunExports]
    "The run exports of the package, per package version (not build!)"
    subdirs: Iterable[str]
    "Which subdirs the package is available in"
    summary: Optional[str] = None
    "The summary of the package. Shorter than description."
    text_prefix: bool
    "Whether the package contains text files that hardcode the installation prefix"
    timestamp: Optional[int] = None
    "Last update time for artifacts of this package"
    version: Optional[VersionStr] = None
    "The latest version of the package"


class ChannelData(ExtrasForbiddenModel):
    """
    Data structures that are present in a `channeldata.json` file. Some channels on anaconda.org
    contain a `channeldata.json` file which describes the subdirs the channel contains, the
    packages stored in the channel and additional data about them like their latest version.

    The `ChannelData` struct represents the data found within the `channeldata.json` file. The
    `ChannelDataPackage` contains information about a package.

    Note that certain aspects of `ChannelData` are broken (e.g. run_exports is only available for a
    single package variant) and therefore the `ChannelData` struct is not really used much more.
    """

    channeldata_version: int
    "The version of the channeldata format"
    packages: dict[PackageNameStr, ChannelDataPackage]
    "The packages available in the channel, grouped by name"
    subdirs: Iterable[str]
    "The subdirs available in the channel"
