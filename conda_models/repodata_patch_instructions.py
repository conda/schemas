"""
WIP
"""
from pydantic import Field

from ._base import ExtrasForbiddenModel
from .repodata import OptionalRepodataRecord
from .types import CondaPackageFileNameStr, PackageFileNameStr, TarBz2PackageFileNameStr


class RepodataPatchInstructions(ExtrasForbiddenModel):
    packages: dict[TarBz2PackageFileNameStr, OptionalRepodataRecord]
    "The .tar.bz2 packages in the repodata that will be patched"
    packages_conda: dict[CondaPackageFileNameStr, OptionalRepodataRecord] = Field(
        ...,
        alias="packages.conda",
    )
    "The .conda packages in the repodata that will be patched"
    remove: set[PackageFileNameStr]
    "The packages (conda or tar.bz2) that should be removed from the index"
    revoke: set[str]
    "DEPRECATED."
    patch_instructions_version: int
    "Version of the patch instructions schema"
