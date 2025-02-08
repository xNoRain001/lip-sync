from .reload_addon import Reload_Addon
from ..libs.blender_utils import register_classes, unregister_classes, remove_scene_custom_prop
from .lip_sync import (
  Lip_Sync, 
  Lip_Sync_Sub_Vars, 
  Lip_Sync_Sub,
  Lip_Sync_Config
)
from ..libs.blender_utils import add_scene_custom_prop

classes = (
  Reload_Addon,
  Lip_Sync,
  Lip_Sync_Sub_Vars, 
  Lip_Sync_Sub,
  Lip_Sync_Config
)

def register():
  register_classes(classes)
  add_scene_custom_prop('my_list', 'Collection', type = Lip_Sync_Sub_Vars)
  add_scene_custom_prop('my_list_index', 'Int')
  add_scene_custom_prop('interpolation', 'Enum', 'bezier', items = [
    ('bezier', "BEZIER", ""),
    ('constant', "CONSTANT", ""),
    ('linear', "LINEAR", "")
  ])
  add_scene_custom_prop('lip_sync_frame_start', 'Int', 1)
  add_scene_custom_prop('step', 'Int', 3)
  add_scene_custom_prop('shape_key_name', 'String', 'phoneme_ah')
  add_scene_custom_prop('min_frame', 'Int', 3)
  add_scene_custom_prop('frame_start_', 'Int', 1)
  add_scene_custom_prop('frame_end_', 'Int', 250)

def unregister():
  unregister_classes(classes)
  remove_scene_custom_prop('my_list')
  remove_scene_custom_prop('my_list_index')
  remove_scene_custom_prop('interpolation')
  remove_scene_custom_prop('lip_sync_frame_start')
  remove_scene_custom_prop('step')
  remove_scene_custom_prop('shape_key_name')
  remove_scene_custom_prop('min_frame')
