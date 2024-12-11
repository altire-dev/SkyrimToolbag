bl_info = {
    "name": "Skyrim Toolbag",
    "description": "A collection of tools and utilities to help with creating Assets for Skyrim",
    "author": "Altire",
    "version": (0, 0, 5), # WARNING: This property is auto-updated by build.py. Do not update manually!
    "blender": (3, 6, 0),
    "location": "3D Viewport > Sidebar > Skyrim Toolbag",
    "category": "Development",
}


# ===================================================================================================
# Imports: External
# ===================================================================================================
import sys
import importlib
import bpy
from bpy.props import PointerProperty

# ===================================================================================================
# Imports: Internal
# ===================================================================================================
from .ui import VIEW3D_PT_LBDT_Panel
from .props import SKT_ADDON_Props
from .operators import Fusion360SanitiseOperator
from .operators import LBExportNIFOperator

# ===================================================================================================
# Add-on Info
# ===================================================================================================
# ===========================================================================================
#
# ENTRY
#
# ===========================================================================================
# Register the panel with Blender
def register():
    bpy.utils.register_class(SKT_ADDON_Props)
    bpy.utils.register_class(Fusion360SanitiseOperator)
    bpy.utils.register_class(LBExportNIFOperator)
    bpy.utils.register_class(VIEW3D_PT_LBDT_Panel)

    # Register our Properties to we can set/access them from anywhere!
    bpy.types.Scene.lbdt = PointerProperty(type=SKT_ADDON_Props)


# Unregister
def unregister():
    bpy.utils.unregister_class(SKT_ADDON_Props)
    bpy.utils.unregister_class(VIEW3D_PT_LBDT_Panel)
    bpy.utils.unregister_class(LBExportNIFOperator)
    bpy.utils.unregister_class(Fusion360SanitiseOperator)