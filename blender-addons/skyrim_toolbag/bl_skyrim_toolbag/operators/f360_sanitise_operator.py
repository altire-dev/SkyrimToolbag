# ===================================================================================================
# Imports: External
# ===================================================================================================
import bpy
from bpy.types import Operator

# ===================================================================================================
# Imports: Internal
# ===================================================================================================


class Fusion360SanitiseOperator(Operator):
    bl_idname = "lb.clean_parent"
    bl_label = "Fusion 360 Sanitiser "

    def execute(self, context):
        print("RUNNING")
        print(context.selected_objects)
        bpy.ops.object.parent_clear(type="CLEAR_KEEP_TRANSFORM")

        # Apply Objects Scales
        bpy.ops.object.transform_apply()

        # Find Empties amongst selection
        empties = []
        for object in context.selected_objects:
            if object.type == "EMPTY":
                empties.append(object)

        # Delete Empties in Selection
        for empty in empties:
            print("DELETING %s" % empty)
            bpy.data.objects.remove(empty, do_unlink=True)

        return {"FINISHED"}


