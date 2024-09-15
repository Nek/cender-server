import bpy

class RPCServerProperties(bpy.types.PropertyGroup):
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

def register():
    bpy.utils.register_class(RPCServerProperties)
    bpy.types.Scene.rpc_server_props = bpy.props.PointerProperty(type=RPCServerProperties)

def unregister():
    del bpy.types.Scene.rpc_server_props
    bpy.utils.unregister_class(RPCServerProperties)
