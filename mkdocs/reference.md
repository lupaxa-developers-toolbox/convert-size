# Reference

Public names are exported from `lupaxa.convert_size`.

## Package

| Name                                               | Description                          |
| -------------------------------------------------- | ------------------------------------ |
| `__version__`                                      | Package version string               |
| `get_version()`                                    | Return `__version__`                 |
| `convert_size(size, start, end, si_units=False)`   | Convert using IEC or SI              |
| `convert_size_iec(size, start, end)`               | Convert using IEC (1024)             |
| `convert_size_si(size, start, end)`                | Convert using SI (1000)              |
| `get_name_from_code(unit, si_units=False)`         | Full name for an abbreviation        |
| `get_name_from_code_iec(unit)`                     | Full IEC name                        |
| `get_name_from_code_si(unit)`                      | Full SI name                         |
| `BITS_PER_BYTE`                                    | `8`                                  |
| `BITS_PER_NIBBLE`                                  | `4`                                  |
| `SIZE_CODES_NIBBLE`                                | `nibble`                             |
| `SIZE_NAMES_NIBBLE`                                | `Nibble`                             |
| `SIZE_CODES_IEC`                                   | IEC byte abbreviations               |
| `SIZE_NAMES_IEC`                                   | IEC byte full names                  |
| `SIZE_CODES_IEC_BITS`                              | IEC bit abbreviations                |
| `SIZE_NAMES_IEC_BITS`                              | IEC bit full names                   |
| `SIZE_CODES_SI`                                    | SI byte abbreviations                |
| `SIZE_NAMES_SI`                                    | SI byte full names                   |
| `SIZE_CODES_SI_BITS`                               | SI bit abbreviations                 |
| `SIZE_NAMES_SI_BITS`                               | SI bit full names                    |

There is no console script and no `python -m lupaxa.convert_size` entry
point.

## IEC byte units

| Code  | Name      | Scaler from bytes |
| ----- | --------- | ----------------- |
| `B`   | Byte      | 1                 |
| `KiB` | Kibibyte  | 1024              |
| `MiB` | Mebibyte  | 1024²             |
| `GiB` | Gibibyte  | 1024³             |
| `TiB` | Tebibyte  | 1024⁴             |
| `PiB` | Pebibyte  | 1024⁵             |
| `EiB` | Exbibyte  | 1024⁶             |
| `ZiB` | Zebibyte  | 1024⁷             |
| `YiB` | Yobibyte  | 1024⁸             |
| `RiB` | Robibyte  | 1024⁹             |
| `QiB` | Quebibyte | 1024¹⁰            |

`RiB` / `QiB` are the 2022 IEC prefixes (robi / quebi).

## IEC bit units

| Code    | Name     | Scaler from bits |
| ------- | -------- | ---------------- |
| `bit`   | Bit      | 1                |
| `Kibit` | Kibibit  | 1024             |
| `Mibit` | Mebibit  | 1024²            |
| `Gibit` | Gibibit  | 1024³            |
| `Tibit` | Tebibit  | 1024⁴            |
| `Pibit` | Pebibit  | 1024⁵            |
| `Eibit` | Exbibit  | 1024⁶            |
| `Zibit` | Zebibit  | 1024⁷            |
| `Yibit` | Yobibit  | 1024⁸            |
| `Ribit` | Robibit  | 1024⁹            |
| `Qibit` | Quebibit | 1024¹⁰           |

## SI byte units

| Code | Name       | Scaler from bytes |
| ---- | ---------- | ----------------- |
| `B`  | Byte       | 1                 |
| `kB` | Kilobyte   | 1000              |
| `MB` | Megabyte   | 1000²             |
| `GB` | Gigabyte   | 1000³             |
| `TB` | Terabyte   | 1000⁴             |
| `PB` | Petabyte   | 1000⁵             |
| `EB` | Exabyte    | 1000⁶             |
| `ZB` | Zettabyte  | 1000⁷             |
| `YB` | Yottabyte  | 1000⁸             |
| `RB` | Ronnabyte  | 1000⁹             |
| `QB` | Quettabyte | 1000¹⁰            |

`kB` is the SI spelling (prefix `k`). `RB` / `QB` are the 2022 SI prefixes
(ronna / quetta).

## SI bit units

| Code   | Name      | Scaler from bits |
| ------ | --------- | ---------------- |
| `bit`  | Bit       | 1                |
| `kbit` | Kilobit   | 1000             |
| `Mbit` | Megabit   | 1000²            |
| `Gbit` | Gigabit   | 1000³            |
| `Tbit` | Terabit   | 1000⁴            |
| `Pbit` | Petabit   | 1000⁵            |
| `Ebit` | Exabit    | 1000⁶            |
| `Zbit` | Zettabit  | 1000⁷            |
| `Ybit` | Yottabit  | 1000⁸            |
| `Rbit` | Ronnabit  | 1000⁹            |
| `Qbit` | Quettabit | 1000¹⁰           |

Eight bits equal one byte and four bits equal one nibble when converting
between the bit, nibble, and byte tables of the same family.

## Nibble

| Code     | Name   | Relation          |
| -------- | ------ | ----------------- |
| `nibble` | Nibble | 4 bits / 0.5 byte |

`nibble` is valid in both IEC and SI mode. There are no prefixed nibble
units.

## Errors

| Condition                          | Exception    |
| ---------------------------------- | ------------ |
| Unknown unit for the chosen family | `ValueError` |
