import bpy
from bpy.props import *
from .. base import FunctionNode

class ObjectMeshNode(bpy.types.Node, FunctionNode):
    bl_idname = "fn_ObjectMeshNode"
    bl_label = "Object Mesh"

    def declaration(self, builder):
        builder.fixed_input("object", "Object", "Object")
        builder.fixed_output("vertex_locations", "Vertex Locations", "Vector List")