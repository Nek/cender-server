import bpy
from .operator import RPCServerToggle
from .panel import RPCServerPanel
from .rpc_service import RPCService
from .properties import RPCServerProperties

def register():
    RPCServerProperties.register()
    
    bpy.utils.register_class(RPCServerToggle)
    bpy.utils.register_class(RPCServerPanel)
    bpy.utils.register_class(RPCService)

def unregister():
    RPCServerProperties.unregister()
    
    bpy.utils.unregister_class(RPCServerToggle)
    bpy.utils.unregister_class(RPCServerPanel)
    bpy.utils.unregister_class(RPCService)
