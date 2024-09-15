bl_info = {
    "name": "RPC Server",
    "blender": (4, 2, 0),
    "category": "View"
}

import bpy
import zerorpc
import threading
from bpy.props import BoolProperty, StringProperty, IntProperty
import mathutils
from bpy.utils import register_class, unregister_class

from transit.writer import Writer
from transit.reader import Reader
from transit.decoder import Tag

from io import StringIO

import sys

def move_object(object_name: str, pos):
    obj = bpy.data.objects.get(object_name)
    if obj is None:
        return f"Object '{object_name}' not found"
    
    obj.location = pos
    return f"Moved '{object_name}' to position ({pos})"

class RPCService:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.reader = Reader("json")  # or "msgpack"
        self.reader.register("Vector", lambda vals: mathutils.Vector(vals))

    def call_fn(self, fn_args):
        incoming_fn_args = self.reader.read(StringIO(fn_args))  # Decode args
        fn, *args = incoming_fn_args
        print(f"Calling function: {fn} with args: {args}")
        res = getattr(sys.modules[__name__], fn)(*args)         
        return_value = StringIO()
        writer = Writer(return_value, "json")  # or "json-verbose", "msgpack"
        writer.write(res)  # Encode decoded args into the return_value
        return return_value.getvalue()
        
    def eval_code(self, code: str):
        return eval(code)

server = None
server_thread = None

def launch_server():
    print(f"Starting server.")
    global server
    address = bpy.context.scene.rpc_server_address
    port = bpy.context.scene.rpc_server_port
    service = RPCService(address, port)
    server = zerorpc.Server(service)
    server.bind(f"tcp://{address}:{port}")
    server.run()

def server_start():
    global server_thread
    if not bpy.context.scene.rpc_server_running:
        server_thread = threading.Thread(target=launch_server)
        server_thread.daemon = True
        server_thread.start()
        bpy.context.scene.rpc_server_running = True

def server_stop():
    print(f"Stopping server.")
    global server, server_thread
    if bpy.context.scene.rpc_server_running:
        bpy.context.scene.rpc_server_running = False
        if server:
            server.stop()
        if server_thread:
            server_thread.join()
        server = None
        server_thread = None

class RPCServerToggle(bpy.types.Operator):
    bl_idname = "wm.rpc_server_toggle"
    bl_label = "Toggle RPC Server"
    
    def execute(self, context):
        if context.scene.rpc_server_running:
            server_stop()
        else:
            server_start()
        return {'FINISHED'}

class RPCServerPanel(bpy.types.Panel):
    bl_label = "RPC Server"
    bl_idname = "VIEW3D_PT_rpc_server"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'RPC Server'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.prop(scene, "rpc_server_address")
        layout.prop(scene, "rpc_server_port")
        label = "Stop Server" if scene.rpc_server_running else "Run Server"
        layout.operator("wm.rpc_server_toggle", text=label)

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
