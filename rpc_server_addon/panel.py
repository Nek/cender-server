import bpy
from bpy.props import BoolProperty, StringProperty, IntProperty

class RPCServerPanel(bpy.types.Panel):
    bl_label = "RPC Server"
    bl_idname = "VIEW3D_PT_rpc_server"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'RPC Server'

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

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.prop(scene, "rpc_server_address")
        layout.prop(scene, "rpc_server_port")
        label = "Stop Server" if scene.rpc_server_running else "Run Server"
        layout.operator("wm.rpc_server_toggle", text=label)

    @classmethod
    def register(cls):
        bpy.types.Scene.rpc_server_running = cls.rpc_server_running
        bpy.types.Scene.rpc_server_address = cls.rpc_server_address
        bpy.types.Scene.rpc_server_port = cls.rpc_server_port

    @classmethod
    def unregister(cls):
        del bpy.types.Scene.rpc_server_running
        del bpy.types.Scene.rpc_server_address
        del bpy.types.Scene.rpc_server_port
