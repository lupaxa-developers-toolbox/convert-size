# Usage

## Convert a size

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

## Bits, nibbles, and bytes

Within one family, bit, nibble, and byte codes convert through 8 bits per
byte and 4 bits per nibble:

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

## Look up a unit name

```python
from lupaxa.convert_size import get_name_from_code

get_name_from_code("KiB")
# "Kibibyte"

get_name_from_code("kB", si_units=True)
# "Kilobyte"

get_name_from_code("Kibit")
# "Kibibit"
```

Codes are matched case-insensitively (`kib`, `KIB`, and `KiB` are the same).
The stored SI kilo symbol is `kB`, which is the SI spelling.

## Invalid units

Unknown abbreviations raise `ValueError` and list the valid codes for that
family. `kB` is not valid in IEC mode; `KiB` is not valid in SI mode.

```python
convert_size(1, "kB", "MB")
# ValueError: Invalid unit type kB, valid options are: B, KiB, MiB, ...
```

## Constants

The unit tables are exported if you need to iterate them:

```python
from lupaxa.convert_size import SIZE_CODES_IEC, SIZE_CODES_IEC_BITS, SIZE_CODES_SI

list(SIZE_CODES_IEC)
list(SIZE_CODES_IEC_BITS)
list(SIZE_CODES_SI)
```
