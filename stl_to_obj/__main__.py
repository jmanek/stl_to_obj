import argparse
from stl_to_obj import stl_to_obj

parser = argparse.ArgumentParser(description='Converts a binary STL to OBJ')
parser.add_argument('stl_file', help='STL file to process')
parser.add_argument('obj_file', nargs='?',
                    help='OBJ filename, defaults to stl_file.obj')
parser.add_argument('--precision', '-p', type=int,
                    help='Rounds vertices to the given precision')
parser.add_argument('--verbose', '-v', action='store_true',
                    help='Outputs conversion info')

args = parser.parse_args()
try:
    stl_to_obj(args.stl_file, args.obj_file, args.precision, args.verbose)
except Exception as e:
    print('Failed to convert STL file')
    print(f'Error: {e}')
