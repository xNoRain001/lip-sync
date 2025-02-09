import json

from ..libs.blender_utils import get_operator, get_utils, get_data
from ..const import lip_sync_text_name
from ..panels.lip_sync import Lip_Sync_Sub_Vars

class Set_Local_Storage (get_operator()):
  bl_label = "Set Local Storage"
  bl_idname = "object.set_local_storage"

  def execute(self, context):
    # python 3.6(+) 返回的列表中元素的顺序和定义时保持一致
    custom_props = Lip_Sync_Sub_Vars.__annotations__.keys()
   
    lip_sync_list = context.scene.lip_sync_list
    lip_sync_data = []
    
    for item in lip_sync_list:
      helper = {}

      for prop in custom_props:
        helper[prop] = getattr(item, prop)
      
      lip_sync_data.append(helper)

    text_name = lip_sync_text_name
    texts = get_data().texts
    text = None

    if text_name in texts:
      text = texts[text_name]
      text.clear()
    else:
      text = texts.new(name = text_name)

    text.write(json.dumps(lip_sync_data, indent = 2))

    return {'FINISHED'}
  