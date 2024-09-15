class Vector:
    def __init__(self, vals):
        self.vals = vals
    def vals(self):
        return self.vals

class VectorReader(object):
    @staticmethod
    def from_rep(v):
        return Vector(v)

class VectorWriter(object):
    @staticmethod
    def tag(a):
        return 'blender-vector'

    @staticmethod
    def rep(a):
        return a.vals

    @staticmethod
    def string_rep(a):
        return None

def move_object(object_name: str, pos):
    print(f"Moved '{object_name}' to position ({pos})")
    return Vector(pos)

def register_readers(reader):
    reader.register("blender-vector", VectorReader)

def register_writers(writer):
    writer.register(Vector, VectorWriter)