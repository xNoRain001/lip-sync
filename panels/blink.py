from ..libs.blender_utils import get_data, get_panel

from ..const import bl_category
from ..operators import OBJECT_OT_blink

class VIEW3D_PT_blink (get_panel()):
  bl_region_type = 'UI'
  bl_label = 'Blink'
  bl_space_type = 'VIEW_3D'
  bl_category = bl_category
  bl_idname = "VIEW3D_PT_blink_config"

  def draw(self, context):
    layout = self.layout
    scene = context.scene
    box = layout.box()

    row = box.row()
    row.label(text = '类型')
    row.prop(scene, 'blink_type', text = '')
    row = box.row()
    row.label(text = '眨眼频率')
    row.prop(scene, 'blink_frequency', text = '')
    row = box.row()
    row.label(text = '起始帧')
    row.prop(scene, 'blink_frame_start', text = '')
    row = box.row()
    row.label(text = '结束帧')
    row.prop(scene, 'blink_frame_end', text = '')
    data = get_data()
    row = box.row()
    row.label(text = '形态键')
    row.prop_search(scene, 'blink_shape_key', data, 'shape_keys', text = '')
   
    blink_shape_key = scene.blink_shape_key

    if blink_shape_key:
      row = box.row()
      row.label(text = '活动形态键')
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
