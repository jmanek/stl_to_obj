# stl_to_obj
Converts a binary STL to OBJ

Uses dictionary lookup for fast results

Requires Python 3.6 and newer

## Installation

`pip install stl_to_obj`

or

`git clone https://github.com/jmanek/stl_to_obj.git`

## Usage

Can be run from the command line or imported 

```
from stl_to_obj import stl_to_obj

stl_to_obj('input1.stl') # saves to output1.obj

stl_to_obj('input2.stl', 'output2.obj', precision=6, verbose=True)
```

```
usage: stl_to_obj [-h] [--precision PRECISION] [--verbose] stl_file [obj_file]

Converts a binary STL to OBJ

positional arguments:
  stl_file              STL file to process
  obj_file              OBJ filename, defaults to stl_file.obj

optional arguments:
  -h, --help            show this help message and exit
  --precision PRECISION, -p PRECISION
                        Rounds vertices to the given precision
  --verbose, -v         Outputs conversion info
```
