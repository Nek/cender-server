import bpy
import zerorpc
import threading
from . import blender_workspace
from .rpc_service import RPCService

rpc_server = None

def launch_server():
    global rpc_server
    print("Starting server.")
    scene = bpy.context.scene
    address = scene.rpc_server_address
    port = scene.rpc_server_port
    service = RPCService(address, port, blender_workspace)
    rpc_server = zerorpc.Server(service)
    rpc_server.bind(f"tcp://{address}:{port}")
    rpc_server.run()

def start():
    scene = bpy.context.scene
    if not scene.rpc_server_running:
        server_thread = threading.Thread(target=launch_server)
        server_thread.daemon = True
        server_thread.start()
        scene.rpc_server_running = True

def stop():
    global rpc_server
    print("Stopping server.")
    scene = bpy.context.scene
    if scene.rpc_server_running:
        scene.rpc_server_running = False
        if rpc_server:
            rpc_server.stop()
        rpc_server = None

