import bpy
from .server import rpc_server

class RPCServerToggle(bpy.types.Operator):
    bl_idname = "wm.rpc_server_toggle"
    bl_label = "Toggle RPC Server"
    
    def execute(self, context):
        if context.scene.rpc_server_running:
            rpc_server.stop()
        else:
            rpc_server.start()
        return {'FINISHED'}
