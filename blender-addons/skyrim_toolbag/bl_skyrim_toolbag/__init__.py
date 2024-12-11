# ===================================================================================================
# Add-on Info
# ===================================================================================================
bl_info = {
    "name": "Lordbound Dev Tools",
    "description": "A collection of tools and utilities for the Lordbound Development Team",
    "author": "Altire",
    "version": (0, 0, 2),
    "blender": (3, 6, 0),
    "location": "3D Viewport > Sidebar > Lordbound",
    "category": "Development",
}

# ===================================================================================================
# Imports: External
# ===================================================================================================
import bpy
from bpy.props import PointerProperty

# ===================================================================================================
# Imports: Internal
# ===================================================================================================
from .ui import VIEW3D_PT_LBDT_Panel
from .props import LBDT_ADDON_Props
from .operators import Fusion360SanitiseOperator
from .operators import LBExportNIFOperator

# ===========================================================================================
#
# ENTRY
#
# ===========================================================================================
# Register the panel with Blender
def register():
    bpy.utils.register_class(LBDT_ADDON_Props)
    bpy.utils.register_class(Fusion360SanitiseOperator)
    bpy.utils.register_class(LBExportNIFOperator)
    bpy.utils.register_class(VIEW3D_PT_LBDT_Panel)

    # Register our Properties to we can set/access them from anywhere!
    bpy.types.Scene.lbdt = PointerProperty(type=LBDT_ADDON_Props)


# Unregister
def unregister():
    bpy.utils.unregister_class(LBDT_ADDON_Props)
    bpy.utils.unregister_class(VIEW3D_PT_LBDT_Panel)
    bpy.utils.unregister_class(LBExportNIFOperator)
    bpy.utils.unregister_class(Fusion360SanitiseOperator)