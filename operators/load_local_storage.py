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
      if prop == 'text':
        setattr(item, prop, lip_sync_item['name'])
      if prop == 'frame':
        setattr(item, prop, lip_sync_item['int_value'])
      if prop == 'open':
        v = True if lip_sync_item['enum_value'] == 'open' else False
        setattr(item, prop, v)
        # setattr(item, prop, lip_sync_item['enum_value'])
      if prop == 'shape_key_value':
        setattr(item, prop, lip_sync_item['float_value'])
      
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
  