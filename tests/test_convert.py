"""Size conversion between IEC and SI units."""

from __future__ import annotations

import pytest

from lupaxa.convert_size import convert_size, convert_size_iec, convert_size_si


def test_iec_up_and_down() -> None:
    assert convert_size_iec(1024, "B", "KiB") == 1.0
    assert convert_size_iec(1, "MiB", "KiB") == 1024.0
    assert convert_size_iec(1, "GiB", "B") == 1024**3
    assert convert_size_iec(1, "RiB", "YiB") == 1024.0
    assert convert_size_iec(1, "QiB", "RiB") == 1024.0


def test_si_up_and_down() -> None:
    assert convert_size_si(1000, "B", "kB") == 1.0
    assert convert_size_si(1, "MB", "kB") == 1000.0
    assert convert_size_si(1, "GB", "B") == 1000**3
    assert convert_size_si(1, "RB", "YB") == 1000.0
    assert convert_size_si(1, "QB", "RB") == 1000.0


def test_convert_size_dispatches_families() -> None:
    assert convert_size(2048, "B", "KiB") == 2.0
    assert convert_size(2000, "B", "kB", si_units=True) == 2.0


def test_iec_and_si_differ_for_same_step() -> None:
    iec = convert_size(1, "MiB", "B")
    si = convert_size(1, "MB", "B", si_units=True)
    assert iec == 1024**2
    assert si == 1000**2
    assert iec != si


def test_same_unit_is_identity() -> None:
    assert convert_size_iec(42.5, "GiB", "GiB") == 42.5
    assert convert_size_si(7, "TB", "tb") == 7


def test_zero_short_circuits() -> None:
    assert convert_size_iec(0, "QiB", "B") == 0.0
    assert convert_size_si(0, "QB", "B") == 0.0
    assert convert_size(0, "MiB", "KiB") == 0.0


def test_case_insensitive_units() -> None:
    assert convert_size(1024, "kib", "mib") == 1.0
    assert convert_size(1000, "kb", "mb", si_units=True) == 1.0
    assert convert_size(1000, "KB", "MB", si_units=True) == 1.0


def test_invalid_start_unit_raises() -> None:
    with pytest.raises(ValueError, match="Invalid unit type"):
        convert_size_iec(1, "kB", "MiB")


def test_invalid_end_unit_raises() -> None:
    with pytest.raises(ValueError, match="valid options are"):
        convert_size(1, "MB", "MiB", si_units=True)


def test_iec_bit_conversion() -> None:
    assert convert_size_iec(1024, "bit", "Kibit") == 1.0
    assert convert_size_iec(1, "Gibit", "Mibit") == 1024.0
    assert convert_size_iec(1, "Qibit", "Ribit") == 1024.0


def test_si_bit_conversion() -> None:
    assert convert_size_si(1000, "bit", "kbit") == 1.0
    assert convert_size_si(1, "Gbit", "Mbit") == 1000.0
    assert convert_size_si(1, "Qbit", "Rbit") == 1000.0


def test_iec_bits_and_bytes() -> None:
    assert convert_size_iec(8, "bit", "B") == 1.0
    assert convert_size_iec(1, "B", "bit") == 8.0
    assert convert_size_iec(1, "KiB", "Kibit") == 8.0
    assert convert_size_iec(8, "Kibit", "KiB") == 1.0


def test_si_bits_and_bytes() -> None:
    assert convert_size_si(8, "bit", "B") == 1.0
    assert convert_size_si(1, "kB", "kbit") == 8.0
    assert convert_size(1, "MB", "Mbit", si_units=True) == 8.0


def test_nibble_conversion() -> None:
    assert convert_size_iec(4, "bit", "nibble") == 1.0
    assert convert_size_iec(1, "nibble", "bit") == 4.0
    assert convert_size_iec(2, "nibble", "B") == 1.0
    assert convert_size_iec(1, "B", "nibble") == 2.0
    assert convert_size_si(1, "kB", "nibble") == 2000.0
    assert convert_size(1, "nibble", "nibble") == 1.0
