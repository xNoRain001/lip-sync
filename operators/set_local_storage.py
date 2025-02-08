import json

from ..libs.blender_utils import get_operator, get_utils, get_data
from ..const import lip_sync_text_name

class Set_Local_Storage (get_operator()):
  bl_label = "Set Local Storage"
  bl_idname = "my_ui.set_local_storage"

  def execute(self, context):
    my_list = context.scene.my_list
    l = []
    
    for item in my_list:
      l.append([item.int_value, item.enum_value, item.float_value])

    text_name = lip_sync_text_name
    texts = get_data().texts
    text = texts[text_name] if text_name in texts else texts.new(name=text_name)
    text.clear()
    text.write(json.dumps(l, indent = 2))

    return {'FINISHED'}
  