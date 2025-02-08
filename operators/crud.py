from ..panels.lip_sync import get_float_value
from ..libs.blender_utils import (
  get_operator,
  get_props
)

def add_lip_sync (
  context, 
  int_value = None, 
  enum_value = 'open', 
  float_value = None,
  name = '',
  load = False
):
  scene = context.scene
  step = scene.step
  my_list = scene.my_list
  item = my_list.add()
  item.enum_value = enum_value
  item.name = name

  if load:
    item.int_value = int_value
    item.float_value = float_value
  else:
    # 当原先本来就有数据时，起始帧在原先的基础上加上间隔
    l = len(my_list)
    int_value = (
      my_list[-2].int_value + step if l > 1 else scene.lip_sync_frame_start
    )
    item.int_value = int_value
    item.float_value = get_float_value(enum_value)
    # 让新增加的被选中
    scene.my_list_index = l - 1
 
def copy_lip_sync (context):
  scene = context.scene
  my_list = scene.my_list
  my_list_index = scene.my_list_index
  
  if my_list_index > -1:
    item = my_list.add()
    source = my_list[my_list_index]
    item.float_value = source.float_value
    item.enum_value = source.enum_value
    item.int_value = source.int_value
    # item.name = source.name
    # 移动到复制对象下方
    index = my_list_index + 1
    my_list.move(len(my_list) - 1, index)
    scene.my_list_index = index

class Copy_Sub (get_operator()):
  bl_idname = "my_ui.copy"
  bl_label = "Copy"

  def execute(self, context):
    copy_lip_sync(context)

    return {'FINISHED'}

class Add_Open_Sub (get_operator()):
  bl_idname = "my_ui.add_open"
  bl_label = "Add Open"

  def execute(self, context):
    add_lip_sync(context, enum_value = 'open')

    return {'FINISHED'}
  
class Add_Mid_Sub (get_operator()):
  bl_idname = "my_ui.add_mid"
  bl_label = "Add Mid"

  def execute(self, context):
    add_lip_sync(context, enum_value = 'mid')

    return {'FINISHED'}
  
class Add_Close_Sub (get_operator()):
  bl_idname = "my_ui.add_close"
  bl_label = "Add Close"

  def execute(self, context):
    add_lip_sync(context, enum_value = 'close')

    return {'FINISHED'}

class Clear_Subs (get_operator()):
  bl_idname = "my_ui.clear_rows"
  bl_label = "Clear Rows"

  def execute(self, context):
    scene = context.scene
    my_list = scene.my_list
    my_list.clear()

    return {'FINISHED'}
  
class Clear_Empty_Subs (get_operator()):
  bl_idname = "my_ui.clear_empty_rows"
  bl_label = "Clear Empty Rows"

  def execute(self, context):
    scene = context.scene
    my_list = scene.my_list

    return {'FINISHED'}
  
class Add_Sub (get_operator()):
  bl_idname = "my_list.new_item"
  bl_label = "Add a new item"

  def execute(self, context):
    add_lip_sync(context)

    return {'FINISHED'}

class Delete_Sub (get_operator()):
  bl_idname = "my_list.delete_item"
  bl_label = "Delete an item"

  def execute(self, context):
    scene = context.scene
    my_list = scene.my_list
    index = scene.my_list_index

    my_list.remove(index)
    scene.my_list_index = min(max(0, index - 1), len(my_list) - 1)
    return {'FINISHED'}

class Move_Sub (get_operator()):
  bl_idname = "my_list.move_item"
  bl_label = "Move an item"
  direction: get_props().EnumProperty(items=(('UP', "Up", ""), ('DOWN', "Down", "")))

  def execute(self, context):
    scene = context.scene
    my_list = scene.my_list
    index = scene.my_list_index

    if self.direction == 'UP' and index > 0:
        my_list.move(index, index - 1)
        scene.my_list_index -= 1
    elif self.direction == 'DOWN' and index < len(my_list) - 1:
        my_list.move(index, index + 1)
        scene.my_list_index += 1

    return {'FINISHED'}
