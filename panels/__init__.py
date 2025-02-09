from .reload_addon import Reload_Addon
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
from .blink import (
  Blink,
  Blink_Config,
  Blink_Sub,
  Blink_Sub_Var
)

classes = (
  Reload_Addon,
  Lip_Sync,
  Lip_Sync_Sub_Vars, 
  Lip_Sync_Sub,
  Lip_Sync_Config,
  Blink,
  Blink_Config,
  Blink_Sub,
  Blink_Sub_Var
)

def register():
  register_classes(classes)

  # lip sync props
  add_scene_custom_prop('lip_sync_list', 'Collection', type = Lip_Sync_Sub_Vars)
  add_scene_custom_prop('lip_sync_list_index', 'Int')
  add_scene_custom_prop('interpolation', 'Enum', 'BEZIER', items = [
    # 标识符（Identifier）：用于在代码中引用该枚举项的字符串。
    # 名称（Name）：在用户界面中显示的字符串。
    # 描述（Description）：当用户将鼠标悬停在该项上时显示的提示信息。
    ('BEZIER', "BEZIER", ""),
    ('CONSTANT', "CONSTANT", ""),
    ('LINEAR', "LINEAR", "")
  ])
  add_scene_custom_prop('lip_sync_frame_start', 'Int', 1)
  add_scene_custom_prop('step', 'Int', 3)
  add_scene_custom_prop('shape_key_name', 'String', 'phoneme_ah')
  add_scene_custom_prop('min_frame', 'Int', 3)
  add_scene_custom_prop('frame_start_', 'Int', 1)
  add_scene_custom_prop('frame_end_', 'Int', 250)
  # 两个闭合之间如果只有 1 项打开，值给 0.5
  # 两个闭合之间如果有 2 项打开，值给 0.5 和 0.25
  # 两个闭合之间如果有 3 项打开，值给 0.33 0.66 0.33
  # 两个闭合之间如果有 4 项打开，值给 0.33 0.66 1 0.5
  add_scene_custom_prop('type_1_shape_key_value', 'Float', 0.5)
  add_scene_custom_prop('type_2_shape_key_value', 'Float', 0.5)
  add_scene_custom_prop('type_2_shape_key_value_2', 'Float', 0.25)
  add_scene_custom_prop('type_3_shape_key_value', 'Float', 0.33)
  add_scene_custom_prop('type_3_shape_key_value_2', 'Float', 0.66)
  add_scene_custom_prop('type_3_shape_key_value_3', 'Float', 0.33)
  add_scene_custom_prop('type_4_shape_key_value', 'Float', 0.33)
  add_scene_custom_prop('type_4_shape_key_value_2', 'Float', 0.66)
  add_scene_custom_prop('type_4_shape_key_value_3', 'Float', 1)
  add_scene_custom_prop('type_4_shape_key_value_4', 'Float', 0.5)
  add_scene_custom_prop('type_5_shape_key_value', 'Float', 0.33)
  add_scene_custom_prop('type_5_shape_key_value_2', 'Float', 0.66)
  add_scene_custom_prop('type_5_shape_key_value_3', 'Float', 1)
  add_scene_custom_prop('type_5_shape_key_value_4', 'Float', 0.66)
  add_scene_custom_prop('type_5_shape_key_value_5', 'Float', 0.33)
  add_scene_custom_prop('smart_mode', 'Bool', False)
  add_scene_custom_prop('lip_sync_shape_key_value', 'Float', 0.5)
  add_scene_custom_prop('lip_sync_shape_key', 'String', 'Key')

  # blink props
  add_scene_custom_prop('blink_list', 'Collection', type = Blink_Sub_Var)
  add_scene_custom_prop('blink_list_index', 'Int')
  add_scene_custom_prop('blink_interpolation', 'Enum', 'BEZIER', items = [
    ('BEZIER', "BEZIER", ""),
    ('CONSTANT', "CONSTANT", ""),
    ('LINEAR', "LINEAR", "")
  ])
  add_scene_custom_prop('eye_opening_time', 'Int', 36)
  add_scene_custom_prop('eye_closing_time', 'Int', 3)
  # 偏向闭眼，2/3 位置
  add_scene_custom_prop('eye_in_betweener_frame_time', 'Int', 3)
  add_scene_custom_prop('blink_shape_key_name', 'String', 'eye_blink')

def unregister():
  unregister_classes(classes)
  remove_scene_custom_prop('lip_sync_list')
  remove_scene_custom_prop('lip_sync_list_index')
  remove_scene_custom_prop('interpolation')
  remove_scene_custom_prop('lip_sync_frame_start')
  remove_scene_custom_prop('step')
  remove_scene_custom_prop('shape_key_name')
  remove_scene_custom_prop('min_frame')
