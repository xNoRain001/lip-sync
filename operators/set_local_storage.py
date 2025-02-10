import json

from ..libs.blender_utils import get_operator, get_utils, get_data, get_props
from ..const import lip_sync_text_name, blink_text_name, lip_sync_list_index, blink_list_index
from ..panels.lip_sync import Lip_Sync_Sub_Vars
from ..panels.blink import Blink_Sub_Var

def get_info (type, context):
  list = None
  text_name = None
  index_name = None
  scene = context.scene

  if type == 'lip_sync':
    vars = Lip_Sync_Sub_Vars
    list = scene.lip_sync_list
    text_name = lip_sync_text_name
    index_name = lip_sync_list_index
  else:
    vars = Blink_Sub_Var
    list = scene.blink_list
    text_name = blink_text_name
    index_name = blink_list_index

  # python 3.6(+) 返回的列表中元素的顺序和定义时保持一致
  custom_props = vars.__annotations__.keys()

  return [custom_props, list, text_name, index_name]

def gen_obj (custom_props, list):
  obj = []
    
  for item in list:
    helper = {}

    for prop in custom_props:
      helper[prop] = getattr(item, prop)
    
    obj.append(helper)

  return obj

def get_text (text_name):
  text = None
  texts = get_data().texts

  if text_name in texts:
    text = texts[text_name]
    text.clear()
  else:
    text = texts.new(name = text_name)

  return text

class Set_Local_Storage (get_operator()):
  bl_label = "Set Local Storage"
  bl_idname = "object.set_local_storage"
  type: get_props().StringProperty()

  def execute(self, context):
    custom_props, list, text_name, _ = get_info(self.type, context)
    obj = gen_obj(custom_props, list)
    text = get_text(text_name)
    text.write(json.dumps(obj, indent = 2))

    return {'FINISHED'}
  