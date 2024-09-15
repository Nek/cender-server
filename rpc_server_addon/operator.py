import bpy
import zerorpc
import threading
from . import blender_workspace
from .rpc_service import RPCService

class RPCServerToggle(bpy.types.Operator):
    bl_idname = "wm.rpc_server_toggle"
    bl_label = "Toggle RPC Server"
    
    server = None
    thread = None

    def execute(self, context):
        if context.scene.rpc_server_running:
            self.stop_server(context)
        else:
            self.start_server(context)
        return {'FINISHED'}

    def start_server(self, context):
        if not context.scene.rpc_server_running:
            self.thread = threading.Thread(target=self._launch_server, args=(context,))
            self.thread.daemon = True
            self.thread.start()
            context.scene.rpc_server_running = True
            print("RPC Server started.")

    def stop_server(self, context):
        if context.scene.rpc_server_running:
            context.scene.rpc_server_running = False
            if self.server:
                self.server.stop()
            self.server = None
            self.thread = None
            print("RPC Server stopped.")

    def _launch_server(self, context):
        address = context.scene.rpc_server_address
        port = context.scene.rpc_server_port
        service = RPCService(address, port, blender_workspace)
        self.server = zerorpc.Server(service)
        self.server.bind(f"tcp://{address}:{port}")
        self.server.run()
