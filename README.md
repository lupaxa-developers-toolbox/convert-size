<p align="center">
  <a href="https://github.com/lupaxa-developers-toolbox">
    <img src="https://raw.githubusercontent.com/the-lupaxa-project/brand-assets/master/logos/organisations/developers-toolbox/readme-logo.png" alt="Developers Toolbox" />
  </a>
</p>

<h1 align="center">Convert Size</h1>

Convert file sizes between IEC (binary, 1024) and SI (decimal, 1000)
units, including bits, nibbles, and bytes.

The PyPI name is `lupaxa-convert-size`. The import path is
`lupaxa.convert_size`. `lupaxa` is a namespace package — there is no
`lupaxa/__init__.py`.

## Install

```bash
pip install lupaxa-convert-size
```

Requires Python 3.10+. There are no runtime dependencies.

From a clone of this repository (editable install):

```bash
make init
make python-install-dev
```

## Usage

`convert-size` is a library only. There is no console script and no
`python -m` entry point.

A walkthrough of the same API lives in `demo.py` at the repository
root (not shipped in the wheel):

```bash
python demo.py
```

### Convert a size

`convert_size()` is the usual entry point. It uses IEC units unless
`si_units=True`.

```python
from lupaxa.convert_size import convert_size

convert_size(4096, "B", "KiB")
# 4.0

convert_size(1.5, "MiB", "KiB")
# 1536.0

convert_size(2500, "B", "kB", si_units=True)
# 2.5
```

Dedicated helpers skip the flag:

```python
from lupaxa.convert_size import convert_size_iec, convert_size_si

convert_size_iec(1, "TiB", "GiB")
convert_size_si(1, "TB", "GB")
```

A size of `0` returns `0.0` without looking up the units.

### Bits, nibbles, and bytes

Within one family, bit, nibble, and byte codes convert through 8 bits
per byte and 4 bits per nibble:

```python
convert_size(8, "bit", "B")
# 1.0

convert_size(1, "B", "nibble")
# 2.0

convert_size(4, "bit", "nibble")
# 1.0

convert_size(1, "KiB", "Kibit")
# 8.0

convert_size(1, "kB", "kbit", si_units=True)
# 8.0
```

`nibble` has no SI or IEC prefixes. It is valid in both families.

### Look up a unit name

```python
from lupaxa.convert_size import get_name_from_code

get_name_from_code("KiB")
# "Kibibyte"

get_name_from_code("kB", si_units=True)
# "Kilobyte"

get_name_from_code("Kibit")
# "Kibibit"
```

Codes are matched case-insensitively (`kib`, `KIB`, and `KiB` are the
same). The stored SI kilo symbol is `kB`, which is the SI spelling.

```python
convert_size(1, "gib", "mib")
convert_size(1, "tb", "gb", si_units=True)
```

### Invalid units

Unknown abbreviations raise `ValueError` and list the valid codes for
that family. `kB` is not valid in IEC mode; `KiB` is not valid in SI
mode.

```python
convert_size(1, "kB", "MB")
# ValueError: Invalid unit type kB, valid options are: B, KiB, MiB, ...
```

### Constants

The unit tables are exported if you need to iterate them:

```python
from lupaxa.convert_size import SIZE_CODES_IEC, SIZE_CODES_IEC_BITS, SIZE_CODES_SI

list(SIZE_CODES_IEC)
list(SIZE_CODES_IEC_BITS)
list(SIZE_CODES_SI)
```

## Unit families

| Family | Kind   | Scaler | Abbreviations                                                                                   |
| ------ | ------ | ------ | ----------------------------------------------------------------------------------------------- |
| IEC    | bytes  | 1024   | `B`, `KiB`, `MiB`, `GiB`, `TiB`, `PiB`, `EiB`, `ZiB`, `YiB`, `RiB`, `QiB`                       |
| IEC    | bits   | 1024   | `bit`, `Kibit`, `Mibit`, `Gibit`, `Tibit`, `Pibit`, `Eibit`, `Zibit`, `Yibit`, `Ribit`, `Qibit` |
| SI     | bytes  | 1000   | `B`, `kB`, `MB`, `GB`, `TB`, `PB`, `EB`, `ZB`, `YB`, `RB`, `QB`                                 |
| SI     | bits   | 1000   | `bit`, `kbit`, `Mbit`, `Gbit`, `Tbit`, `Pbit`, `Ebit`, `Zbit`, `Ybit`, `Rbit`, `Qbit`           |
| both   | nibble | —      | `nibble` (4 bits, half a byte)                                                                  |

Codes follow SI and IEC 80000-13: kilo is `kB` / `kbit`, not `KB`.
Lookup is case-insensitive, so `KB` still matches `kB`. `kB` is SI
only; `KiB` is IEC only. Eight bits are one byte and four bits are
one nibble, so a call may mix bit, nibble, and byte codes in the
same family. `nibble` has no prefixes and is valid in both families.

The 2022 prefixes are included: SI `RB` / `QB` / `Rbit` / `Qbit`
(ronna / quetta) and IEC `RiB` / `QiB` / `Ribit` / `Qibit` (robi /
quebi). Full names are `Ronnabyte`, `Quettabyte`, `Robibyte`, and
`Quebibyte` (and the matching `*bit` forms).

Public names are exported from `lupaxa.convert_size`:
`convert_size(size, start, end, si_units=False)`,
`convert_size_iec`, `convert_size_si`,
`get_name_from_code(unit, si_units=False)`,
`get_name_from_code_iec`, `get_name_from_code_si`,
`__version__` / `get_version()`, `BITS_PER_BYTE` (`8`),
`BITS_PER_NIBBLE` (`4`), and the `SIZE_CODES_*` / `SIZE_NAMES_*`
tables.

## Check

```bash
make init
make python-check
```

<a href="https://github.com/the-lupaxa-project">
    <img src="https://raw.githubusercontent.com/the-lupaxa-project/brand-assets/master/logos/components/footer-for-child-orgs.svg" alt="The Lupaxa Project Footer" width="100%" />
</a>
