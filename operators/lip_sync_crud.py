from ..panels.lip_sync import get_shape_key_value
from ..libs.blender_utils import (
  get_operator,
  get_props
)

def add_lip_sync (
  context, 
  frame = None, 
  text = '',
  open = True
):
  scene = context.scene
  step = scene.step
  lip_sync_list = scene.lip_sync_list
  lip_sync_frame_start = scene.lip_sync_frame_start
  lip_sync_shape_key_value = scene.lip_sync_shape_key_value
  item = lip_sync_list.add()
  l = len(lip_sync_list)
  frame = lip_sync_list[-2].frame + step if l > 1 else lip_sync_frame_start
  # TODO: delete
  item.open = open
  item.text = text
  # 当原先本来就有数据时，起始帧在原先的基础上加上间隔
  item.frame = frame
  item.shape_key_value = get_shape_key_value(open, lip_sync_shape_key_value)
  # 让新增加的被选中
  scene.lip_sync_list_index = l - 1
 
def copy_lip_sync (context):
  scene = context.scene
  lip_sync_list = scene.lip_sync_list
  lip_sync_list_index = scene.lip_sync_list_index
  
  if lip_sync_list_index > -1:
    item = lip_sync_list.add()
    source = lip_sync_list[lip_sync_list_index]
    item.shape_key_value = source.shape_key_value
    item.open = source.open
    item.frame = source.frame
    # item.text = source.text
    # 移动到复制对象下方
    index = lip_sync_list_index + 1
    lip_sync_list.move(len(lip_sync_list) - 1, index)
    scene.lip_sync_list_index = index

class Copy_Sub (get_operator()):
  bl_idname = "object.copy"
  bl_label = "Copy"

  def execute(self, context):
    copy_lip_sync(context)

    return {'FINISHED'}

class Add_Open_Sub (get_operator()):
  bl_idname = "object.add_open"
  bl_label = "Add Open"

  def execute(self, context):
    add_lip_sync(context, open = True)

    return {'FINISHED'}
  
class Add_Close_Sub (get_operator()):
  bl_idname = "object.add_close"
  bl_label = "Add Close"

  def execute(self, context):
    add_lip_sync(context, open = False)

    return {'FINISHED'}

class Clear_Subs (get_operator()):
  bl_idname = "object.clear_rows"
  bl_label = "Clear Rows"

  def execute(self, context):
    scene = context.scene
    lip_sync_list = scene.lip_sync_list
    lip_sync_list.clear()

    return {'FINISHED'}
  
class Clear_Empty_Subs (get_operator()):
  bl_idname = "object.clear_empty_rows"
  bl_label = "Clear Empty Rows"

  def execute(self, context):
    scene = context.scene
    lip_sync_list = scene.lip_sync_list

    return {'FINISHED'}

class Delete_Sub (get_operator()):
  bl_idname = "lip_sync_list.delete_item"
  bl_label = "Delete an item"

  def execute(self, context):
    scene = context.scene
    lip_sync_list = scene.lip_sync_list
    index = scene.lip_sync_list_index

    lip_sync_list.remove(index)
    scene.lip_sync_list_index = min(max(0, index - 1), len(lip_sync_list) - 1)
    return {'FINISHED'}

class Move_Sub (get_operator()):
  bl_idname = "lip_sync_list.move_item"
  bl_label = "Move an item"
  direction: get_props().EnumProperty(items=(('UP', "Up", ""), ('DOWN', "Down", "")))

  def execute(self, context):
    scene = context.scene
    lip_sync_list = scene.lip_sync_list
    index = scene.lip_sync_list_index

    if self.direction == 'UP' and index > 0:
        lip_sync_list.move(index, index - 1)
        scene.lip_sync_list_index -= 1
    elif self.direction == 'DOWN' and index < len(lip_sync_list) - 1:
        lip_sync_list.move(index, index + 1)
        scene.lip_sync_list_index += 1

    return {'FINISHED'}
