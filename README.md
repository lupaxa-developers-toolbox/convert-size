<p align="center">
  <a href="https://github.com/lupaxa-developers-toolbox">
    <img src="https://raw.githubusercontent.com/the-lupaxa-project/brand-assets/master/logos/organisations/developers-toolbox/readme-logo.png" alt="Developers Toolbox" />
  </a>
</p>

<h1 align="center">convert-size</h1>

Convert file sizes between IEC (binary, 1024) and SI (decimal, 1000)
units, including bits, nibbles, and bytes.

## Install

```bash
pip install lupaxa-convert-size
```

Requires Python 3.10+.

## Usage

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

## Documentation

Site pages live in `mkdocs/` and publish to
<https://convert-size.thelupaxaproject.org/>.

```bash
make init
make python-install-dev
make mkdocs-serve
```

<a href="https://github.com/the-lupaxa-project">
    <img src="https://raw.githubusercontent.com/the-lupaxa-project/brand-assets/master/logos/components/footer-for-child-orgs.svg" alt="The Lupaxa Project Footer" width="100%" />
</a>
