import mathutils

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

def register_readers(reader):
    reader.register("blender-vector", VectorReader)

def register_writers(writer):
    writer.register(mathutils.Vector, VectorWriter)