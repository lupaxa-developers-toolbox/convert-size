# Examples

## IEC Conversion

```python
from lupaxa.convert_size import convert_size

print(convert_size(1024, "B", "KiB"))
print(convert_size(1, "GiB", "MiB"))
print(convert_size(5, "MiB", "B"))
```

## SI Conversion

```python
from lupaxa.convert_size import convert_size

print(convert_size(1000, "B", "kB", si_units=True))
print(convert_size(2.5, "GB", "MB", si_units=True))
```

## Dedicated Helpers

```python
from lupaxa.convert_size import convert_size_iec, convert_size_si

print(convert_size_iec(2048, "KiB", "MiB"))
print(convert_size_si(2048, "kB", "MB"))
```

## Bits, Nibbles, and Bytes

```python
print(convert_size(8, "bit", "B"))
print(convert_size(1, "B", "nibble"))
print(convert_size(4, "bit", "nibble"))
print(convert_size(1, "KiB", "Kibit"))
print(convert_size(1, "MB", "Mbit", si_units=True))
```

## Unit Names

```python
from lupaxa.convert_size import get_name_from_code

print(get_name_from_code("PiB"))
print(get_name_from_code("kB", si_units=True))
print(get_name_from_code("Kibit"))
```

## Case-Insensitive Codes

```python
from lupaxa.convert_size import convert_size

print(convert_size(1, "gib", "mib"))
print(convert_size(1, "tb", "gb", si_units=True))
```

## Demo Script

From a clone of this repository (not installed with the wheel):

```bash
python demo.py
```
