"""IEC and SI unit tables and scalers."""

from __future__ import annotations

BITS_PER_BIT = 1
BITS_PER_NIBBLE = 4
BITS_PER_BYTE = 8

IEC_SCALER = 1024
SI_SCALER = 1000

SIZE_CODES_NIBBLE: tuple[str, ...] = ("nibble",)
SIZE_NAMES_NIBBLE: tuple[str, ...] = ("Nibble",)

SIZE_CODES_IEC: tuple[str, ...] = (
    "B",
    "KiB",
    "MiB",
    "GiB",
    "TiB",
    "PiB",
    "EiB",
    "ZiB",
    "YiB",
    "RiB",
    "QiB",
)
SIZE_NAMES_IEC: tuple[str, ...] = (
    "Byte",
    "Kibibyte",
    "Mebibyte",
    "Gibibyte",
    "Tebibyte",
    "Pebibyte",
    "Exbibyte",
    "Zebibyte",
    "Yobibyte",
    "Robibyte",
    "Quebibyte",
)

SIZE_CODES_IEC_BITS: tuple[str, ...] = (
    "bit",
    "Kibit",
    "Mibit",
    "Gibit",
    "Tibit",
    "Pibit",
    "Eibit",
    "Zibit",
    "Yibit",
    "Ribit",
    "Qibit",
)
SIZE_NAMES_IEC_BITS: tuple[str, ...] = (
    "Bit",
    "Kibibit",
    "Mebibit",
    "Gibibit",
    "Tebibit",
    "Pebibit",
    "Exbibit",
    "Zebibit",
    "Yobibit",
    "Robibit",
    "Quebibit",
)

SIZE_CODES_SI: tuple[str, ...] = (
    "B",
    "kB",
    "MB",
    "GB",
    "TB",
    "PB",
    "EB",
    "ZB",
    "YB",
    "RB",
    "QB",
)
SIZE_NAMES_SI: tuple[str, ...] = (
    "Byte",
    "Kilobyte",
    "Megabyte",
    "Gigabyte",
    "Terabyte",
    "Petabyte",
    "Exabyte",
    "Zettabyte",
    "Yottabyte",
    "Ronnabyte",
    "Quettabyte",
)

SIZE_CODES_SI_BITS: tuple[str, ...] = (
    "bit",
    "kbit",
    "Mbit",
    "Gbit",
    "Tbit",
    "Pbit",
    "Ebit",
    "Zbit",
    "Ybit",
    "Rbit",
    "Qbit",
)
SIZE_NAMES_SI_BITS: tuple[str, ...] = (
    "Bit",
    "Kilobit",
    "Megabit",
    "Gigabit",
    "Terabit",
    "Petabit",
    "Exabit",
    "Zettabit",
    "Yottabit",
    "Ronnabit",
    "Quettabit",
)
