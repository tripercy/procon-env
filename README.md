# Procon environment for 2024 competition

Environment implementation in C++ for speed optimization. A Python3 module is
exposed to use within python.

## Requirements

- Any C++ compiler
- Python3 (tested for python 3.9)
- Python `setuptools` module.
- Optional: Swig (for rebuilding the module), Makefile (for ease of building/installing)

## How to use

### Normal installation

C++ source must be compiled into platform native machine code using Makefile:

```
make
# or
python setup.py build_ext --build-lib target
```

The resulting module can be found within the `target/` directory, with the two
important files being `board_env.py` and `_board_env.<your platform shared
library format>`. To use the module in python, you must keep these two files in
the same directory and then import board_env.py, i.e.:

```
from board_env import *
```

### Rebuild from source

The template files are built into the repo, but you can regenerate them using swig:

```
make wrapper
# or
swig -c++ -python -outdir target board_env.i
```

Then the shared library can be installed using the step above.
