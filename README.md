# stl_to_obj
Converts a binary STL to OBJ

Uses dictionary lookup for fast results

Requires Python 3

Can be run from the command line or imported as 

```
from stl_to_obj import *
stl_to_obj('input.stl', 'output.obj')
```

```
usage: stl_to_obj.py [-h] [--precision PRECISION] stl_file [obj_file]

Converts a binary STL to OBJ

positional arguments:
  stl_file              STL file to process
  obj_file              OBJ filename, defaults to stl_file.obj

optional arguments:
  -h, --help            show this help message and exit
  --precision PRECISION, -p PRECISION
                        Rounds vertices to the given precision
```
