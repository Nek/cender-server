import bpy

class RPCServerPanel(bpy.types.Panel):
    bl_label = "RPC Server"
    bl_idname = "VIEW3D_PT_rpc_server"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'RPC Server'

    def draw(self, context):
        global label
        layout = self.layout
        props = context.scene.rpc_server_settings
        label = "Stop Server" if props.rpc_server_running else "Run Server"
        layout.operator("wm.rpc_server_toggle", text=label)
        layout.prop(props, "rpc_server_address")
        layout.prop(props, "rpc_server_port")
