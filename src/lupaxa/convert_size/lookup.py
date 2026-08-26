"""Case-insensitive lookup of unit codes."""

from __future__ import annotations

from typing import Literal

UnitKind = Literal["bit", "nibble", "byte"]


def in_tuple(item: str, stuff: tuple[str, ...]) -> bool:
    """Return True if *item* exists in *stuff*, case-insensitively."""
    return any(entry.lower() == item.lower() for entry in stuff)


def index_of(item: str, stuff: tuple[str, ...]) -> int:
    """Return the case-insensitive index of *item* in *stuff*.

    Raises
    ------
    ValueError
        If *item* is not found.
    """
    lowered = [entry.lower() for entry in stuff]
    try:
        return lowered.index(item.lower())
    except ValueError as err:
        raise ValueError(f"Item {item} not found in the provided tuple.") from err


def unit_index(unit: str, code_list: tuple[str, ...]) -> int:
    """Return the index of *unit* in *code_list*.

    Raises
    ------
    ValueError
        If *unit* is not a valid code in *code_list*.
    """
    if not in_tuple(unit, code_list):
        valid_types = ", ".join(code_list)
        raise ValueError(f"Invalid unit type {unit}, valid options are: {valid_types}")
    return index_of(unit, code_list)


def resolve_unit(
    unit: str,
    byte_codes: tuple[str, ...],
    bit_codes: tuple[str, ...],
    nibble_codes: tuple[str, ...],
) -> tuple[int, UnitKind]:
    """Return ``(index, kind)`` for *unit*.

    Raises
    ------
    ValueError
        If *unit* is not in any of the tables.
    """
    if in_tuple(unit, byte_codes):
        return index_of(unit, byte_codes), "byte"
    if in_tuple(unit, nibble_codes):
        return index_of(unit, nibble_codes), "nibble"
    if in_tuple(unit, bit_codes):
        return index_of(unit, bit_codes), "bit"
    valid_types = ", ".join((*byte_codes, *nibble_codes, *bit_codes))
    raise ValueError(f"Invalid unit type {unit}, valid options are: {valid_types}")
