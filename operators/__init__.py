from .reload_addon import Reload_Addon
from .set_local_storage import Set_Local_Storage
from .load_local_storage import Load_Local_Storage
from .lip_sync import Lip_Sync
from .crud import (
  MYUI_OT_AddRows,
  MYUI_OT_ClearEmptyRows,
  MYUI_OT_ClearRows,
  MY_OT_move_item,
  MY_OT_delete_item,
  MY_OT_new_item,
  Add_Open,
  Add_Mid,
  Add_Close,
)
from ..libs.blender_utils import register_classes, unregister_classes

classes = (
  Reload_Addon,
  MYUI_OT_AddRows,
  MYUI_OT_ClearEmptyRows,
  MYUI_OT_ClearRows,
  MY_OT_move_item,
  MY_OT_delete_item,
  MY_OT_new_item,
  Add_Open,
  Add_Mid,
  Add_Close,
  Set_Local_Storage,
  Load_Local_Storage,
  Lip_Sync
)

def register():
  register_classes(classes)

def unregister():
  unregister_classes(classes)
