import bpy
import mathutils
import sys
from transit.writer import Writer
from transit.reader import Reader
from io import StringIO

class RPCService:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.reader = Reader("json")  # or "msgpack"
        self.reader.register("Vector", lambda vals: mathutils.Vector(vals))

    def call_fn(self, fn_args):
        incoming_fn_args = self.reader.read(StringIO(fn_args))  # Decode args
        fn, *args = incoming_fn_args
        print(f"Calling function: {fn} with args: {args}")
        res = getattr(sys.modules[__name__], fn)(*args)         
        return_value = StringIO()
        writer = Writer(return_value, "json")  # or "json-verbose", "msgpack"
        writer.write(res)  # Encode decoded args into the return_value
        return return_value.getvalue()
        
    def eval_code(self, code: str):
        return eval(code)

def move_object(object_name: str, pos):
    obj = bpy.data.objects.get(object_name)
    if obj is None:
        return f"Object '{object_name}' not found"
    
    obj.location = pos
    return f"Moved '{object_name}' to position ({pos})"
