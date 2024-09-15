import bpy
from .server import rpc_server

class RPCServerToggle(bpy.types.Operator):
    bl_idname = "wm.rpc_server_toggle"
    bl_label = "Toggle RPC Server"
    
    def execute(self, context):
        panel = context.scene.rpc_server_panel
        if panel.rpc_server_running:
            rpc_server.stop()
            panel.rpc_server_running = False
        else:
            rpc_server.start()
            panel.rpc_server_running = True
        return {'FINISHED'}
