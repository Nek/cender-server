import bpy
from . import rpc_server

class RPCServerToggle(bpy.types.Operator):
    bl_idname = "wm.rpc_server_toggle"
    bl_label = "Toggle RPC Server"
    
    def execute(self, context):
        scene = context.scene
        if scene.rpc_server_running:
            rpc_server.stop()
            scene.rpc_server_running = False
        else:
            rpc_server.start()
            scene.rpc_server_running = True
        return {'FINISHED'}
