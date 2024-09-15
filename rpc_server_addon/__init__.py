import bpy

from .operator import RPCServerToggle
from .panel import RPCServerPanel

def register():
    bpy.utils.register_class(RPCServerToggle)
    bpy.utils.register_class(RPCServerPanel)

def unregister():
    bpy.utils.unregister_class(RPCServerToggle)
    bpy.utils.unregister_class(RPCServerPanel)

if __name__ == "__main__":
    register()
