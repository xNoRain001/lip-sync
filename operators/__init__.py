from .reload_addon import OBJECT_OT_reload_addon
from .set_local_storage import Set_Local_Storage
from .load_local_storage import Load_Local_Storage
from .lip_sync import Lip_Sync
from .set_frame_range import Set_Frame_Range
from .blink import OBJECT_OT_blink
from .lip_sync_crud import (
  Clear_Empty_Subs,
  Clear_Subs,
  Move_Sub,
  Delete_Sub,
  Copy_Sub,
  Add_Open_Sub,
  Add_Close_Sub
)
from ..libs.blender_utils import register_classes, unregister_classes

classes = (
  OBJECT_OT_reload_addon,
  Clear_Empty_Subs,
  Clear_Subs,
  Move_Sub,
  Delete_Sub,
  Copy_Sub,
  Add_Open_Sub,
  Add_Close_Sub,
  Set_Local_Storage,
  Load_Local_Storage,
  Lip_Sync,
  Set_Frame_Range,
  OBJECT_OT_blink
)

def register():
  register_classes(classes)

def unregister():
  unregister_classes(classes)
