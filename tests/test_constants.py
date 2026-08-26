"""Unit tables stay paired and include the 2022 prefixes."""

from __future__ import annotations

from lupaxa.convert_size.constants import (
    BITS_PER_BYTE,
    BITS_PER_NIBBLE,
    IEC_SCALER,
    SI_SCALER,
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


def test_iec_tables_are_paired() -> None:
    assert len(SIZE_CODES_IEC) == len(SIZE_NAMES_IEC)
    assert SIZE_CODES_IEC[-2:] == ("RiB", "QiB")
    assert SIZE_NAMES_IEC[-2:] == ("Robibyte", "Quebibyte")


def test_si_tables_are_paired() -> None:
    assert len(SIZE_CODES_SI) == len(SIZE_NAMES_SI)
    assert SIZE_CODES_SI[1] == "kB"
    assert SIZE_CODES_SI[-2:] == ("RB", "QB")
    assert SIZE_NAMES_SI[-2:] == ("Ronnabyte", "Quettabyte")


def test_iec_bit_tables_are_paired() -> None:
    assert len(SIZE_CODES_IEC_BITS) == len(SIZE_NAMES_IEC_BITS)
    assert SIZE_CODES_IEC_BITS[:2] == ("bit", "Kibit")
    assert SIZE_CODES_IEC_BITS[-2:] == ("Ribit", "Qibit")
    assert SIZE_NAMES_IEC_BITS[-2:] == ("Robibit", "Quebibit")


def test_si_bit_tables_are_paired() -> None:
    assert len(SIZE_CODES_SI_BITS) == len(SIZE_NAMES_SI_BITS)
    assert SIZE_CODES_SI_BITS[:2] == ("bit", "kbit")
    assert SIZE_CODES_SI_BITS[-2:] == ("Rbit", "Qbit")
    assert SIZE_NAMES_SI_BITS[-2:] == ("Ronnabit", "Quettabit")


def test_nibble_table() -> None:
    assert SIZE_CODES_NIBBLE == ("nibble",)
    assert SIZE_NAMES_NIBBLE == ("Nibble",)


def test_scalers() -> None:
    assert IEC_SCALER == 1024
    assert SI_SCALER == 1000
    assert BITS_PER_BYTE == 8
    assert BITS_PER_NIBBLE == 4
    assert BITS_PER_BYTE == 2 * BITS_PER_NIBBLE
