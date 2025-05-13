"""
conda-specific constrains for scalar types.
"""

from enum import Enum, auto
from typing import Annotated

from pydantic import AnyUrl, Field


class NoarchStr(str, Enum):
    Python = "python"
    """
    A noarch python package is a python package without any precompiled python files (`.pyc` or
    `__pycache__`). Normally these files are bundled with the package. However, these files are
    tied to a specific version of Python and must therefor be generated for every target
    platform and architecture. This complicates the build process.

    For noarch python packages these files are generated when installing the package by invoking
    the compilation process through the python binary that is installed in the same environment.

    This introductory blog post highlights some of specific of noarch python packages:
    <https://www.anaconda.com/blog/condas-new-noarch-packages>

    Or read the docs for more information:
    <https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/packages.html#noarch-python>
    """
    Generic = "generic"
    """
    Noarch generic packages allow users to distribute docs, datasets, and source code in conda
    packages.
    """


class NoarchType(str, Enum):
    GenericV1 = auto()
    "An old-format generic noarch package"
    GenericV2 = auto()
    "A new-format generic noarch package"
    Python = auto()
    "A noarch Python package"


class SubdirStr(str, Enum):
    # Value length MUST NOT exceed 32 characters
    EmscriptenWasm32 = "emscripten-wasm32"
    FreeBSD64 = "freebsd-64"
    Linux32 = "linux-32"
    Linux64 = "linux-64"
    LinuxArmV6l = "linux-armv6l"
    LinuxArmV7l = "linux-armv7l"
    LinuxPPC64le = "linux-ppc64le"
    LinuxS390x = "linux-s390x"
    OSX32 = "osx-32"
    OSX64 = "osx-64"
    OSXArm64 = "osx-arm64"
    WasiWasm32 = "wasi-wasm32"
    Win32 = "win-32"
    Win64 = "win-64"
    WinArm64 = "win-arm64"
    ZosZ = "zos-z"
    Noarch = "noarch"


class PackageType(str, Enum):
    pass


NonEmptyStr = Annotated[str, Field(min_length=1)]

package_name_regex = r"^(([a-z0-9])|([a-z0-9_](?!_)))[._-]?([a-z0-9]+(\.|-|_|$))*$"
virtual_package_name_regex = r"^__[a-z0-9][._-]?([a-z0-9]+(\.|-|_|$))*$"
version_regex = r"([0-9]!)?[0-9a-z\._]+"
version_spec_regex = r"[0-9a-z<>=!\.\*]+"
build_string_regex = r"^[a-zA-Z0-9_\.+]+$"
build_string_spec_regex = r"^[a-zA-Z0-9_\.+*]+$"
artifact_extension_regex = r"[a-z0-9](\.?[a-z0-9])*$"

MD5Str = Annotated[str, Field(min_length=32, max_length=32, pattern=r"[a-fA-F0-9]{32}")]
SHA1Str = Annotated[
    str, Field(min_length=40, max_length=40, pattern=r"[a-fA-F0-9]{40}")
]
SHA256Str = Annotated[
    str, Field(min_length=64, max_length=64, pattern=r"[a-fA-F0-9]{64}")
]
MatchSpecStr = NonEmptyStr  # TODO: implement regex???
BuildNumber = Annotated[int, Field(ge=0)]
BuildStr = Annotated[
    str, Field(min_length=1, max_length=64, pattern=build_string_regex)
]
BuildSpecStr = Annotated[
    str, Field(min_length=1, max_length=64, pattern=build_string_spec_regex)
]
PackageNameStr = Annotated[
    str, Field(min_length=1, max_length=64, pattern=package_name_regex)
]
PackageFileNameStr = Annotated[
    str,
    Field(
        min_length=1,
        max_length=211,
        pattern=rf"({package_name_regex})-({version_regex})-({build_string_regex})\.(conda|tar\.bz2)",
    ),
]
TarBz2PackageFileNameStr = Annotated[
    str,
    Field(
        min_length=1,
        max_length=211,
        pattern=rf"({package_name_regex})-({version_regex})-({build_string_regex})\.tar\.bz2",
    ),
]
CondaPackageFileNameStr = Annotated[
    str,
    Field(
        min_length=1,
        max_length=211,
        pattern=rf"({package_name_regex})-({version_regex})-({build_string_regex})\.conda",
    ),
]
NameVersionBuildMatchSpecStr = Annotated[
    str,
    Field(
        min_length=1,
        pattern=rf"({package_name_regex})\s+("
        rf"({version_spec_regex})"
        rf"|({version_spec_regex})?\s+({build_string_spec_regex})"
        rf")?",
    ),
]
VersionStr = Annotated[str, Field(min_length=1, max_length=64, pattern=version_regex)]
VersionSpecStr = Annotated[str, Field(min_length=1, pattern=version_spec_regex)]

EntryPointStr = Annotated[
    str, Field(min_length=5, pattern=r"\S+\s*=\s*[A-z0-9_\.]:[A-z0-9_]")
]

ChannelNameOrUrl = NonEmptyStr | AnyUrl
