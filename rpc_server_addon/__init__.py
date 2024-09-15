import bpy
from bpy.props import BoolProperty, StringProperty, IntProperty
from . import server
from .operator import RPCServerToggle
from .panel import RPCServerPanel

def register():
    bpy.utils.register_class(RPCServerToggle)
    bpy.utils.register_class(RPCServerPanel)
    bpy.types.Scene.rpc_server_running = BoolProperty(
        name="RPC Server Running",
        description="Indicates whether the RPC server is currently running",
        default=False
    )
    bpy.types.Scene.rpc_server_address = StringProperty(
        name="Server Address",
        description="Address for the RPC server",
        default="127.0.0.1"
    )
    bpy.types.Scene.rpc_server_port = IntProperty(
        name="Server Port",
        description="Port for the RPC server",
        default=10000,
        min=1024,
        max=65535
    )

def unregister():
    bpy.utils.unregister_class(RPCServerToggle)
    bpy.utils.unregister_class(RPCServerPanel)
    del bpy.types.Scene.rpc_server_running
    del bpy.types.Scene.rpc_server_address
    del bpy.types.Scene.rpc_server_port

if __name__ == "__main__":
    register()
