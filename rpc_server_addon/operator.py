import bpy
from .rpc_server import start, stop

class RPCServerToggle(bpy.types.Operator):
    bl_idname = "wm.rpc_server_toggle"
    bl_label = "Toggle RPC Server"
    
    def execute(self, context):
        scene = context.scene
        if scene.rpc_server_running:
            stop()
        else:
            start()
        return {'FINISHED'}
