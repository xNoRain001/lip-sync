from ..libs.blender_utils import add_scene_custom_prop

from ..const import lip_sync_list_index
from ..panels.lip_sync import Lip_Sync_Sub_Vars

def add_lip_sync ():
  add_scene_custom_prop('lip_sync_list', 'Collection', type = Lip_Sync_Sub_Vars)
  add_scene_custom_prop(lip_sync_list_index, 'Int')
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
  add_scene_custom_prop('smart_mode', 'Bool', True)
  add_scene_custom_prop('lip_sync_shape_key_value', 'Float', 0.5)
  add_scene_custom_prop('lip_sync_shape_key', 'String', 'Key')
