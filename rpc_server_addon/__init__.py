import bpy
from .operator import RPCServerToggle
from .panel import RPCServerPanel
from .rpc_service import RPCService

def register():
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
    
    bpy.utils.register_class(RPCServerToggle)
    bpy.utils.register_class(RPCServerPanel)
    bpy.utils.register_class(RPCService)

def unregister():
    del bpy.types.Scene.rpc_server_running
    del bpy.types.Scene.rpc_server_address
    del bpy.types.Scene.rpc_server_port
    
    bpy.utils.unregister_class(RPCServerToggle)
    bpy.utils.unregister_class(RPCServerPanel)
    bpy.utils.unregister_class(RPCService)
