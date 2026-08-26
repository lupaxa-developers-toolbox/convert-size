# convert-size

Convert file sizes between IEC (binary, 1024) and SI (decimal, 1000) units,
including bits, nibbles, and bytes.

Install the **`lupaxa-convert-size`** package and import
`lupaxa.convert_size`:

```bash
pip install lupaxa-convert-size
```

```python
from lupaxa.convert_size import convert_size, get_name_from_code

convert_size(1024, "B", "KiB")
# 1.0

convert_size(2000, "B", "kB", si_units=True)
# 2.0

convert_size(1, "KiB", "Kibit")
# 8.0

convert_size(1, "B", "nibble")
# 2.0

get_name_from_code("MiB")
# "Mebibyte"
```

`convert-size` is a library only. There is no console script and no
`python -m` entry point.

## Unit families

| Family | Kind    | Scaler | Abbreviations                                                                                   |
| ------ | ------- | ------ | ----------------------------------------------------------------------------------------------- |
| IEC    | bytes   | 1024   | `B`, `KiB`, `MiB`, `GiB`, `TiB`, `PiB`, `EiB`, `ZiB`, `YiB`, `RiB`, `QiB`                       |
| IEC    | bits    | 1024   | `bit`, `Kibit`, `Mibit`, `Gibit`, `Tibit`, `Pibit`, `Eibit`, `Zibit`, `Yibit`, `Ribit`, `Qibit` |
| SI     | bytes   | 1000   | `B`, `kB`, `MB`, `GB`, `TB`, `PB`, `EB`, `ZB`, `YB`, `RB`, `QB`                                 |
| SI     | bits    | 1000   | `bit`, `kbit`, `Mbit`, `Gbit`, `Tbit`, `Pbit`, `Ebit`, `Zbit`, `Ybit`, `Rbit`, `Qbit`           |
| both   | nibble  | —      | `nibble` (4 bits, half a byte)                                                                  |

Codes follow SI and IEC 80000-13: kilo is `kB` / `kbit`, not `KB`.
Lookup is case-insensitive, so `KB` still matches `kB`. `kB` is SI only;
`KiB` is IEC only. Eight bits are one byte and four bits are one nibble,
so a call may mix bit, nibble, and byte codes in the same family.

The 2022 prefixes are included: SI `RB` / `QB` / `Rbit` / `Qbit` and IEC
`RiB` / `QiB` / `Ribit` / `Qibit`.

## Next steps

- [Getting started](getting-started.md) — install and first conversions
- [Usage](usage.md) — families, names, and error handling
- [Reference](reference.md) — public API
- [Examples](examples.md) — copy-paste recipes
