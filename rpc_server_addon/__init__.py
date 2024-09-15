import bpy

from .operator import RPCServerToggle
from .panel import RPCServerPanel, register as panel_register, unregister as panel_unregister

def register():
    panel_register()
    bpy.utils.register_class(RPCServerToggle)
    bpy.utils.register_class(RPCServerPanel)

def unregister():
    panel_unregister()
    bpy.utils.unregister_class(RPCServerToggle)
    bpy.utils.unregister_class(RPCServerPanel)

if __name__ == "__main__":
    register()
