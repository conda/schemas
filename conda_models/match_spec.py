"""
A [`MatchSpec`] is, fundamentally, a query language for conda packages. Any of the fields that
comprise a [`crate::PackageRecord`] can be used to compose a [`MatchSpec`].

[`MatchSpec`] can be composed with keyword arguments, where keys are any of the attributes of
[`crate::PackageRecord`]. Values for keyword arguments are the exact values the attribute should
match against. Many fields can also be matched against non-exact values -- by including wildcard
`*` and `>`/`<` ranges--where supported. Any non-specified field is the equivalent of a full
wildcard match.

MatchSpecs can also be composed using a single positional argument, with optional keyword
arguments. Keyword arguments also override any conflicting information provided in the positional
argument. Conda has historically had several string representations for equivalent MatchSpecs.

A series of rules are now followed for creating the canonical string representation of a MatchSpec
instance. The canonical string representation can generically be represented by

(channel(/subdir):(namespace):)name(version(build))[key1=value1,key2=value2]

where `()` indicate optional fields.

The rules for constructing a canonical string representation are:

1. `name` (i.e. "package name") is required, but its value can be '*'. Its position is always
   outside the key-value brackets.
2. If `version` is an exact version, it goes outside the key-value brackets and is prepended by
   `==`. If `version` is a "fuzzy" value (e.g. `1.11.*`), it goes outside the key-value brackets
   with the `.*` left off and is prepended by `=`. Otherwise `version` is included inside key-value
   brackets.
3. If `version` is an exact version, and `build` is an exact value, `build` goes outside key-value
   brackets prepended by a `=`.  Otherwise, `build` goes inside key-value brackets. `build_string`
   is an alias for `build`.
4. The `namespace` position is being held for a future feature. It is currently ignored.
5. If `channel` is included and is an exact value, a `::` separator is used between `channel` and
   `name`.  `channel` can either be a canonical channel name or a channel url.  In the canonical
   string representation, the canonical channel name will always be used.
6. If `channel` is an exact value and `subdir` is an exact value, `subdir` is appended to `channel`
   with a `/` separator.  Otherwise, `subdir` is included in the key-value brackets.
7. Key-value brackets can be delimited by comma, space, or comma+space.  Value can optionally be
   wrapped in single or double quotes, but must be wrapped if `value` contains a comma, space, or
   equal sign.  The canonical format uses comma delimiters and single quotes.
8. When constructing a `MatchSpec` instance from a string, any key-value pair given inside the
   key-value brackets overrides any matching parameter given outside the brackets.

When `MatchSpec` attribute values are simple strings, the are interpreted using the following
conventions:
  - If the string begins with `^` and ends with `$`, it is converted to a regex.
  - If the string contains an asterisk (`*`), it is transformed from a glob to a regex.
  - Otherwise, an exact match to the string is sought.

To fully-specify a package with a full, exact spec, the following fields must be given as exact
values:

  - channel
  - subdir
  - name
  - version
  - build

In the future, the namespace field might be added to this list.

Alternatively, an exact spec is given by
`*[sha256=01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b]`.
"""
from typing import Literal, Optional, Union

from ._base import ExtrasForbiddenModel
from .types import (
    BuildSpecStr,
    MD5Str,
    PackageFileNameStr,
    PackageNameStr,
    SHA256Str,
    SubdirStr,
    VersionSpecStr,
)


class MatchSpec(ExtrasForbiddenModel):
    """
    TODO: In theory, any PackageRecord (scalar) keys should be admitted here.
    """
    name: Optional[Union[PackageNameStr, Literal["*"]]] = None
    "The name of the package"
    version: Optional[VersionSpecStr] = None
    "The version spec of the package (e.g. `1.2.3`, `>=1.2.3`, `1.2.*`)"
    build: Optional[BuildSpecStr] = None
    "The build string of the package (e.g. `py37_0`, `py37h6de7cb9_0`, `py*`)"
    build_number: Optional[int] = None
    "The build number of the package"
    file_name: Optional[PackageFileNameStr] = None
    "Match the specific filename of the package"
    channel: Optional[str] = None
    "The channel of the package"
    subdir: Optional[SubdirStr] = None
    "The subdir of the channel"
    namespace: Optional[str] = None
    "The namespace of the package (currently not used)"
    md5: Optional[MD5Str] = None
    "The MD5 hash of the package archive"
    sha256: Optional[SHA256Str] = None
    "The SHA256 hash of the package archive"

    @classmethod
    def from_str(cls, value: str):
        raise NotImplementedError
