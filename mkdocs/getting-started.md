# Getting started

## Requirements

- Python 3.10 or newer
- No runtime dependencies

## Install

```bash
python3 -m pip install lupaxa-convert-size
```

Then import the package:

```python
from lupaxa.convert_size import convert_size

print(convert_size(1024, "B", "KiB"))
```

The PyPI name is `lupaxa-convert-size`. The import path is
`lupaxa.convert_size`. `lupaxa` is a namespace package — there is no
`lupaxa/__init__.py`.

### From source (development)

Editable install with dev extras (includes the MkDocs pins):

```bash
make init
make python-install-dev
```

Site Markdown lives in `mkdocs/` (not GitHub’s special `docs/` directory).
After makefile-skills are installed:

```bash
make mkdocs-serve
```

## First conversions

```python
from lupaxa.convert_size import convert_size, get_name_from_code

print(convert_size(1, "GiB", "MiB"))
print(convert_size(2, "GB", "MB", si_units=True))
print(convert_size(1, "KiB", "Kibit"))
print(get_name_from_code("TiB"))
```

A walkthrough of the same API lives in `demo.py` at the repository root
(not shipped in the wheel):

```bash
python demo.py
```

## Makefile helpers

```bash
make init                 # clone makefile-skills into .makefiles/
make python-install-dev   # editable install with [dev]
make python-check         # lint + type + test (via makefile-skills)
make mkdocs-serve         # local docs site
```
