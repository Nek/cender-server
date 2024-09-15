import bpy
from .rpc_server import RPCServer
from .operator import RPCServerToggle
from .panel import RPCServerPanel
from .rpc_service import RPCService

def register():
    bpy.utils.register_class(RPCServerToggle)
    bpy.utils.register_class(RPCServerPanel)
    bpy.utils.register_class(RPCService)
    bpy.utils.register_class(RPCServer)


def unregister():
    bpy.utils.unregister_class(RPCServerToggle)
    bpy.utils.unregister_class(RPCServerPanel)
    bpy.utils.unregister_class(RPCService)
    bpy.utils.unregister_class(RPCServer)
