import zerorpc

from transit.writer import Writer
from transit.reader import Reader
from io import StringIO

class RPCService:
    def __init__(self, address, port):
        self.address = address
        self.port = port
    
    def echo(self, args):
        reader = Reader("json") # or "msgpack"
        incoming_args = reader.read(StringIO(args)) # Decode args
        print(incoming_args)
        return_value = StringIO()
        writer = Writer(return_value, "json") # or "json-verbose", "msgpack"
        writer.write(incoming_args) # Encode decoded args into the return_value
        return return_value.getvalue()

address = "127.0.0.1"
port = 10000
service = RPCService(address, port)
server = zerorpc.Server(service)
server.bind(f"tcp://{address}:{port}")
server.run()
