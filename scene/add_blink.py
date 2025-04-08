from ..libs.blender_utils import add_scene_custom_prop

def add_blink ():
  add_scene_custom_prop('appearance', 'Int', 1)
  add_scene_custom_prop('disappearance', 'Int', 100)
  # blink props
  add_scene_custom_prop('blink_interpolation', 'Enum', 'BEZIER', items = [
    ('BEZIER', "BEZIER", ""),
    ('CONSTANT', "CONSTANT", ""),
    ('LINEAR', "LINEAR", "")
  ])
  add_scene_custom_prop('eye_step', 'Int', 72)
  add_scene_custom_prop('eye_opening_time', 'Int', 3)
  add_scene_custom_prop('eye_closing_time', 'Int', 3)
  # 偏向闭眼，2/3 位置
  add_scene_custom_prop('eye_in_betweener_frame_time', 'Int', 3)
  add_scene_custom_prop('blink_shape_key', 'String', 'Key.002')
  add_scene_custom_prop('blink_key_block', 'String', 'Eye_WinkA_R')
