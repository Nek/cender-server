import bpy
import zerorpc
import threading
from . import blender_workspace
from .rpc_service import RPCService

class RPCServer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RPCServer, cls).__new__(cls)
            cls._instance.server = None
            cls._instance.thread = None
        return cls._instance

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

