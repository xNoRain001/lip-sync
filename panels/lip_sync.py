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
  get_ui_list
)

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
    row = layout.row()
    row.prop(item, "frame", text="", emboss=False)
    # Enum dropdown
    # 这有这样才会在里面显示复选框
    # emboss=False 复选框就看不见了
    row.prop(item, "open", text="")
    row.label(text=str(item.open))
    row.prop(item, "shape_key_value", text="", emboss=False)
    row.prop(item, "text", text="", emboss=False)

class Lip_Sync_Config (get_panel()):
  bl_label = "Lip Sync Config"
  bl_idname = "OBJECT_PT_Lip_Config"
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = 'Item'

  def draw(self, context):
    layout = self.layout
    scene = context.scene

    # add_row_with_label(layout, '起始', scene, 'lip_sync_frame_start', .2)
    add_row_with_label(layout, '间隔', scene, 'step', .2)
    add_row_with_label(layout, '形态键', scene, 'lip_sync_shape_key', .2)
    # TODO: 下拉框选择形态键
    add_row_with_label(layout, '音素', scene, 'shape_key_name', .2)
    add_row_with_label(layout, '打开时的默认值', scene, 'lip_sync_shape_key_value', .2)
    add_row_with_label(layout, '插值', scene, 'interpolation', .2)
    add_row_with_label(layout, '闭口间隔', scene, 'min_frame', .2)
    add_row_with_label(layout, '智能模式', scene, 'smart_mode', .2)
    add_row_with_label(layout, '打开一次', scene, 'type_1_shape_key_value', .2)
    row = layout.row()
    row.label(text = '打开两次')
    row.prop(scene, "type_2_shape_key_value", text = '')
    row.prop(scene, "type_2_shape_key_value_2", text = '')
    row = layout.row()
    row.label(text = '打开三次')
    row.prop(scene, "type_3_shape_key_value", text = '')
    row.prop(scene, "type_3_shape_key_value_2", text = '')
    row.prop(scene, "type_3_shape_key_value_3", text = '')
    row = layout.row()
    row.label(text = '打开四次')
    row.prop(scene, "type_4_shape_key_value", text = '')
    row.prop(scene, "type_4_shape_key_value_2", text = '')
    row.prop(scene, "type_4_shape_key_value_3", text = '')
    row.prop(scene, "type_4_shape_key_value_4", text = '')
    row = layout.row()
    row.label(text = '打开五次')
    row.prop(scene, "type_5_shape_key_value", text = '')
    row.prop(scene, "type_5_shape_key_value_2", text = '')
    row.prop(scene, "type_5_shape_key_value_3", text = '')
    row.prop(scene, "type_5_shape_key_value_4", text = '')
    row.prop(scene, "type_5_shape_key_value_5", text = '')
  
class Lip_Sync (get_panel()):
  bl_label = "Lip Sync"
  bl_idname = "OBJECT_PT_Lip_Sync"
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = 'Item'

  def draw(self, context):
    layout = self.layout
    scene = context.scene

    row = layout.row()
    row.operator("object.set_local_storage", text="Local Storagge")
    row.operator("object.load_local_storage", text="Load Local Storagge")

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
    # col.operator("lip_sync_list.new_item", icon='ADD', text="")
    # col.operator("lip_sync_list.delete_item", icon='REMOVE', text="")
    col.operator("lip_sync_list.move_item", icon='TRIA_UP', text="").direction = 'UP'
    col.operator("lip_sync_list.move_item", icon='TRIA_DOWN', text="").direction = 'DOWN'
    
    row = layout.row()
    row.operator("object.add_open", text="Add Open", icon = 'ADD')
    row.operator("object.add_close", text="Add Close", icon = 'ADD')
    row.operator("object.copy", text="Copy", icon = 'DUPLICATE')
    row.operator("lip_sync_list.delete_item", text="删除", icon = 'X')
    layout.operator("object.lip_sync", text="Lip Sync")
    # layout.operator("object.clear_empty_rows", text="Clear Empty Rows")
    layout.operator("object.clear_rows", text="Clear")
