import bpy
from .rpc_server import rpc_server
from .operator import RPCServerToggle
from .panel import RPCServerPanel
from .rpc_service import RPCService

bl_info = {
    "name": "RPC Server Addon",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > RPC Server",
    "description": "RPC Server for Blender",
    "warning": "",
    "doc_url": "",
    "category": "Development",
}

def register():
    bpy.utils.register_class(RPCServerToggle)
    bpy.utils.register_class(RPCServerPanel)
    bpy.utils.register_class(RPCService)
    
    # Register the start and stop methods of the RPCServer instance
    bpy.types.Scene.rpc_server_start = rpc_server.start
    bpy.types.Scene.rpc_server_stop = rpc_server.stop

def unregister():
    bpy.utils.unregister_class(RPCServerToggle)
    bpy.utils.unregister_class(RPCServerPanel)
    bpy.utils.unregister_class(RPCService)
    
    # Unregister the start and stop methods
    del bpy.types.Scene.rpc_server_start
    del bpy.types.Scene.rpc_server_stop

if __name__ == "__main__":
    register()

# Expose start and stop methods at the addon level
start = rpc_server.start
stop = rpc_server.stop

__all__ = ['register', 'unregister', 'start', 'stop']
