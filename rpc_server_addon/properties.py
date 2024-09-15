import bpy

def register_properties():
    bpy.types.Scene.rpc_server_running = bpy.props.BoolProperty(
        name="RPC Server Running",
        description="Indicates whether the RPC server is currently running",
        default=False
    )
    bpy.types.Scene.rpc_server_address = bpy.props.StringProperty(
        name="Server Address",
        description="Address for the RPC server",
        default="127.0.0.1"
    )
    bpy.types.Scene.rpc_server_port = bpy.props.IntProperty(
        name="Server Port",
        description="Port for the RPC server",
        default=10000,
        min=1024,
        max=65535
    )

def unregister_properties():
    del bpy.types.Scene.rpc_server_running
    del bpy.types.Scene.rpc_server_address
    del bpy.types.Scene.rpc_server_port
