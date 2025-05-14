"""
WIP
"""

from collections.abc import Iterable
from typing import Annotated, Literal

from pydantic import AnyUrl, Field, PositiveInt

from ._base import ExtrasForbiddenModel
from .types import (
    BuildStr,
    EntryPointStr,
    MD5Str,
    NameVersionBuildMatchSpecStr,
    NoarchStr,
    NonEmptyStr,
    PackageNameStr,
    RunExports,
    SHA1Str,
    SHA256Str,
    VersionStr,
)


class _Package(ExtrasForbiddenModel):
    name: PackageNameStr
    version: VersionStr


class _Source(ExtrasForbiddenModel):
    fn: str = None
    url: AnyUrl | Iterable[AnyUrl] = None
    md5: MD5Str = None
    sha1: SHA1Str = None
    sha256: SHA256Str = None
    path: NonEmptyStr = None
    git_url: NonEmptyStr = None
    "URL or (relative) path to git repository"
    git_tag: NonEmptyStr = None
    git_branch: NonEmptyStr = None
    git_rev: NonEmptyStr = None
    git_depth: int = -1
    hg_url: NonEmptyStr = None
    hg_tag: NonEmptyStr = None
    svn_url: NonEmptyStr = None
    svn_rev: NonEmptyStr = None
    svn_ignore_externals: bool = False
    svn_username: NonEmptyStr = None
    svn_password: NonEmptyStr = None
    folder: NonEmptyStr = None
    patches: Iterable[NonEmptyStr] = None
    no_hoist: bool = None  # ???
    "UNDOCUMENTED"
    path_via_symlink: str = None  # ???
    "UNDOCUMENTED"


