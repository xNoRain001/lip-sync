from ..libs.blender_utils import  get_operator, get_key_block

from .lip_sync import shape_key_keyframe_insert

def key_block_insert_keyframe (scene):
  japanese = scene.blink_type == '日式'
  time = 3 if japanese else 2
  eye_opening_time = eye_closing_time = eye_in_betweener_frame_time = time
  blink_shape_key = scene.blink_shape_key
  blink_key_block = scene.blink_key_block
  blink_frame_start = scene.blink_frame_start
  blink_frame_end = scene.blink_frame_end
  blink_frequency = scene.blink_frequency
  frame = blink_frame_start
  key_block = get_key_block(blink_shape_key, blink_key_block)

  while (
    frame + 
    blink_frequency + 
    eye_closing_time + 
    eye_in_betweener_frame_time + 
    eye_opening_time
  ) < blink_frame_end :
    # 下一帧开始闭眼
    frame += blink_frequency
    shape_key_keyframe_insert(key_block, frame, 0)

    if not japanese:
      # 闭眼前 2 帧多出一张 2 / 3 闭眼
      frame += 2
      shape_key_keyframe_insert(key_block, frame, 0.66)

    # 完全闭眼
    frame += eye_closing_time
    shape_key_keyframe_insert(key_block, frame, 1)

    # 中割，2 / 3 睁眼
    frame += eye_in_betweener_frame_time
    shape_key_keyframe_insert(key_block, frame, 0.33)

    # 完全睁眼
    frame += eye_opening_time
    shape_key_keyframe_insert(key_block, frame, 0)

class OBJECT_OT_blink (get_operator()):
  bl_idname = "object.blink"
  bl_label = "Blink"

  def execute(self, context):
    key_block_insert_keyframe(context.scene)
      
    return {'FINISHED'}
