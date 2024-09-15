import bpy

class RPCServerProperties(bpy.types.PropertyGroup):
    rpc_server_running: bpy.props.BoolProperty
    rpc_server_address: bpy.props.StringProperty
    rpc_server_port: bpy.props.IntProperty

    def __init__(self):
        self.rpc_server_running = bpy.props.BoolProperty(
            name="RPC Server Running",
            description="Indicates whether the RPC server is currently running",
            default=False
        )
        self.rpc_server_address = bpy.props.StringProperty(
            name="Server Address",
            description="Address for the RPC server",
            default="127.0.0.1"
        )
        self.rpc_server_port = bpy.props.IntProperty(
            name="Server Port",
            description="Port for the RPC server",
            default=10000,
            min=1024,
            max=65535
        )

    @classmethod
    def register(cls):
        bpy.utils.register_class(cls)
        bpy.types.Scene.rpc_server_props = bpy.props.PointerProperty(type=cls)

    @classmethod
    def unregister(cls):
        del bpy.types.Scene.rpc_server_props
        bpy.utils.unregister_class(cls)

def register():
    RPCServerProperties.register()

def unregister():
    RPCServerProperties.unregister()
