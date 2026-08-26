"""Unit name lookups."""

from __future__ import annotations

import pytest

from lupaxa.convert_size import (
    get_name_from_code,
    get_name_from_code_iec,
    get_name_from_code_si,
)


def test_iec_name_lookup() -> None:
    assert get_name_from_code_iec("KiB") == "Kibibyte"
    assert get_name_from_code_iec("mib") == "Mebibyte"
    assert get_name_from_code("YiB") == "Yobibyte"
    assert get_name_from_code_iec("RiB") == "Robibyte"
    assert get_name_from_code("qib") == "Quebibyte"


def test_si_name_lookup() -> None:
    assert get_name_from_code_si("kB") == "Kilobyte"
    assert get_name_from_code_si("KB") == "Kilobyte"
    assert get_name_from_code_si("gb") == "Gigabyte"
    assert get_name_from_code("MB", si_units=True) == "Megabyte"
    assert get_name_from_code_si("RB") == "Ronnabyte"
    assert get_name_from_code("qb", si_units=True) == "Quettabyte"


def test_bit_name_lookup() -> None:
    assert get_name_from_code_iec("bit") == "Bit"
    assert get_name_from_code_iec("Kibit") == "Kibibit"
    assert get_name_from_code("qibit") == "Quebibit"
    assert get_name_from_code_si("kbit") == "Kilobit"
    assert get_name_from_code("Mbit", si_units=True) == "Megabit"
    assert get_name_from_code_si("Qbit") == "Quettabit"


def test_nibble_name_lookup() -> None:
    assert get_name_from_code_iec("nibble") == "Nibble"
    assert get_name_from_code_si("NIBBLE") == "Nibble"


def test_byte_name_is_shared() -> None:
    assert get_name_from_code_iec("B") == "Byte"
    assert get_name_from_code_si("b") == "Byte"


def test_invalid_iec_name_raises() -> None:
    with pytest.raises(ValueError, match="Invalid unit type"):
        get_name_from_code_iec("kB")


def test_invalid_si_name_raises() -> None:
    with pytest.raises(ValueError, match="valid options are"):
        get_name_from_code("KiB", si_units=True)
