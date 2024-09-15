import bpy
import zerorpc
import threading
from . import blender_workspace
from .rpc_service import RPCService
from . import rpc_service

class RPCServer:
    def __init__(self):
        self.server = None
        self.server_thread = None

    def launch_server(self):
        print(f"Starting server.")
        scene = bpy.context.scene
        address = scene.rpc_server_address
        port = scene.rpc_server_port
        service = RPCService(address, port, blender_workspace)
        self.server = zerorpc.Server(service)
        self.server.bind(f"tcp://{address}:{port}")
        self.server.run()

    def start(self):
        scene = bpy.context.scene
        if not scene.rpc_server_running:
            self.server_thread = threading.Thread(target=self.launch_server)
            self.server_thread.daemon = True
            self.server_thread.start()
            scene.rpc_server_running = True

    def stop(self):
        print(f"Stopping server.")
        scene = bpy.context.scene
        if scene.rpc_server_running:
            scene.rpc_server_running = False
            if self.server:
                self.server.stop()
            if self.server_thread:
                self.server_thread.join()
            self.server = None
            self.server_thread = None

