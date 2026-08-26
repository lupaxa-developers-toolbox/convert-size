"""Convert sizes between units in one family."""

from __future__ import annotations

from .constants import (
    BITS_PER_BIT,
    BITS_PER_BYTE,
    BITS_PER_NIBBLE,
    IEC_SCALER,
    SI_SCALER,
    SIZE_CODES_IEC,
    SIZE_CODES_IEC_BITS,
    SIZE_CODES_NIBBLE,
    SIZE_CODES_SI,
    SIZE_CODES_SI_BITS,
)
from .lookup import UnitKind, resolve_unit

BITS_FOR_KIND: dict[UnitKind, int] = {
    "bit": BITS_PER_BIT,
    "nibble": BITS_PER_NIBBLE,
    "byte": BITS_PER_BYTE,
}


def scale_size(
    size: float,
    scaler: int,
    start_index: int,
    end_index: int,
) -> float:
    """Scale *size* from *start_index* to *end_index* using *scaler*."""
    if end_index > start_index:
        for _ in range(end_index - start_index):
            size /= scaler
    else:
        for _ in range(start_index - end_index):
            size *= scaler
    return size


def convert_in_family(
    size: float,
    start_unit: str,
    end_unit: str,
    scaler: int,
    byte_codes: tuple[str, ...],
    bit_codes: tuple[str, ...],
) -> float:
    """Convert *size* between byte, nibble, and bit units that share *scaler*."""
    if size == 0:
        return 0.0

    start_index, start_kind = resolve_unit(
        start_unit,
        byte_codes,
        bit_codes,
        SIZE_CODES_NIBBLE,
    )
    end_index, end_kind = resolve_unit(
        end_unit,
        byte_codes,
        bit_codes,
        SIZE_CODES_NIBBLE,
    )

    bits = size
    for _ in range(start_index):
        bits *= scaler
    bits *= BITS_FOR_KIND[start_kind]
    bits /= BITS_FOR_KIND[end_kind]
    for _ in range(end_index):
        bits /= scaler
    return bits


def convert_size_iec(size: float, start_unit: str, end_unit: str) -> float:
    """Convert *size* between IEC byte, nibble, or bit units.

    Parameters
    ----------
    size
        Original size.
    start_unit
        Starting IEC abbreviation (``KiB``, ``nibble``, ``Kibit``, …).
    end_unit
        Target IEC abbreviation.

    Returns
    -------
    float
        Converted size.

    Raises
    ------
    ValueError
        If either unit abbreviation is not a valid IEC code.
    """
    return convert_in_family(
        size,
        start_unit,
        end_unit,
        IEC_SCALER,
        SIZE_CODES_IEC,
        SIZE_CODES_IEC_BITS,
    )


def convert_size_si(size: float, start_unit: str, end_unit: str) -> float:
    """Convert *size* between SI byte, nibble, or bit units.

    Parameters
    ----------
    size
        Original size.
    start_unit
        Starting SI abbreviation (``kB``, ``nibble``, ``kbit``, …).
    end_unit
        Target SI abbreviation.

    Returns
    -------
    float
        Converted size.

    Raises
    ------
    ValueError
        If either unit abbreviation is not a valid SI code.
    """
    return convert_in_family(
        size,
        start_unit,
        end_unit,
        SI_SCALER,
        SIZE_CODES_SI,
        SIZE_CODES_SI_BITS,
    )


def convert_size(
    size: float,
    start_unit: str,
    end_unit: str,
    si_units: bool = False,
) -> float:
    """Convert *size* between IEC or SI units.

    Parameters
    ----------
    size
        Original size.
    start_unit
        Starting unit abbreviation.
    end_unit
        Target unit abbreviation.
    si_units
        If True, use SI (1000); otherwise use IEC (1024).

    Returns
    -------
    float
        Converted size.

    Raises
    ------
    ValueError
        If either unit abbreviation is not valid for the selected family.
    """
    if si_units:
        return convert_size_si(size, start_unit, end_unit)
    return convert_size_iec(size, start_unit, end_unit)
