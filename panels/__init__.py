from .reload_addon import Reload_Addon
from ..libs.blender_utils import register_classes, unregister_classes
from .lip_sync import (
  # MyUIListItem, 
  MyUIPanel, 
  MyPropertyGroup, 
  MY_UL_items
)
from ..libs.blender_utils import add_scene_custom_prop

classes = (
  Reload_Addon,
  # MyUIListItem, 
  MyUIPanel,
  MyPropertyGroup, 
  MY_UL_items
)

import bpy
def register():
  register_classes(classes)
  # add_scene_custom_prop('my_ui_list', 'Collection', type = MyUIListItem)
  bpy.types.Scene.my_list = bpy.props.CollectionProperty(type=MyPropertyGroup)
  bpy.types.Scene.my_list_index = bpy.props.IntProperty()
  
def unregister():
  unregister_classes(classes)
  # del bpy.types.Scene.my_ui_list
