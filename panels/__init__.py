from .reload_addon import VIEW3D_PT_reload_addon
from ..const import lip_sync_list_index
from ..libs.blender_utils import (
  register_classes, 
  unregister_classes, 
  add_scene_custom_prop,
  remove_scene_custom_prop
)
from .lip_sync import (
  Lip_Sync, 
  Lip_Sync_Sub_Vars, 
  Lip_Sync_Sub,
  Lip_Sync_Config,
)
from .blink import VIEW3D_PT_blink

classes = (
  VIEW3D_PT_reload_addon,
  Lip_Sync,
  Lip_Sync_Sub_Vars, 
  Lip_Sync_Sub,
  Lip_Sync_Config,
  VIEW3D_PT_blink,
)

def register():
  register_classes(classes)

def unregister():
  unregister_classes(classes)