class _Build(ExtrasForbiddenModel):
    number: PositiveInt = 0
    "Identifier for subsequent builds of the same version."
    string: BuildStr = None
    """
    Third field in the final package filename.
    Usually automatically generated from the build number and package contents.
    """
    entry_points: Iterable[EntryPointStr] = None
    """
    List of Python entry points to be generated when the package is installed.
    """
    osx_is_app: bool = False
    "Make entry points use python.app instead of Python in macOS"
    track_features: Iterable[NonEmptyStr] = None
    """
    Adding track_features to one or more of the package variants will cause conda to de-prioritize
    it or "weigh it down". The lowest priority package is the one that would cause the most
    track_features to be activated in the environment. The default package among many variants is
    the one that would cause the least track_features to be activated.

    No two packages in a given subdir should ever have the same track_feature.
    """
    preserve_egg_dir: bool = False
    "Needed for some packages that use features specific to setuptools."
    no_link: Iterable[NonEmptyStr] = None
    "A list of globs for files that should always be copied and never soft linked or hard linked."
    binary_relocation: bool = True
    """
    Whether binary files should be made relocatable using install_name_tool on macOS or patchelf on
    Linux. The default is True. It also accepts False, which indicates no relocation for any files,
    or a list of files, which indicates relocation only for listed files.
    """
    script: NonEmptyStr | Iterable[NonEmptyStr] = None
    """
    Used instead of build.sh or bld.bat. For short build scripts, this can be more convenient. You
    may need to use selectors to use different scripts for different platforms.
    """
    noarch: NoarchStr = None
    "Make this package noarch (architecture independent)."
    noarch_python: bool = False
    "DEPRECATED. Use 'noarch: python' instead."
    has_prefix_files: None
    """
    Text files (files containing no NULL bytes) may contain the build prefix and need it replaced
    with the install prefix at installation time. Conda will automatically register such files.
    Binary files that contain the build prefix are generally handled differently (see
    'binary_has_prefix_files') but there may be cases where such a binary file needs to be treated
    as an ordinary text file, in which case they need to be identified.
    """
    binary_has_prefix_files: Iterable[NonEmptyStr] = None
    """
    By default, conda-build tries to detect prefixes in all files. You may also elect to specify
    files with binary prefixes individually. This allows you to specify the type of file as binary,
    when it may be incorrectly detected as text for some reason. Binary files are those containing
    NULL bytes
    """
    ignore_prefix_files: bool | Iterable[NonEmptyStr] = None
    """
    Used to exclude some or all of the files in the build recipe from the list of files that have
    the build prefix replaced with the install prefix. Use 'True' to ignore all files, or a list of
    paths to specify individual filenames. This setting is independent of RPATH replacement. Use
    the 'detect_binary_files_with_prefix' setting to control that behavior.
    """
    detect_binary_files_with_prefix: bool = True
    """
    Binary files may contain the build prefix and need it replaced with the install prefix at
    installation time. Conda can automatically identify and register such files.
    """
    skip_compile_pyc: Iterable[NonEmptyStr] = None
    """
    List of globs that will not be compiled to bytecode.
    """
    rpaths: Iterable[NonEmptyStr] = ("lib/",)
    """
    Set which RPATHs are used when making executables relocatable on Linux. This is a Linux feature
    that is ignored on other systems. The default is lib/.
    """
    script_env: Iterable[
        Annotated[str, Field(min_length=3, pattern=r"[A-z0-9_]+(=.+)?")]
    ] = None
    """
    Allow these environment variables to be seen by the build process. You can also (re)define
    their values with the `NAME=VAR` syntax.
    """
    always_include_files: Iterable[NonEmptyStr] = None
    """
    Force files to always be included, even if they are already in the environment from the build
    dependencies. This may be needed, for example, to create a recipe for conda itself.
    """
    skip: bool = False
    """
    Specifies whether conda-build should skip the build of this recipe. Particularly useful for
    defining recipes that are platform specific, thanks to selectors.
    """
    pin_depends: Literal["record", "strict"] = None
    """
    EXPERIMENTAL. Enforce pinning behaviour on the output recipe or built package.

    With a value of record, conda-build will record all requirements exactly as they would be
    installed in a file called info/requires. These pins will not show up in the output of conda
    render and they will not affect the actual run dependencies of the output package. It is only
    adding in this new file.

    With a value of strict, conda-build applies the pins to the actual metadata. This does affect
    the output of conda render and also affects the end result of the build. The package
    dependencies will be strictly pinned down to the build string level. This will supersede any
    dynamic or compatible pinning that conda-build may otherwise be doing.
    """
    include_recipe: bool = True
    """
    The full conda-build recipe and rendered meta.yaml file is included in the Package metadata by
    default. You can disable it here.
    """
    run_exports: RunExports = None
    """
    List of packages that will be injected as a runtime dependency in other recipes.
    Use the 'strong' key to indicate which dependencies will be injected when this package is used
    as a build dependency. Use 'weak' for dependencies that will be injected when this package is
    used as a host dependency. If you do not specify a category and just write a list of packages,
    'weak' is assumed.
    """
    ignore_run_exports: Iterable[PackageNameStr] = None
    "Ignore these injected run exports, regardless the origin."
    ignore_run_exports_from: Iterable[PackageNameStr] = None
    "Ignore the injected run exports coming from these packages."
    force_use_keys: Iterable[PackageNameStr] = None
    "Ensure these packages are considered for the build hash"
    force_ignore_keys: Iterable[PackageNameStr] = None
    "Ensure these packages are NOT considered for the build hash"
    merge_build_host: bool = False
    "Whether to merge the build and host dependencies into a single environment."
    missing_dso_whitelist: Iterable[NonEmptyStr] = None
    """
    List of globs for dynamic shared object (DSO) files that should be ignored when examining
    linkage information.
    """
    overlinking_ignore_patterns: Iterable[NonEmptyStr] = None
    """
    Used to ignore patterns of files for the overlinking and overdepending checks. This is
    sometimes useful to speed up builds that have many files (large repackage jobs) or builds where
    you know only a small fraction of the files should be checked.

    Glob patterns are allowed here, but mind your quoting, especially with leading wildcards.

    Use this sparingly, as the overlinking checks generally do prevent you from making mistakes.
    """
    runpath_whitelist: Iterable[NonEmptyStr] = None
    """
    List of globs for paths which are allowed to appear as runpaths in the package's shared
    libraries. All other runpaths will cause a warning message to be printed during the build.
    """
    activate_in_script: bool = True
    "UNDOCUMENTED. Whether the environments should be activated before the build script runs."
    # These are mentioned in conda_build.metadata.FIELDS but not documented?
    disable_pip: bool = False
    "UNDOCUMENTED."
    error_overdepending: None
    "UNDOCUMENTED."
    error_overlinking: None
    "UNDOCUMENTED."
    features: Iterable[NonEmptyStr] = None
    "DEPRECATED."
    msvc_compiler: str
    "UNDOCUMENTED."
    noarch_python_build_age: int = None
    "UNDOCUMENTED."
    no_move_top_level_workdir_loops: bool = None
    "UNDOCUMENTED."
    postlink: str
    "UNDOCUMENTED."
    preferred_env_executable_paths: list
    "UNDOCUMENTED."
    preferred_env: str
    "UNDOCUMENTED."
    prelink: str
    "UNDOCUMENTED."
    preunlink: str
    "UNDOCUMENTED."
    provides_features: dict
    "UNDOCUMENTED."
    requires_features: dict
    "UNDOCUMENTED."
    rpaths_patcher: None
    "UNDOCUMENTED."


