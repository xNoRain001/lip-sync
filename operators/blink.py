from ..libs.blender_utils import  get_operator, get_key_block

from .lip_sync import shape_key_keyframe_insert

def key_block_insert_keyframe (scene):
  blink_shape_key = scene.blink_shape_key
  blink_key_block = scene.blink_key_block
  blink_interpolation = scene.blink_interpolation
  appearance = scene.appearance
  disappearance = scene.disappearance
  eye_step = scene.eye_step
  eye_opening_time = scene.eye_opening_time
  eye_closing_time = scene.eye_closing_time
  eye_in_betweener_frame_time = scene.eye_in_betweener_frame_time
  frame = appearance
  key_block = get_key_block(blink_shape_key, blink_key_block)

  while (
    frame + 
    eye_step + 
    eye_closing_time + 
    eye_in_betweener_frame_time + 
    eye_opening_time
  ) < disappearance :
    # 下一帧开始闭眼
    frame += eye_step
    shape_key_keyframe_insert(key_block, frame, 0)

    # 完全闭眼
    frame += eye_closing_time
    shape_key_keyframe_insert(key_block, frame, 1)

    # 中割
    frame += eye_in_betweener_frame_time
    shape_key_keyframe_insert(key_block, frame, 0.66)

    # 完全睁眼
    frame += eye_opening_time
    shape_key_keyframe_insert(key_block, frame, 0)

class OBJECT_OT_blink (get_operator()):
  bl_idname = "object.blink"
  bl_label = "Blink"

  def execute(self, context):
    key_block_insert_keyframe(context.scene)
      
    return {'FINISHED'}
