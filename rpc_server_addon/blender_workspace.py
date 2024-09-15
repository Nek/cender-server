import mathutils
import bpy

class VectorReader(object):
    @staticmethod
    def from_rep(v):
        return mathutils.Vector(v)

class VectorWriter(object):
    @staticmethod
    def tag(a):
        return 'blender-vector'

    @staticmethod
    def rep(a):
        return a[:]

    @staticmethod
    def string_rep(a):
        return None

def move_object(object_name: str, pos):
    obj = bpy.data.objects[object_name]
    obj.location = pos
    print(f"Moved '{object_name}' to position ({pos})")
    return ["move_object", [object_name, pos]]

def register_readers(reader):
    reader.register("blender-vector", VectorReader)

def register_writers(writer):
    writer.register(mathutils.Vector, VectorWriter)