class _Requirements(ExtrasForbiddenModel):
    """
    Specifies the build and runtime requirements. Dependencies of these requirements are included
    automatically.
    """

    build: Iterable[NameVersionBuildMatchSpecStr] = None
    """
    Tools required to build the package. These packages are run on the build system and include
    things such as revision control systems (Git, SVN) make tools (GNU make, Autotool, CMake) and
    compilers (real cross, pseudo-cross, or native when not cross-compiling), and any source
    pre-processors.

    Packages which provide "sysroot" files, like the CDT packages (see below) also belong in the
    build section.
    """
    host: Iterable[NameVersionBuildMatchSpecStr] = None
    """
    Packages that need to be specific to the target platform when the target platform is not
    necessarily the same as the native build platform.

    For example, in order for a recipe to be "cross-capable", shared libraries requirements must be
    listed in the host section, rather than the build section, so that the shared libraries that
    get linked are ones for the target platform, rather than the native build platform.

    You should also include the base interpreter for packages that need one. In other words, a
    Python package would list 'python' here and an R package would list 'mro-base' or 'r-base'.
    """
    run: Iterable[NameVersionBuildMatchSpecStr] = None
    """
    Packages required to run the package. These are the dependencies that are installed
    automatically whenever the package is installed.
    """
    run_constrained: Iterable[NameVersionBuildMatchSpecStr] = None
    """
    Packages that are optional at runtime but must obey the supplied additional constraint if they
    are installed.
    """
    conflicts: Iterable[NameVersionBuildMatchSpecStr] = None
    "UNDOCUMENTED."


class _Test(ExtrasForbiddenModel):
    files: Iterable[NonEmptyStr] = None
    """
    Test files that are copied from the recipe into the temporary test directory and are needed
    during testing. If providing a path, forward slashes must be used. Allows globs.
    """
    source_files: Iterable[NonEmptyStr] = None
    """
    Test files that are copied from the source work directory into the temporary test directory and
    are needed during testing. Allows globs.
    """
    requires: Iterable[NameVersionBuildMatchSpecStr] = None
    """
    In addition to the runtime requirements, you can specify requirements needed during testing.
    The runtime requirements that you specified in the "run" section described above are
    automatically included during testing.
    """
    commands: Iterable[NonEmptyStr] = None
    """
    Shell commands that are run as part of the test.
    """
    imports: Iterable[Annotated[str, Field(pattern=r"[A-z0-9\._]+")]] = None
    """
    Python modules that will be imported as part of the test checks.
    """
    downstreams: Iterable[PackageNameStr] = None
    """
    Run the bundled test suite of the listed packages ensuring the package being built is used as
    a dependency.
    """


class _App(ExtrasForbiddenModel):
    """
    If the app section is present, the package is an app, meaning that it appears in Anaconda
    Navigator.
    """

    entry: NonEmptyStr = None
    "The command that is called to launch the app in Navigator."
    icon: NonEmptyStr = None
    "The icon file contained in the recipe."
    summary: NonEmptyStr = None
    "Summary of the package used in Navigator."
    own_environment: bool = False
    "Whether to install the app through Navigator into its own environment."
    type: NonEmptyStr = None
    "UNDOCUMENTED."
    cli_opts: NonEmptyStr = None
    "UNDOCUMENTED."


class _About(ExtrasForbiddenModel):
    home: NonEmptyStr = None
    dev_url: AnyUrl = None
    doc_url: AnyUrl = None
    doc_source_url: AnyUrl = None
    license_url: AnyUrl = None
    license: NonEmptyStr = None
    summary: NonEmptyStr = None
    description: NonEmptyStr = None
    license_family: NonEmptyStr = None
    identifiers: Iterable[NonEmptyStr] = None
    tags: Iterable[NonEmptyStr] = None
    keywords: Iterable[NonEmptyStr] = None
    license_file: NonEmptyStr | Iterable[NonEmptyStr] = None
    prelink_message: NonEmptyStr = None
    readme: NonEmptyStr | Iterable[NonEmptyStr] = None


class _OutputTest(ExtrasForbiddenModel):
    script: NonEmptyStr = None


_Extra = dict


class _Output(ExtrasForbiddenModel):
    name: PackageNameStr
    version: VersionStr
    number: PositiveInt
    entry_points: Iterable[EntryPointStr] = None
    script: NonEmptyStr = None
    "Script that will be run to prepare or distribute the files being packaged."
    script_interpreter: NonEmptyStr = None
    "Interpreter to use to run the script."
    files: Iterable[NonEmptyStr] = None
    "List of files to include in the package, run after 'script', if any."
    build: dict  # Is this really allowed / used ???
    requirements: Iterable[NameVersionBuildMatchSpecStr] | _Requirements = None
    run_exports: Iterable[NameVersionBuildMatchSpecStr] | RunExports = None
    test: _OutputTest = None
    type_: Literal["conda", "conda_v2", "wheel"] = Field("conda", alias="type")
    about: _About = None
    extra: _Extra = None
    target: NonEmptyStr = None
    "UNDOCUMENTED."


class MetaYaml(ExtrasForbiddenModel):
    package: _Package
    source: _Source | Iterable[_Source]
    build: _Build
    requirements: _Requirements
    test: _Test
    outputs: Iterable[_Output] = None
    about: _About = None
    app: _App = None
    extra: _Extra = None
