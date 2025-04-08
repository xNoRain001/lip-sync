from ..libs.blender_utils import get_data, get_panel

from ..const import bl_category
from ..operators import OBJECT_OT_blink

class VIEW3D_PT_blink (get_panel()):
  bl_region_type = 'UI'
  bl_label = 'Blink Config'
  bl_space_type = 'VIEW_3D'
  bl_category = bl_category
  bl_idname = "VIEW3D_PT_blink_config"

  def draw(self, context):
    layout = self.layout
    scene = context.scene
    box = layout.box()

    row = box.row()
    row.label(text = '插值')
    row.prop(scene, 'blink_interpolation', text = '')
    row = box.row()
    row.label(text = '眨眼间隔')
    row.prop(scene, 'eye_step', text = '')
    row = box.row()
    row.label(text = '闭眼时间')
    row.prop(scene, 'eye_closing_time', text = '')
    row = box.row()
    row.label(text = '中割时间')
    row.prop(scene, 'eye_in_betweener_frame_time', text = '')
    row = box.row()
    row.label(text = '睁眼时间')
    row.prop(scene, 'eye_opening_time', text = '')
    row = box.row()
    row.label(text = '出现')
    row.prop(scene, 'appearance', text = '')
    row = box.row()
    row.label(text = '消失')
    row.prop(scene, 'disappearance', text = '')
    data = get_data()
    row = box.row()
    row.label(text = '形态键')
    row.prop_search(scene, 'blink_shape_key', data, 'shape_keys', text = '')
   
    blink_shape_key = scene.blink_shape_key

    if blink_shape_key:
      row = box.row()
      row.label(text = '眨眼形态键')
      row.prop_search(
        scene, 
        'blink_key_block', 
        data.shape_keys[blink_shape_key], 
        'key_blocks', 
        text = ''
      )

    if scene.blink_key_block:
      row = box.row()
      row.operator(OBJECT_OT_blink.bl_idname, text = 'Blink')
