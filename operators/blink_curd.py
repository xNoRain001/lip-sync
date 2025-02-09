from ..panels.lip_sync import get_shape_key_value
from ..libs.blender_utils import (
  get_operator,
  get_props
)

def add_blink (
  context, 
  appearance = 0, 
  disappearance = 0, 
  eye_opening_time_2 = 36,
  eye_closing_time_2 = 3,
  eye_in_betweener_frame_time_2 = 3,
  load = False
):
  scene = context.scene
  blink_list = scene.blink_list
  item = blink_list.add()
  item.disappearance = disappearance
  item.eye_opening_time_2 = eye_opening_time_2
  item.eye_closing_time_2 = eye_closing_time_2
  item.eye_in_betweener_frame_time_2 = eye_in_betweener_frame_time_2

  if load:
    item.appearance = blink_list.appearance
  else:
    # 当原先本来就有数据时，起始帧在原先的基础上加上间隔
    l = len(blink_list)
    appearance = scene.frame_current
    item.appearance = appearance
    # 让新增加的被选中
    scene.blink_list_index = l - 1
 
def copy_blink (context):
  scene = context.scene
  blink_list = scene.blink_list
  blink_list_index = scene.blink_list_index
  
  if blink_list_index > -1:
    item = blink_list.add()
    source = blink_list[blink_list_index]

    item.appearance = source.disappearance
    item.disappearance = source.disappearance
    item.eye_opening_time_2 = source.eye_opening_time_2
    item.eye_closing_time_2 = source.eye_closing_time_2
    item.eye_in_betweener_frame_time_2 = source.eye_in_betweener_frame_time_2
    # item.name = source.name
    # 移动到复制对象下方
    index = blink_list_index + 1
    blink_list.move(len(blink_list) - 1, index)
    scene.blink_list_index = index

class Copy_Blink_Sub (get_operator()):
  bl_idname = "object.copy_blink_sub"
  bl_label = "Copy Blink Sub"

  def execute(self, context):
    copy_blink(context)

    return {'FINISHED'}

class Clear_Blink_Subs (get_operator()):
  bl_idname = "object.clear_blink_subs"
  bl_label = "Clear Blink Subs"

  def execute(self, context):
    scene = context.scene
    blink_list = scene.blink_list
    blink_list.clear()

    return {'FINISHED'}
  
class Clear_Empty_Blink_Subs (get_operator()):
  bl_idname = "object.clear_empty_blink_subs"
  bl_label = "Clear Empty Blink Subs"

  def execute(self, context):
    scene = context.scene
    blink_list = scene.blink_list

    return {'FINISHED'}
  
class Add_Blink_Sub (get_operator()):
  bl_idname = "object.add_blink_sub"
  bl_label = "Add Blink Sub"

  def execute(self, context):
    add_blink(context)

    return {'FINISHED'}

class Delete_Blink_Sub (get_operator()):
  bl_idname = "object.delete_blink_sub"
  bl_label = "Delete Blink Sub"

  def execute(self, context):
    scene = context.scene
    blink_list = scene.blink_list
    index = scene.blink_list_index

    blink_list.remove(index)
    scene.blink_list_index = min(max(0, index - 1), len(blink_list) - 1)
    return {'FINISHED'}

class Move_Blink_Sub (get_operator()):
  bl_idname = "object.move_blink_sub"
  bl_label = "Move Blink Sub"
  direction: get_props().EnumProperty(items=(('UP', "Up", ""), ('DOWN', "Down", "")))

  def execute(self, context):
    scene = context.scene
    blink_list = scene.blink_list
    index = scene.blink_list_index

    if self.direction == 'UP' and index > 0:
        blink_list.move(index, index - 1)
        scene.blink_list_index -= 1
    elif self.direction == 'DOWN' and index < len(blink_list) - 1:
        blink_list.move(index, index + 1)
        scene.blink_list_index += 1

    return {'FINISHED'}
