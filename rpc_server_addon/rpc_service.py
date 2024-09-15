import sys
from transit.writer import Writer
from transit.reader import Reader
from io import StringIO

class RPCService:
    def __init__(self, address, port, datatypes, workspace):
        self.__workspace__ = workspace.__name__
        self.address = address
        self.port = port
        self.register_readers = datatypes.register_readers
        self.register_writers = datatypes.register_writers

    def call_fn(self, fn_args):
        reader = Reader("json")
        self.register_readers(reader)
        incoming_fn_args = reader.read(StringIO(fn_args))  # Decode args
        fn, *args = incoming_fn_args
        # print(f"Calling function: {fn} with args: {args}")
        res = getattr(sys.modules[self.__workspace__], fn)(*args)    
    
        return_value = StringIO()
        writer = Writer(return_value, "json")
        self.register_writers(writer)
        writer.write(res)  # Encode decoded args into the return_value
        # print(res)
        ret = return_value.getvalue()
        # print(ret)
        return ret
        

