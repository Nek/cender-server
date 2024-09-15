import bpy
import zerorpc
import threading
from . import blender_workspace
from .rpc_service import RPCService

class RPCServerSettings(bpy.types.PropertyGroup):
    rpc_server_running: bpy.props.BoolProperty(
        name="RPC Server Running",
        description="Indicates whether the RPC server is currently running",
        default=False
    )
    rpc_server_address: bpy.props.StringProperty(
        name="Server Address",
        description="Address for the RPC server",
        default="127.0.0.1"
    )
    rpc_server_port: bpy.props.IntProperty(
        name="Server Port",
        description="Port for the RPC server",
        default=10000,
        min=1024,
        max=65535
    )


bpy.utils.register_class(RPCServerSettings)

bpy.types.Scene.rpc_server_settings = bpy.props.PointerProperty(type=RPCServerSettings)


class RPCServerToggle(bpy.types.Operator):
    bl_idname = "wm.rpc_server_toggle"
    bl_label = "Toggle RPC Server"
    bl_options = {'REGISTER'}
    
    server = None
    thread = None

    def execute(self, context):
        if context.scene.rpc_server_settings.rpc_server_running:
            self.stop_server(context)
        else:
            self.start_server(context)
        return {'FINISHED'}

    def start_server(self, context):
        if not context.scene.rpc_server_settings.rpc_server_running:
            self.thread = threading.Thread(target=self._launch_server, args=(context,))
            self.thread.daemon = True
            self.thread.start()
            context.scene.rpc_server_settings.rpc_server_running = True
            print("RPC Server started.")

    def stop_server(self, context):
        if context.scene.rpc_server_settings.rpc_server_running:
            context.scene.rpc_server_settings.rpc_server_running = False
            if self.server:
                self.server.stop()
            self.server = None
            self.thread = None
            print("RPC Server stopped.")

    def _launch_server(self, context):
        address = context.scene.rpc_server_settings.rpc_server_address
        port = context.scene.rpc_server_settings.rpc_server_port
        service = RPCService(address, port, blender_workspace)
        self.server = zerorpc.Server(service)
        self.server.bind(f"tcp://{address}:{port}")
        self.server.run()
