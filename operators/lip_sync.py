from ..libs.blender_utils import get_operator

class Lip_Sync (get_operator()):
  bl_idname = "my_ui.lip_sync"
  bl_label = "Lip Sync"

  def execute(self, context):
    print('a')
    return {'FINISHED'}
