import struct
import argparse

def stl_to_obj(stl_file, obj_file=None, precision=None):
    vertices = []
    vert_idx = {}
    faces = []
    with open(stl_file, 'rb') as f:
        header = f.read(80)
        num_triangles = int.from_bytes(f.read(4), 'little')
        for [nx, ny, nz, 
            *verts, 
            attributes] in struct.iter_unpack('ffffffffffffH', f.read()):

            if precision:
                [vax, vay, vaz, 
                 vbx, vby, vbz, 
                 vcx, vcy, vcz] = map(lambda pos: round(pos, precision), verts)
            else:
                [vax, vay, vaz, 
                 vbx, vby, vbz, 
                 vcx, vcy, vcz] = verts
        
            if (vax, vay, vaz) not in vert_idx:
                vertices.append((vax, vay, vaz))
                vert_idx[(vax, vay, vaz)] = len(vertices) - 1
            va = vert_idx[(vax, vay, vaz)]

            if (vbx, vby, vbz) not in vert_idx:
                vertices.append((vbx, vby, vbz))
                vert_idx[(vbx, vby, vbz)] = len(vertices) - 1
            vb = vert_idx[(vbx, vby, vbz)]

            if (vcx, vcy, vcz) not in vert_idx:
                vertices.append((vcx, vcy, vcz))
                vert_idx[(vcx, vcy, vcz)] = len(vertices) - 1
            vc = vert_idx[(vcx, vcy, vcz)]

            faces.append((va, vb, vc))
            
    if not obj_file: obj_file = f'{stl_file[:-3]}obj'
    with open(obj_file, 'w+') as f:
        for vertex in vertices:
            f.write(f'v {vertex[0]} {vertex[1]} {vertex[2]}\n')
        for face in faces:
            f.write(f'f {face[0] + 1} {face[1] + 1} {face[2] + 1}\n')


parser = argparse.ArgumentParser(description='Converts a binary STL to OBJ')
parser.add_argument('stl_file', help='STL file to process')
parser.add_argument('obj_file', nargs='?', help='OBJ filename, defaults to stl_file.obj')
parser.add_argument('--precision', '-p', type=int, help='Rounds vertices to the given precision')


args = parser.parse_args()
stl_to_obj(args.stl_file, args.obj_file, args.precision)
