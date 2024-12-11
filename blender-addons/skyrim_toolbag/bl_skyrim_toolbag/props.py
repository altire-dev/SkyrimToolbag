# ===================================================================================================
# Imports: External
# ===================================================================================================
from bpy.types import PropertyGroup
from bpy.props import BoolProperty
from bpy.props import StringProperty

# ===================================================================================================
# Imports: Internal
# ===================================================================================================

# ===================================================================================================
# Class: LBDT Add-on Properties
# ===================================================================================================
class LBDT_ADDON_Props(PropertyGroup):
    reset_location: BoolProperty(
        name="",
        description="Ensure the Mesh's location is reset to world center for export",
        default=True
    )

    output_scale: StringProperty(
        name="",
        description="Desired scale for NIF Output",
        default="10.0"
    )