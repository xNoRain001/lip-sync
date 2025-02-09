import json

from ..libs.blender_utils import get_operator, get_utils, get_data
from .lip_sync_crud import add_lip_sync
from ..const import lip_sync_text_name
from ..panels.lip_sync import Lip_Sync_Sub_Vars

def load_lip_sync (context, lip_sync_data):
  scene = context.scene
  lip_sync_list = scene.lip_sync_list
  custom_props = Lip_Sync_Sub_Vars.__annotations__.keys()

  for lip_sync_item in lip_sync_data:
    item = lip_sync_list.add()

    for prop in custom_props:
      setattr(item, prop, lip_sync_item[prop])
      
    scene.lip_sync_list_index = len(lip_sync_data) - 1

class Load_Local_Storage (get_operator()):
  bl_label = "Load Local Storage"
  bl_idname = "object.load_local_storage"

  def execute(self, context):
    text_name = lip_sync_text_name
    texts = get_data().texts

    if text_name in texts:
      text = texts[text_name]
      lip_sync_data = json.loads(text.as_string())
      load_lip_sync(context, lip_sync_data)
      context.scene.lip_sync_list_index = len(lip_sync_data) - 1
      self.report({'INFO'}, '导入完成')
    else:
      self.report({'WARNING'}, '本地数据不存在')

    return {'FINISHED'}
  