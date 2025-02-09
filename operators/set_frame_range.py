from ..libs.blender_utils import get_operator, get_context

class Set_Frame_Range (get_operator()):
  bl_idname = "object.set_frame_range"
  bl_label = "Set Frame Range"

  def execute(self, context):
    scene = get_context().scene
    scene.frame_start = scene.frame_start_
    scene.frame_end = scene.frame_end_

    return {'FINISHED'}
