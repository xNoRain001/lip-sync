from ..libs.blender_utils import  get_data, get_operator, get_object_, get_shape_keys, get_context
from .lip_sync import shape_key_keyframe_insert

def before ():
  return

class Blink (get_operator()):
  bl_idname = "object.blink"
  bl_label = "Blink"

  def execute(self, context):
    scene = context.scene
    blink_list = scene.blink_list
    shape_key_name = scene.blink_shape_key_name
    shape_keys = get_shape_keys('Key')
    shape_key = shape_keys[shape_key_name]
    interpolation = scene.blink_interpolation
    # passing = before()

    for blink_item in blink_list:
      appearance = blink_item.appearance
      disappearance = blink_item.disappearance
      eye_opening_time_2 = blink_item.eye_opening_time_2
      eye_closing_time_2 = blink_item.eye_closing_time_2
      eye_in_betweener_frame_time_2 = blink_item.eye_in_betweener_frame_time_2
      frame = appearance + eye_opening_time_2

      while frame + eye_closing_time_2 + eye_in_betweener_frame_time_2 + 3 < disappearance:
        shape_key_keyframe_insert(shape_key, frame, 0)
        # 闭眼
        frame += eye_closing_time_2
        shape_key_keyframe_insert(shape_key, frame, 1)
        # # 3 帧后
        frame += eye_in_betweener_frame_time_2
        shape_key_keyframe_insert(shape_key, frame, 0.66)
        frame += 3
        shape_key_keyframe_insert(shape_key, frame, 0)
        frame += eye_opening_time_2
      
    return {'FINISHED'}
