import bpy

class RPCServerToggle(bpy.types.Operator):
    bl_idname = "wm.rpc_server_toggle"
    bl_label = "Toggle RPC Server"
    
    def execute(self, context):
        scene = context.scene
        if scene.rpc_server_running:
            scene.rpc_server_stop()
        else:
            scene.rpc_server_start()
        return {'FINISHED'}
