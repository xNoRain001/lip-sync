import json

from ..libs.blender_utils import get_operator, get_utils, get_data, get_props, report_warning, report_info
from ..const import lip_sync_text_name, blink_text_name
from ..panels.lip_sync import Lip_Sync_Sub_Vars
from ..panels.blink import Blink_Sub_Var
from .set_local_storage import get_info

def get_text (text_name):
  text = None
  texts = get_data().texts

  if text_name in texts:
    text = texts[text_name]

  return text

def load_data (context, data, custom_props, list, index_name):
  scene = context.scene

  for d in data:
    item = list.add()

    for prop in custom_props:
      setattr(item, prop, d[prop])

  # 选中最后一项
  setattr(scene, index_name, len(data) - 1)

class Load_Local_Storage (get_operator()):
  bl_label = "Load Local Storage"
  bl_idname = "object.load_local_storage"
  type: get_props().StringProperty()

  def execute(self, context):
    [custom_props, list, text_name, index_name] = get_info(self.type, context)
    text = get_text(text_name)
    print(text_name)

    if text:
      data = json.loads(text.as_string())
      load_data(context, data, custom_props, list, index_name)
      self.report({'INFO'}, '导入完成')
    else:
      self.report({'WARNING'}, '本地数据不存在')

    return {'FINISHED'}
  