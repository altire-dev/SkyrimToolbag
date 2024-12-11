# ===================================================================================================
# Imports: External
# ===================================================================================================
import bpy
import mathutils
from io_scene_nifly import ExportNIF
from bpy.types import Operator

# ===================================================================================================
# Imports: Internal
# ===================================================================================================

# ===================================================================================================
# Class: Export NIF Operator
# ===================================================================================================
class LBExportNIFOperator(ExportNIF, Operator):
    bl_idname = "lb.export_to_nif"
    bl_label = "Export NIF"
    bl_space_type = "VIEW_3D"
    bl_parent_id = "io_scene_nifly.ExportNIF"

    def __init__(self):
        super(LBExportNIFOperator, self).__init__()

    def execute(self, context):
        r_val = {"FINISHED"}
        lbdt = context.scene.lbdt
        print("LB: Starting Export")
        # Get Object scales
        original_scales = {}
        original_locations = {}

        if lbdt.reset_location:
            print("OK, we will be resetting location")
        else:
            print("Naaah")

        # Upscale all Objects
        print("LB: Getting Original Scales")
        for object in context.selected_objects:
            original_scales[object] = object.scale.copy()
            if lbdt.reset_location:
                original_locations[object] = object.location.copy()
                object.location = mathutils.Vector((0.0, 0.0, 0.0))
            object.scale = mathutils.Vector((
                float(lbdt.output_scale),
                float(lbdt.output_scale),
                float(lbdt.output_scale)
            ))
        print("LB: Processed Original Scales. Upscaled")

        # Center Mesh at Origin point

        print("LB: Calling PyNifly")
        r_val = super(LBExportNIFOperator, self).execute(context)
        print("LB: PyNifly Finished")

        # Restore Scales and Locations
        print("LB: Restoring Scales")
        for object in context.selected_objects:
            object.scale = original_scales[object]
            if lbdt.reset_location:
                object.location = original_locations[object]
        print("LB: Scales Restored")

        print("DONE")
        return r_val