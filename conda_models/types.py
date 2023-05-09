"""
conda-specific constrains for scalar types.
"""
from enum import Enum, auto

from pydantic import conint, constr


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
    Linux64 = "linux-64"
    Linux32 = "linux-32"
    LinuxArmV6l = "linux-armv6l"
    LinuxArmV7l = "linux-armv7l"
    LinuxPPC64le = "linux-ppc64le"
    LinuxS390x = "linux-s390x"
    OSX64 = "osx-64"
    OSX32 = "osx-32"
    OSXArm64 = "osx-arm64"
    Win64 = "win-64"
    Win32 = "win-32"
    WinArm64 = "win-arm64"
    ZosZ = "zos-z"
    Noarch = "noarch"


class PackageType(str, Enum):
    pass


class Platform(str, Enum):
    pass


NaturalInt = conint(ge=0)
NonEmptyStr = constr(min_length=1)

package_name_regex = r"[0-9a-zA-Z\._-]+"
version_regex = r"([0-9]!)?[0-9a-z\._]+"
version_spec_regex = r"[0-9a-z<>=!\.\*]+"
build_string_regex = r"[0-9a-zA-Z\._]+"
build_string_spec_regex = r"[0-9a-zA-Z\._\*]+"

MD5Str = constr(min_length=32, max_length=32, regex=r"[a-fA-F0-9]{32}")
SHA256Str = constr(min_length=64, max_length=64, regex=r"[a-fA-F0-9]{64}")
MatchSpecStr = NonEmptyStr  # TODO: implement regex???
BuildStr = constr(min_length=1, regex=build_string_regex)
BuildSpecStr = constr(min_length=1, regex=build_string_spec_regex)
PackageNameStr = constr(min_length=1, regex=package_name_regex)
PackageFileNameStr = constr(
    min_length=1,
    regex=rf"({package_name_regex})-({version_regex})-({build_string_regex})\.(conda|tar\.bz2)",
)
TarBz2PackageFileNameStr = constr(
    min_length=1,
    regex=rf"({package_name_regex})-({version_regex})-({build_string_regex})\.tar\.bz2",
)
CondaPackageFileNameStr = constr(
    min_length=1,
    regex=rf"({package_name_regex})-({version_regex})-({build_string_regex})\.conda",
)
NameVersionBuildMatchSpecStr = constr(
    min_length=1,
    regex=rf"({package_name_regex})\s+("
    rf"({version_spec_regex})"
    rf"|({version_spec_regex})?\s+({build_string_spec_regex})"
    rf")?",
)
VersionStr = constr(min_length=1, regex=version_regex)
VersionSpecStr = constr(min_length=1, regex=version_spec_regex)
