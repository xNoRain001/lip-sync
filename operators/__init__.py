from .reload_addon import Reload_Addon
from .set_local_storage import Set_Local_Storage
from .load_local_storage import Load_Local_Storage
from .lip_sync import Lip_Sync
from .crud import (
  Add_Sub,
  Clear_Empty_Subs,
  Clear_Subs,
  Move_Sub,
  Delete_Sub,
  Copy_Sub,
  Add_Open_Sub,
  Add_Mid_Sub,
  Add_Close_Sub
)
from ..libs.blender_utils import register_classes, unregister_classes

classes = (
  Reload_Addon,
  Add_Sub,
  Clear_Empty_Subs,
  Clear_Subs,
  Move_Sub,
  Delete_Sub,
  Copy_Sub,
  Add_Open_Sub,
  Add_Mid_Sub,
  Add_Close_Sub,
  Set_Local_Storage,
  Load_Local_Storage,
  Lip_Sync,
)

def register():
  register_classes(classes)

def unregister():
  unregister_classes(classes)
