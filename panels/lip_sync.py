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

def get_float_value (enum_value):
  # mid
  float_value = 0.5

  if enum_value == 'open':
    float_value = 1
  elif enum_value == 'close':
    float_value = 0

  return float_value

# 两次选中同一项也会触发
def on_update(self, context):
  self.float_value = get_float_value(self.enum_value)
  
# 定义一个自定义属性组
class Lip_Sync_Sub_Vars (get_property_group()):
  # 用于占位，其他属性有控件，不好进行选择
  name: get_props().StringProperty(name="Name")
  int_value: get_props().IntProperty(name="Int Value")
  enum_value: get_props().EnumProperty(
    name="Enum Value",
    items=[
      ('open', "Open", ""),
      ('mid', "Mid", ""),
      ('close', "Close", "")
    ],
    default='open',
    update=on_update
  )
  float_value: get_props().FloatProperty(name="Float Value", min=0.0, max=1.0)

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
    row.prop(item, "int_value", text="", emboss=False)
    # Enum dropdown
    row.prop(item, "enum_value", text="", emboss=False)
    row.prop(item, "float_value", text="", emboss=False)
    row.prop(item, "name", text="", emboss=False)

class Lip_Sync_Config (get_panel()):
  bl_label = "Lip Sync Config"
  bl_idname = "OBJECT_PT_Lip_Config"
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = 'Item'

  def draw(self, context):
    layout = self.layout
    scene = context.scene

    add_row_with_label(layout, '起始', scene, 'lip_sync_frame_start', .2)
    add_row_with_label(layout, '间隔', scene, 'step', .2)
    # TODO: 下拉框选择形态键
    add_row_with_label(layout, '音素', scene, 'shape_key_name', .2)
    add_row_with_label(layout, '插值', scene, 'interpolation', .2)
    add_row_with_label(layout, '闭口间隔', scene, 'min_frame', .2)

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
    row.label(text="帧")
    row.label(text="状态")
    row.label(text="形态键值")
    row.label(text="文本")

    row = layout.row()
    row.template_list("OBJECT_UL_Lip_Sync_Sub", "my_list", scene, "my_list", scene, "my_list_index")
       
    col = row.column()
    col.operator("my_list.new_item", icon='ADD', text="")
    col.operator("my_list.delete_item", icon='REMOVE', text="")
    col.separator()
    col.operator("my_list.move_item", icon='TRIA_UP', text="").direction = 'UP'
    col.operator("my_list.move_item", icon='TRIA_DOWN', text="").direction = 'DOWN'

    row = layout.row()
    row.operator("my_ui.add_open", text="Add Open")
    row.operator("my_ui.add_mid", text="Add Mid")
    row.operator("my_ui.add_close", text="Add Close")
    row.operator("my_ui.copy", text="Copy")

    # layout.operator("my_ui.add_row", text="Add Row")
    # Add 10 rows button
    layout.operator("my_ui.lip_sync", text="Lip Sync")
    # Clear empty rows button
    # layout.operator("my_ui.clear_empty_rows", text="Clear Empty Rows")
    layout.operator("my_ui.clear_rows", text="Clear Rows")
    layout.operator("my_ui.set_local_storage", text="Local Storagge")
    layout.operator("my_ui.load_local_storage", text="Load Local Storagge")
