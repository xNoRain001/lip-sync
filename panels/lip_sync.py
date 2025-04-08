from ..libs.blender_utils import (
  get_panel, 
  add_scene_custom_prop,
  add_row_with_operator,
  add_row_with_label_and_operator,
  add_row_with_label,
  add_row,
  get_operator,
  get_property_group,
  get_props,
  get_utils,
  get_ui_list,
  get_data
)

from ..const import bl_category

def get_shape_key_value (open, lip_sync_shape_key_value):
  shape_key_value = lip_sync_shape_key_value if open else 0

  return shape_key_value

# 两次选中同一项也会触发
def on_update(self, context):
  self.shape_key_value = get_shape_key_value(self.open, context.scene.lip_sync_shape_key_value)
  
# 定义一个自定义属性组
class Lip_Sync_Sub_Vars (get_property_group()):
  # 用于占位，其他属性有控件，不好进行选择
  text: get_props().StringProperty(name="text")
  frame: get_props().IntProperty(name="frame")
  open: get_props().BoolProperty(name="open", update=on_update, default = True)
  shape_key_value: get_props().FloatProperty(name="shape_key_value", min=0.0, max=1.0)

class Lip_Sync_Sub (get_ui_list()):
  bl_label = "Lip Sync Sub"
  bl_idname = "OBJECT_UL_Lip_Sync_Sub"

  def draw_item(
    self, 
    context, 
    layout, 
    data, 
    item, 
    icon, 
    active_data, 
    active_propname,
    index
  ):
    common = { 'text': '', 'emboss': False }
    row = layout.row()
    row.prop(item, "frame", **common)
    # 开启 emboss 会导致复选框就看不见了
    row.prop(item, "open", text = '打开' if item.open else '闭合')
    row.prop(item, "shape_key_value", **common)
    row.prop(item, "text", **common)

import bpy
class Lip_Sync_Config (get_panel()):
  bl_label = "Lip Sync Config"
  bl_idname = "OBJECT_PT_Lip_Config"
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category

  def draw(self, context):
    layout = self.layout
    scene = context.scene
    box = layout.box()

    row = box.row()
    row.label(text = '每一拍帧数')
    row.prop(scene, 'step', text = '')

    data = get_data()
    row = box.row()
    row.label(text = '形态键')
    row.prop_search(scene, 'lip_sync_shape_key', data, 'shape_keys', text = '')

    lip_sync_shape_key = scene.lip_sync_shape_key

    if lip_sync_shape_key:
      row = box.row()
      row.label(text = '音素形态键')
      row.prop_search(
        scene, 
        'shape_key_name', 
        data.shape_keys[lip_sync_shape_key], 
        'key_blocks', 
        text = ''
      )

    row = box.row()
    row.label(text = '打开默认值')
    row.prop(scene, 'lip_sync_shape_key_value', text = '')
    row = box.row()
    row.label(text = '插值')
    row.prop(scene, 'interpolation', text = '')
    row = box.row()
    row.label(text = '闭口帧数')
    row.prop(scene, 'min_frame', text = '')
    row = box.row()
    row.label(text = '智能模式')
    row.prop(scene, 'smart_mode', text = '')
    row = box.row()
    row.label(text = '打开一次')
    row.prop(scene, 'type_1_shape_key_value', text = '')
    row = box.row()
    row.label(text = '打开两次')
    row.prop(scene, 'type_2_shape_key_value', text = '')
    row.prop(scene, 'type_2_shape_key_value_2', text = '')
    row = box.row()
    row.label(text = '打开三次')
    row.prop(scene, 'type_3_shape_key_value', text = '')
    row.prop(scene, 'type_3_shape_key_value_2', text = '')
    row.prop(scene, 'type_3_shape_key_value_3', text = '')
    row = box.row()
    row.label(text = '打开四次')
    row.prop(scene, 'type_4_shape_key_value', text = '')
    row.prop(scene, 'type_4_shape_key_value_2', text = '')
    row.prop(scene, 'type_4_shape_key_value_3', text = '')
    row.prop(scene, 'type_4_shape_key_value_4', text = '')
    row = box.row()
    row.label(text = '打开五次')
    row.prop(scene, 'type_5_shape_key_value', text = '')
    row.prop(scene, 'type_5_shape_key_value_2', text = '')
    row.prop(scene, 'type_5_shape_key_value_3', text = '')
    row.prop(scene, 'type_5_shape_key_value_4', text = '')
    row.prop(scene, 'type_5_shape_key_value_5', text = '')
  
class Lip_Sync (get_panel()):
  bl_label = "Lip Sync"
  bl_idname = "OBJECT_PT_Lip_Sync"
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category

  def draw(self, context):
    layout = self.layout
    scene = context.scene

    # row = layout.row()
    # row.operator("object.set_local_storage", text="Local Storagge")
    # row.operator("object.load_local_storage", text="Load Local Storagge")

    # row = layout.row()
    # row.label(text="帧")
    # row.label(text="状态")
    # row.label(text="形态键值")
    # row.label(text="文本")
    row = layout.row()
    row.prop(scene, "frame_start_", text = '起始')
    row.prop(scene, "frame_end_", text = '结束')
    row.operator("object.set_frame_range", text="更新帧范围")

    row = layout.row()
    row.template_list("OBJECT_UL_Lip_Sync_Sub", "lip_sync_list", scene, "lip_sync_list", scene, "lip_sync_list_index")
       
    col = row.column()
    # col.operator("object.add_open", icon='ADD', text="")
    # col.operator("object.add_open", icon='REMOVE', text="")
    col.operator("lip_sync_list.move_item", icon='TRIA_UP', text="").direction = 'UP'
    col.operator("lip_sync_list.move_item", icon='TRIA_DOWN', text="").direction = 'DOWN'
    col.operator("object.clear_rows", icon='TRASH', text="")
    col.operator("object.set_local_storage", icon='FILE_TICK', text="").type = 'lip_sync'
    col.operator("object.load_local_storage", icon='IMPORT', text="").type = 'lip_sync'
    
    row = layout.row()
    row.operator("object.add_open", text="Add Open", icon = 'ADD')
    row.operator("object.add_close", text="Add Close", icon = 'ADD')
    row.operator("object.copy", text="Copy", icon = 'DUPLICATE')
    row.operator("lip_sync_list.delete_item", text="删除", icon = 'X')
    layout.operator("object.lip_sync", text="Lip Sync")
