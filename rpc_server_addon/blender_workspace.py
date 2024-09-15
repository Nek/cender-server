import bpy
import sys
import mathutils

def move_object(object_name, pos):
    obj = bpy.data.objects.get(object_name)                                                                                                              
    if obj is None:                                                                                                                                      
        return f"Object '{object_name}' not found"                                                                                                                        
    obj.location = pos                                                                                                          
    return f"Moved '{object_name}' to position ({pos.x}, {pos.y}, {pos.z})"

def eval_code(code):
    return eval(code)

def import_ns(name):
    setattr(sys.modules[__name__], name, __import__(name))

def set_var(name, val):
    setattr(sys.modules[__name__], name, val)

def get_var(name):
    return getattr(sys.modules[__name__], name)

# objects, materials
def set_item_prop(collection, item_name, prop_name, value):
    item = getattr(bpy.data, collection).get(item_name)                                                                                                              
    if item is None:                                                                                                                                      
        return f"Item '{item_name}' of '{collection}' not found"
    setattr(item, prop_name, value)
    return f"Set '{prop_name} of '{item_name}' of '{collection}' to '{value}'"

def get_item_prop(collection, item_name, prop_name):
    item = getattr(bpy.data, collection).get(item_name)                                                                                                            
    if item is None:                                                                                                                                      
        return f"Item '{item_name}' of '{collection}' not found"
    return getattr(item, prop_name)

def set_obj_prop(object_name, prop_name, value):
    obj = bpy.data.objects.get(object_name)                                                                                                              
    if obj is None:                                                                                                                                      
        return f"Object '{object_name}' not found"
    setattr(obj, prop_name, value)
    return f"Set '{prop_name} of '{object_name}' to '{value}'"

def get_obj_prop(object_name, prop_name):
    obj = bpy.data.objects.get(object_name)                                                                                                              
    if obj is None:                                                                                                                                      
        return f"Object '{object_name}' not found"
    return getattr(obj, prop_name)

def add_cube(name, size=1):
    bpy.ops.mesh.primitive_cube_add(size=size)
    bpy.context.object.name = name
    return bpy.context.object.name