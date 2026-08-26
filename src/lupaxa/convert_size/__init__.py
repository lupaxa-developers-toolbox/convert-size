"""lupaxa.convert_size — IEC and SI file-size conversion."""

from __future__ import annotations

from .constants import (
    BITS_PER_BYTE,
    BITS_PER_NIBBLE,
    SIZE_CODES_IEC,
    SIZE_CODES_IEC_BITS,
    SIZE_CODES_NIBBLE,
    SIZE_CODES_SI,
    SIZE_CODES_SI_BITS,
    SIZE_NAMES_IEC,
    SIZE_NAMES_IEC_BITS,
    SIZE_NAMES_NIBBLE,
    SIZE_NAMES_SI,
    SIZE_NAMES_SI_BITS,
)
from .convert import convert_size, convert_size_iec, convert_size_si
from .names import get_name_from_code, get_name_from_code_iec, get_name_from_code_si
from .version import __version__, get_version

__all__ = [
    "BITS_PER_BYTE",
    "BITS_PER_NIBBLE",
    "SIZE_CODES_IEC",
    "SIZE_CODES_IEC_BITS",
    "SIZE_CODES_NIBBLE",
    "SIZE_CODES_SI",
    "SIZE_CODES_SI_BITS",
    "SIZE_NAMES_IEC",
    "SIZE_NAMES_IEC_BITS",
    "SIZE_NAMES_NIBBLE",
    "SIZE_NAMES_SI",
    "SIZE_NAMES_SI_BITS",
    "__version__",
    "convert_size",
    "convert_size_iec",
    "convert_size_si",
    "get_name_from_code",
    "get_name_from_code_iec",
    "get_name_from_code_si",
    "get_version",
]
