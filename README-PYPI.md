<!-- markdownlint-disable -->
<p align="center">
  <a href="https://github.com/lupaxa-developers-toolbox">
    <img src="https://raw.githubusercontent.com/the-lupaxa-project/brand-assets/master/logos/organisations/developers-toolbox/readme-logo.png" alt="Project Logo" width="256"/><br/>
  </a>
</p>
<h3 align="center">
  The Lupaxa Developers Toolbox<br />
  Part of The Lupaxa Project
</h3>

<br />

# lupaxa-convert-size

Convert file sizes between IEC (binary) and SI (decimal) units,
including bits, nibbles, and bytes.

Built for scripts and tools used by The Lupaxa Project.

## Features

- Convert between **IEC** units (`B`, `KiB`, … `QiB`, `bit`, `Kibit`, … `Qibit`) using a 1024 scaler
- Convert between **SI** units (`B`, `kB`, … `QB`, `bit`, `kbit`, … `Qbit`) using a 1000 scaler
- Convert between bits, nibbles, and bytes in the same family (8 bits = 2 nibbles = 1 byte)
- Look up the full name of a unit from its abbreviation
- Case-insensitive unit codes
- Fully typed, linted, formatted, and tested

## Installation

### From PyPI

```bash
pip install lupaxa-convert-size
```

### From source (development mode)

```bash
pip install -e ".[dev]"
```

Requires Python 3.10+. No runtime dependencies.

## Usage

```python
from lupaxa.convert_size import convert_size, get_name_from_code

convert_size(1024, "B", "KiB")
# 1.0

convert_size(1, "GiB", "MiB")
# 1024.0

convert_size(2000, "B", "kB", si_units=True)
# 2.0

convert_size(1, "KiB", "Kibit")
# 8.0

convert_size(1, "B", "nibble")
# 2.0

get_name_from_code("MiB")
# "Mebibyte"

get_name_from_code("kB", si_units=True)
# "Kilobyte"
```

A walkthrough of the same API is in `demo.py` in the
[source repository](https://github.com/lupaxa-developers-toolbox/convert-size).

## Development

Clone the repository and install with Make:

```bash
make init                # first-time makefile-skills checkout
make python-install-dev  # editable install with [dev]
make python-check        # lint, type-check, and test
make mkdocs-serve        # local docs site
```

Documentation: <https://convert-size.thelupaxaproject.org/>.

<a href="https://github.com/the-lupaxa-project">
    <img src="https://raw.githubusercontent.com/the-lupaxa-project/brand-assets/master/logos/components/footer-for-child-orgs.svg" alt="The Lupaxa Project Footer" width="100%" />
</a>
