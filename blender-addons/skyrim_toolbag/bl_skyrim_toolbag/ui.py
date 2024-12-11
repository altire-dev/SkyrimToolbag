# ===================================================================================================
# Imports: External
# ===================================================================================================
import bpy

# ===================================================================================================
# Imports: Internal
# ===================================================================================================
from .operators import Fusion360SanitiseOperator
from .operators import LBExportNIFOperator

# ===================================================================================================
# Class: LBDT Panel
# ===================================================================================================

class VIEW3D_PT_LBDT_Panel(bpy.types.Panel):
    pass

    # Where to add the panel in the UI
    bl_space_type = "VIEW_3D"  # 3D Viewport Area
    bl_region_type = "UI"  # Sidebar Reion

    # Add Labels
    bl_category = "Lordbound"  # Label in the sidebar
    bl_label = "Lordbound Dev Tools"  # Label of the Sidebar Menu (once expanded)

    def draw(self, context):
        '''
        The function that actually draws the panel
        '''
        lbdt = context.scene.lbdt

        # Create an option in our Panel!
        row = self.layout.row()
        row.operator(Fusion360SanitiseOperator.bl_idname, text="Fusion 360 Sanitiser", icon="OUTLINER_OB_FORCE_FIELD")

        export_box = self.layout.box()

        row = export_box.row()
        row.label(text="Reset Location:")
        row.prop(lbdt, "reset_location")

        row = export_box.row()
        row.label(text="Output Scale:")
        row.prop(lbdt, "output_scale")

        row = export_box.row()

        row.operator(LBExportNIFOperator.bl_idname, text="Export NIF", icon="EXPORT")


