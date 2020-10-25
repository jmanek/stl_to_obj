import struct
import argparse

def stl_to_obj(stl_file, obj_file=None, precision=None):
    verts = []
    verts_idx = {}
    faces = []
    with open(stl_file, 'rb') as f:
        header = f.read(80)
        num_triangles = int.from_bytes(f.read(4), 'little')
        for [nx, ny, nz, 
            *face_verts, 
            attributes] in struct.iter_unpack('ffffffffffffH', f.read()):

            [vax, vay, vaz, 
             vbx, vby, vbz, 
             vcx, vcy, vcz] = map(lambda pos: round(pos, precision), face_verts) if precision else face_verts
        
            va = (vax, vay, vaz)
            if va not in verts_idx:
                verts.append(va)
                verts_idx[va] = len(verts) - 1
            va = verts_idx[va]

            vb = (vbx, vby, vbz)
            if vb not in verts_idx:
                verts.append(vb)
                verts_idx[vb] = len(verts) - 1
            vb = verts_idx[vb]

            vc = (vcx, vcy, vcz)
            if vc not in verts_idx:
                verts.append(vc)
                verts_idx[vc] = len(verts) - 1
            vc = verts_idx[vc]

            faces.append((va, vb, vc))
            
    if not obj_file: obj_file = f'{stl_file[:-3]}obj'
    with open(obj_file, 'w+') as f:
        for vert in verts:
            f.write(f'v {vert[0]} {vert[1]} {vert[2]}\n')
        for face in faces:
            f.write(f'f {face[0] + 1} {face[1] + 1} {face[2] + 1}\n')


parser = argparse.ArgumentParser(description='Converts a binary STL to OBJ')
parser.add_argument('stl_file', help='STL file to process')
parser.add_argument('obj_file', nargs='?', help='OBJ filename, defaults to stl_file.obj')
parser.add_argument('--precision', '-p', type=int, help='Rounds vertices to the given precision')

args = parser.parse_args()
stl_to_obj(args.stl_file, args.obj_file, args.precision)