from ..libs.blender_utils import get_operator, get_context

class Blink (get_operator()):
  bl_idname = "object.blink"
  bl_label = "Blink"

  def execute(self, context):
    scene = get_context().scene

    return {'FINISHED'}
