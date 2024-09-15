import bpy
import sys
import mathutils

def move_object(object_name, pos):
    obj = bpy.data.objects.get(object_name)                                                                                                              
    if obj is None:                                                                                                                                      
        return f"Object '{object_name}' not found"                                                                                                                        
    obj.location = pos                                                                                                          
    return f"Moved '{object_name}' to position ({pos.x}, {pos.y}, {pos.z})"

def set_obj_prop(object_name, prop_name, value):
    obj = bpy.data.objects.get(object_name)                                                                                                              
    if obj is None:                                                                                                                                      
        return f"Object '{object_name}' not found"
    setattr(obj, prop_name, value)
    return f"Set '{prop_name} of '{object_name}' to '{value}'"

def eval_code(code):
    return eval(code)

def import_ns(name):
    setattr(sys.modules[__name__], name, __import__(name))

def set_var(name, val):
    setattr(sys.modules[__name__], name, val)

def get_var(name):
    return getattr(sys.modules[__name__], name)