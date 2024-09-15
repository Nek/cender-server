import bpy
import zerorpc
import threading
from . import blender_workspace
from .rpc_service import RPCService

class RPCServer:
    def __init__(self):
        self.server = None
        self.server_thread = None

    def launch_server(self):
        print(f"Starting server.")
        panel = bpy.context.scene.rpc_server_panel
        address = panel.rpc_server_address
        port = panel.rpc_server_port
        service = RPCService(address, port, blender_workspace)
        self.server = zerorpc.Server(service)
        self.server.bind(f"tcp://{address}:{port}")
        self.server.run()

    def start(self):
        panel = bpy.context.scene.rpc_server_panel
        if not panel.rpc_server_running:
            self.server_thread = threading.Thread(target=self.launch_server)
            self.server_thread.daemon = True
            self.server_thread.start()
            panel.rpc_server_running = True

    def stop(self):
        print(f"Stopping server.")
        panel = bpy.context.scene.rpc_server_panel
        if panel.rpc_server_running:
            panel.rpc_server_running = False
            if self.server:
                self.server.stop()
            if self.server_thread:
                self.server_thread.join()
            self.server = None
            self.server_thread = None

rpc_server = RPCServer()
