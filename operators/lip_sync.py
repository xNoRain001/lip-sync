from ..libs.blender_utils import  get_data, get_operator, get_object_, get_shape_keys, get_context

def set_constant (index_list):
  action = get_data().actions.get("Key动作")
  keyframe_points = action.fcurves[0].keyframe_points

  for keyframe_point in keyframe_points:
    keyframe_point.interpolation = 'BEZIER'

  for i in index_list:
    keyframe_points[i].interpolation = 'CONSTANT'
    # keyframe_points[i + 1].interpolation = 'BEZIER'

class Lip_Sync (get_operator()):
  bl_idname = "my_ui.lip_sync"
  bl_label = "Lip Sync"

  def execute(self, context):
    scene = context.scene
    my_list = scene.my_list
    shape_key_name = scene.shape_key_name
    shape_keys = get_shape_keys('Key')
    shape_key = shape_keys[shape_key_name]
    index_list = []

    last_index = len(my_list) - 1
    for index, item in enumerate(my_list):
      frame = item.int_value
      value = item.float_value
      enum_value = item.enum_value
      shape_key.value = value
      shape_key.keyframe_insert(data_path = "value", frame = frame)

      if (
        enum_value == 'close' and 
        index < last_index and 
        my_list[index + 1].int_value - frame > 3
      ):
        index_list.append(index)

    set_constant(index_list)

    return {'FINISHED'}
