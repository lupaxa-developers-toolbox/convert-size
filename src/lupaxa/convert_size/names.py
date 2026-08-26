"""Look up full unit names from abbreviations."""

from __future__ import annotations

from .constants import (
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
from .lookup import resolve_unit


def name_in_family(
    unit: str,
    byte_codes: tuple[str, ...],
    byte_names: tuple[str, ...],
    bit_codes: tuple[str, ...],
    bit_names: tuple[str, ...],
) -> str:
    """Return the full name for *unit* in the byte, nibble, or bit tables."""
    index, kind = resolve_unit(unit, byte_codes, bit_codes, SIZE_CODES_NIBBLE)
    if kind == "bit":
        return bit_names[index]
    if kind == "nibble":
        return SIZE_NAMES_NIBBLE[index]
    return byte_names[index]


def get_name_from_code_iec(unit: str) -> str:
    """Return the full IEC unit name for *unit*.

    Parameters
    ----------
    unit
        IEC abbreviation such as ``KiB``, ``nibble``, or ``Kibit``.

    Returns
    -------
    str
        Full name such as ``Kibibyte`` or ``Kibibit``.

    Raises
    ------
    ValueError
        If *unit* is not a valid IEC code.
    """
    return name_in_family(
        unit,
        SIZE_CODES_IEC,
        SIZE_NAMES_IEC,
        SIZE_CODES_IEC_BITS,
        SIZE_NAMES_IEC_BITS,
    )


def get_name_from_code_si(unit: str) -> str:
    """Return the full SI unit name for *unit*.

    Parameters
    ----------
    unit
        SI abbreviation such as ``kB``, ``nibble``, or ``kbit``.

    Returns
    -------
    str
        Full name such as ``Kilobyte`` or ``Kilobit``.

    Raises
    ------
    ValueError
        If *unit* is not a valid SI code.
    """
    return name_in_family(
        unit,
        SIZE_CODES_SI,
        SIZE_NAMES_SI,
        SIZE_CODES_SI_BITS,
        SIZE_NAMES_SI_BITS,
    )


def get_name_from_code(unit: str, si_units: bool = False) -> str:
    """Return the full unit name for *unit*.

    Parameters
    ----------
    unit
        Unit abbreviation.
    si_units
        If True, look up SI names; otherwise look up IEC names.

    Returns
    -------
    str
        Full unit name.

    Raises
    ------
    ValueError
        If *unit* is not valid for the selected family.
    """
    if si_units:
        return get_name_from_code_si(unit)
    return get_name_from_code_iec(unit)
