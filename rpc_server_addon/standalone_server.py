import zerorpc
from rpc_service import RPCService

import standalone_workspace

def main():
    address = "127.0.0.1"
    port = 10000
    service = RPCService(address, port, standalone_workspace)

    server = zerorpc.Server(service)
    print(f"Starting standalone RPC server on {address}:{port}")
    server.bind(f"tcp://{address}:{port}")
    server.run()

if __name__ == "__main__":
    main()
