from ..libs.blender_utils import  (
  get_data, get_operator, get_object_, get_shape_keys, get_context
)
from .lip_sync import shape_key_keyframe_insert

def before ():
  return

def get_next_circle_start_frame (
  frame, 
  eye_opening_time,
  eye_closing_time,
  eye_in_betweener_frame_time
):
  return (
    frame + 
    eye_opening_time + 
    eye_closing_time + 
    eye_in_betweener_frame_time + 
    3
  )

def keyframe_insert (blink_list, shape_key, eyebrow_shape_key):
  for blink_item in blink_list:
    appearance = blink_item.appearance
    disappearance = blink_item.disappearance
    eye_opening_time = blink_item.eye_opening_time
    eye_closing_time = blink_item.eye_closing_time
    eye_in_betweener_frame_time = blink_item.eye_in_betweener_frame_time
    frame = appearance

    while (
      frame + 
      eye_opening_time + 
      eye_closing_time + 
      eye_in_betweener_frame_time + 
      3
    ) < disappearance :
      frame += eye_opening_time
      # 睁眼
      shape_key_keyframe_insert(shape_key, frame, 0)
      shape_key_keyframe_insert(eyebrow_shape_key, frame, 0)

      frame += eye_closing_time
      # 闭眼
      shape_key_keyframe_insert(shape_key, frame, 1)
      shape_key_keyframe_insert(eyebrow_shape_key, frame, 1)

      frame += eye_in_betweener_frame_time
      # 中割
      shape_key_keyframe_insert(shape_key, frame, 0.66)
      shape_key_keyframe_insert(eyebrow_shape_key, frame, 0.66)

      frame += 3
      # 睁眼
      shape_key_keyframe_insert(shape_key, frame, 0)
      shape_key_keyframe_insert(eyebrow_shape_key, frame, 0)

class Blink (get_operator()):
  bl_idname = "object.blink"
  bl_label = "Blink"

  def execute(self, context):
    scene = context.scene
    blink_list = scene.blink_list
    shape_key_name = scene.blink_shape_key_name
    blink_eyebrow_shape_key_name = scene.blink_eyebrow_shape_key_name
    shape_keys = get_shape_keys('Key')
    shape_key = shape_keys[shape_key_name]
    eyebrow_shape_key = shape_keys[blink_eyebrow_shape_key_name]
    
    blink_interpolation = scene.blink_interpolation
    # passing = before()

    keyframe_insert(blink_list, shape_key, eyebrow_shape_key)
      
    return {'FINISHED'}
