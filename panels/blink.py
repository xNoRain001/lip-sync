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

class Blink_Sub_Var (get_property_group()):
  # 用于占位，其他属性有控件，不好进行选择
  name: get_props().StringProperty(name="name")
  appearance: get_props().IntProperty(name="appearance")
  disappearance: get_props().IntProperty(name="disappearance")
  eye_opening_time_2: get_props().IntProperty(name="eye_opening_time_2", default = 36)
  eye_closing_time_2: get_props().IntProperty(name="eye_closing_time_2", default = 3)
  eye_in_betweener_frame_time_2: get_props().IntProperty(name="eye_in_betweener_frame_time_2", default = 3)
  blink_interpolation_2: get_props().EnumProperty(
    name="blink_interpolation_2",
    items = [
      ('bezier', "BEZIER", ""),
      ('constant', "CONSTANT", ""),
      ('linear', "LINEAR", "")
    ],
    default='bezier'
  )

class Blink_Sub (get_ui_list()):
  bl_label = "Blink Sub"
  bl_idname = "OBJECT_UL_Blink_Sub"

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
    row.prop(item, "appearance", text="", emboss=False)
    row.prop(item, "disappearance", text="", emboss=False)
    row.prop(item, "eye_opening_time_2", text="", emboss=False)
    row.prop(item, "eye_closing_time_2", text="", emboss=False)
    row.prop(item, "eye_in_betweener_frame_time_2", text="", emboss=False)
    row.prop(item, "name", text="", emboss=False)

class Blink_Config (get_panel()):
  bl_label = "Blink Config"
  bl_idname = "OBJECT_PT_Blink_Config"
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = 'Item'

  def draw(self, context):
    layout = self.layout
    scene = context.scene

    # TODO: 下拉框选择形态键
    add_row_with_label(layout, '插值', scene, 'blink_interpolation', .2)
    add_row_with_label(layout, '睁眼时间', scene, 'eye_opening_time', .2)
    add_row_with_label(layout, '闭眼时间', scene, 'eye_closing_time', .2)
    add_row_with_label(layout, '中割时间', scene, 'eye_in_betweener_frame_time', .2)
    add_row_with_label(layout, '眼睛形态键', scene, 'blink_shape_key_name', .2)

class Blink (get_panel()):
  bl_label = "Blink"
  bl_idname = "OBJECT_PT_Blink"
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = 'Item'

  def draw(self, context):
    layout = self.layout
    scene = context.scene

    row = layout.row()
    # row.operator("my_ui.set_local_storage", text="Local Storagge")
    # row.operator("my_ui.load_local_storage", text="Load Local Storagge")

    row = layout.row()
    row.label(text="出现")
    row.label(text="消失")
    row.label(text="眨眼时间")
    row.label(text="闭眼时间时间")
    row.label(text="中割时间")

    row = layout.row()
    row.template_list("OBJECT_UL_Blink_Sub", "blink_list", scene, "blink_list", scene, "blink_list_index")
       
    col = row.column()
    col.operator("object.add_blink_sub", icon='ADD', text="")
    col.operator("object.delete_blink_sub", icon='REMOVE', text="")
    col.separator()
    col.operator("object.move_blink_sub", icon='TRIA_UP', text="").direction = 'UP'
    col.operator("object.move_blink_sub", icon='TRIA_DOWN', text="").direction = 'DOWN'
  
    row = layout.row()
    row.operator("object.add_blink_sub", text="Add Blink Sub")
    row.operator("object.copy_blink_sub", text="Copy Blink Sub")

    # layout.operator("my_ui.add_row", text="Add Row")
    # Add 10 rows button
    layout.operator("object.blink", text="Blink")
    # Clear empty rows button
    # layout.operator("my_ui.clear_empty_rows", text="Clear Empty Rows")
    layout.operator("object.clear_blink_subs", text="Clear Blink Subs")
