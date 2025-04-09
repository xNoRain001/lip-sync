from ..libs.blender_utils import add_scene_custom_prop

def add_blink ():
  add_scene_custom_prop(
    'blink_type', 
    'Enum', 
    default = '日式',
    items = [
      ('日式', '日式', ''),
      ('欧美式', '欧美式', '')
    ]
  )
  add_scene_custom_prop('blink_frame_start', 'Int', 1)
  add_scene_custom_prop('blink_frame_end', 'Int', 100)
  add_scene_custom_prop('blink_frequency', 'Int', 72)
  add_scene_custom_prop('blink_shape_key', 'String', 'Key.002')
  add_scene_custom_prop('blink_key_block', 'String', 'Eye_WinkA_R')
