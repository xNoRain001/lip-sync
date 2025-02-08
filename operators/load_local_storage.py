import json

from ..libs.blender_utils import get_operator, get_utils, get_data
from .crud import add_lip_sync
from ..const import lip_sync_text_name

class Load_Local_Storage (get_operator()):
  bl_label = "Load Local Storage"
  bl_idname = "my_ui.load_local_storage"

  def execute(self, context):
    text_name = lip_sync_text_name
    texts = get_data().texts

    if text_name in texts:
      text = texts[text_name]
      list = json.loads(text.as_string())

      for item in list:
        add_lip_sync(context, item[0], item[1], item[2], True)

    return {'FINISHED'}
  