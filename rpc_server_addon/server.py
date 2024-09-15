import bpy
import zerorpc
import threading
from . import blender_workspace
from .rpc_service import RPCService

server = None
server_thread = None

def launch_server():
    print(f"Starting server.")
    global server
    address = bpy.context.scene.rpc_server_address
    port = bpy.context.scene.rpc_server_port
    service = RPCService(address, port, blender_workspace)
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
