"""
Schemas for the files shipped in the `info/` directory in each package.
"""

from typing import Any

from pydantic import AnyUrl, PositiveInt

from ._base import ExtrasForbiddenModel
from .types import (
    BuildNumber,
    BuildStr,
    MD5Str,
    NameVersionBuildMatchSpecStr,
    NonEmptyStr,
    PackageFileNameStr,
    PackageNameStr,
    PathsDataV1,
    ResolvedNameVersionBuildStr,
    RunExportsDict,
    SHA256Str,
    SubdirStr,
    VersionStr,
)


class InfoAbout(ExtrasForbiddenModel):
    channels: list[AnyUrl] = []
    conda_build_version: NonEmptyStr | None = None
    conda_version: NonEmptyStr | None = None
    description: str = ""
    dev_url: AnyUrl | None = None
    doc_url: AnyUrl | None = None
    env_vars: dict[NonEmptyStr, str] = {}
    extra: dict[NonEmptyStr, Any] = {}
    home: AnyUrl | None = None
    identifiers: list[str] = []
    keywords: list[str] = []
    license: NonEmptyStr = ...
    license_file: NonEmptyStr = ...
    root_pkgs: list[ResolvedNameVersionBuildStr]
    summary: str = ""
    tags: list[str] = []


class InfoIndex(ExtrasForbiddenModel):
    arch: NonEmptyStr = ...
    build: BuildStr = ...
    build_number: BuildNumber = ...
    constrains: list[NameVersionBuildMatchSpecStr] = []
    depends: list[NameVersionBuildMatchSpecStr] = []
    license: NonEmptyStr = ...
    name: PackageNameStr = ...
    platform: NonEmptyStr = ...
    subdir: SubdirStr = ...
    timestamp: PositiveInt = 0
    version: VersionStr = ...


class InfoRepodataRecord(InfoIndex):
    channel: AnyUrl = ...
    fn: PackageFileNameStr = ...
    md5: MD5Str = ...
    sha256: SHA256Str = ...
    size: PositiveInt = ...
    url: AnyUrl = ...


InfoHashInput = dict[NonEmptyStr, str]
InfoPaths = PathsDataV1
InfoRunExports = RunExportsDict
InfoTestTimeDependencies = list[NameVersionBuildMatchSpecStr]
