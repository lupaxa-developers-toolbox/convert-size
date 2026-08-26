"""Public export surface."""

from __future__ import annotations

import lupaxa.convert_size as convert_size


def test_public_names_are_exported() -> None:
    for name in (
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
    ):
        assert hasattr(convert_size, name)
        assert name in convert_size.__all__
