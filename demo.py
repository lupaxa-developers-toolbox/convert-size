"""Walkthrough of the lupaxa.convert_size public API."""

from __future__ import annotations

from lupaxa.convert_size import convert_size, convert_size_iec, convert_size_si

print("IEC conversions")
print(f"  1024 B -> {convert_size_iec(1024, 'B', 'KiB')} KiB")
print(f"  1 GiB -> {convert_size(1, 'GiB', 'MiB')} MiB")
print(f"  1 KiB -> {convert_size_iec(1, 'KiB', 'Kibit')} Kibit")
print(f"  1 B -> {convert_size_iec(1, 'B', 'nibble')} nibble")

print("SI conversions")
print(f"  1000 B -> {convert_size_si(1000, 'B', 'kB')} kB")
print(f"  2 GB -> {convert_size(2, 'GB', 'MB', si_units=True)} MB")
print(f"  8 bit -> {convert_size_si(8, 'bit', 'B')} B")
