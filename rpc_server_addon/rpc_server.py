import bpy
import zerorpc
import threading
from . import blender_workspace
from .rpc_service import RPCService

class RPCServer:
    def __init__(self):
        self.server = None
        self.thread = None

    def start(self):
        scene = bpy.context.scene
        if not scene.rpc_server_running:
            self.thread = threading.Thread(target=self._launch_server)
            self.thread.daemon = True
            self.thread.start()
            scene.rpc_server_running = True
            print("RPC Server started.")

    def stop(self):
        scene = bpy.context.scene
        if scene.rpc_server_running:
            scene.rpc_server_running = False
            if self.server:
                self.server.stop()
            self.server = None
            self.thread = None
            print("RPC Server stopped.")

    def _launch_server(self):
        scene = bpy.context.scene
        address = scene.rpc_server_address
        port = scene.rpc_server_port
        service = RPCService(address, port, blender_workspace)
        self.server = zerorpc.Server(service)
        self.server.bind(f"tcp://{address}:{port}")
        self.server.run()

# Create a global instance of the RPCServer
rpc_server = RPCServer()

# Ensure these functions are available when the module is imported
__all__ = ['rpc_server']

# Explicitly define the start and stop functions at the module level
start = rpc_server.start
stop = rpc_server.stop

