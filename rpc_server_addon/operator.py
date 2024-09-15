import bpy
from . import server

class RPCServerToggle(bpy.types.Operator):
    bl_idname = "wm.rpc_server_toggle"
    bl_label = "Toggle RPC Server"
    
    def execute(self, context):
        if context.scene.rpc_server_running:
            server.server_stop()
        else:
            server.server_start()
        return {'FINISHED'}
