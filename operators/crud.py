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
  load = False
):
  scene = context.scene
  step = scene.step
  my_list = scene.my_list
  item = my_list.add()
  item.enum_value = enum_value

  if load:
    item.int_value = int_value
    item.float_value = float_value
  else:
    # 当原先本来就有数据时，起始帧在原先的基础上加上间隔
    int_value = my_list[-2].int_value + step if len(my_list) > 1 else 0
    item.int_value = int_value
    item.float_value = get_float_value(enum_value)

class MYUI_OT_AddRows(get_operator()):
  bl_idname = "my_ui.add_rows"
  bl_label = "Add 10 Rows"

  def execute(self, context):
    for _ in range(10):
      add_lip_sync(context)

    return {'FINISHED'}
  
class Add_Open (get_operator()):
  bl_idname = "my_ui.add_open"
  bl_label = "Add Open"

  def execute(self, context):
    add_lip_sync(context,  enum_value = 'open')

    return {'FINISHED'}
  
class Add_Mid (get_operator()):
  bl_idname = "my_ui.add_mid"
  bl_label = "Add Mid"

  def execute(self, context):
    add_lip_sync(context, enum_value = 'mid')

    return {'FINISHED'}
  
class Add_Close (get_operator()):
  bl_idname = "my_ui.add_close"
  bl_label = "Add Close"

  def execute(self, context):
    add_lip_sync(context, enum_value = 'close')

    return {'FINISHED'}

class MYUI_OT_ClearRows(get_operator()):
  bl_idname = "my_ui.clear_rows"
  bl_label = "Clear Rows"

  def execute(self, context):
    scene = context.scene
    my_list = scene.my_list
    my_list.clear()

    return {'FINISHED'}
  
class MYUI_OT_ClearEmptyRows(get_operator()):
  bl_idname = "my_ui.clear_empty_rows"
  bl_label = "Clear Empty Rows"

  def execute(self, context):
    scene = context.scene
    my_list = scene.my_list

    return {'FINISHED'}
  
# 定义操作来添加、删除和移动列表项
class MY_OT_new_item(get_operator()):
  bl_idname = "my_list.new_item"
  bl_label = "Add a new item"

  def execute(self, context):
    add_lip_sync(context)

    return {'FINISHED'}

class MY_OT_delete_item(get_operator()):
    bl_idname = "my_list.delete_item"
    bl_label = "Delete an item"

    def execute(self, context):
        scene = context.scene
        my_list = scene.my_list
        index = scene.my_list_index

        my_list.remove(index)
        scene.my_list_index = min(max(0, index - 1), len(my_list) - 1)
        return {'FINISHED'}

class MY_OT_move_item(get_operator()):
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
