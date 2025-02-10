from ..libs.blender_utils import  get_data, get_operator, get_object_, get_shape_keys, get_context

def set_constant (close_index_list, _shape_keys, shape_key_name, interpolation):
  # 获取形态键的动画数据
  fcurves = _shape_keys.animation_data.action.fcurves

  # 查找与指定形态键相关的关键帧曲线
  for fcurve in fcurves:
    if fcurve.data_path.endswith(f'key_blocks["{shape_key_name}"].value'):
      keyframe_points = fcurve.keyframe_points

      for keyframe_point in keyframe_points:
        keyframe_point.interpolation = interpolation

      for close_index in close_index_list:
        keyframe_points[close_index].interpolation = 'CONSTANT'

      break

# 获取每段话结束时的 close 在 lip sync list 中的索引，这些 close 插值需要设置成
# CONSTANT
def get_close_index_list (lip_sync_list, min_frame):
  index_list = []
  last_index = len(lip_sync_list) - 1

  for index, item in enumerate(lip_sync_list):
    frame = item.frame
    open = item.open

    if (
      not open and 
      index < last_index and 
      lip_sync_list[index + 1].frame - frame > min_frame
    ):
      index_list.append(index)

  return index_list

def before (self, lip_sync_list):
  def get_repeat_frame (list):
    seen = set()
    duplicates = set()

    for item in list:
      if item in seen:
        duplicates.add(item)
      else:
        seen.add(item)

    return duplicates

  list = [item.frame for item in lip_sync_list]
  duplicates = get_repeat_frame(list)
  passing = True
  
  if len(duplicates):
    passing = False
    self.report({'WARNING'}, f'存在重复的帧{ str(duplicates) }')

  # TODO: 严格模式，闭合时，值一定要为 0，打开时，值一定不为 0
  # TODO: 检查 shape key 是否存在

  return passing

def one (lip_sync_list, start_index, end_index):
  lip_sync_list[start_index].shape_key_value = 0.5

def two (lip_sync_list, start_index, end_index):
  res = lip_sync_list[start_index:end_index + 1]
  res[0].shape_key_value = 0.5
  res[1].shape_key_value = 0.25

def three (lip_sync_list, start_index, end_index):
  res = lip_sync_list[start_index:end_index + 1]
  res[0].shape_key_value = 0.33
  res[1].shape_key_value = 0.66
  res[2].shape_key_value = 0.33

def four (lip_sync_list, start_index, end_index):
  res = lip_sync_list[start_index:end_index + 1]
  res[0].shape_key_value = 0.33
  res[1].shape_key_value = 0.66
  res[2].shape_key_value = 1
  res[3].shape_key_value = 0.5

def five (lip_sync_list, start_index, end_index):
  res = lip_sync_list[start_index:end_index + 1]
  res[0].shape_key_value = 0.33
  res[1].shape_key_value = 0.66
  res[2].shape_key_value = 1
  res[3].shape_key_value = 0.66
  res[4].shape_key_value = 0.33

strategies = {
  1: one,
  2: two,
  3: three,
  4: four,
  5: five
}

def smart_shape_key_value (lip_sync_list):
  # TODO: 每段话提前 3 帧张嘴，延迟 3 帧闭嘴
  open_list = []
  last_index = len(lip_sync_list) - 1

  # 获取所有连续的 open，将每一段连续的 open 的开始索引和结束索引保持起来
  index = 0
  while index <= last_index:
    item = lip_sync_list[index]
    is_open = item.open

    # 跳过所有 close
    if not is_open:
      index += 1
      continue

    # 处理最开始就是 open 状态的情况
    if index == 0:
      end_index = 0

      # 找到最近的一个 close，如果找不到说明全部都是 open，那么 open_list 将是空列表
      for i, item in enumerate(lip_sync_list):
        if not item.open:
          end_index = i
          open_list.append([index, i - 1])

          break

      # 跳过最近的一个 close 之前的所有项和最近的 close 自身
      index += (end_index + 1)
      continue

    # 处理最后依然是 open 的情况（正常情况应该要为 close）
    if index == last_index:
      # 获取最后一段连续的 open
      last_open_item = open_list[len(open_list) - 1]

      if len(last_open_item) == 1:
        # 有开始索引，说明开始索引的位置到最后一项都是 open，就将最后一项作为
        # 结束索引，如果数量少，也能自动分配数值
        # ... close oepn open
        # ... close oepn open open
        last_open_item.append(index)
      else:
        #  正好以 open 结尾，并且 open 的前一项是 close，那么就是数量为 1 的片段
        # ... close oepn
        last_open_item.append([index, index])
      
      index += 1
      continue

    prev = lip_sync_list[index - 1]
    next = lip_sync_list[index + 1]
    prev_is_open = prev.open == True
    prev_is_close = prev.open == False
    next_is_open = next.open == True
    next_is_close = next.open == False

    if prev_is_close and next_is_close:
      # 前一项是闭合，后一项闭合，唯一的打开
      open_list.append([index, index])
      # 后一项一定是闭合，直接跳过这两项
      index += 2
    elif prev_is_close and next_is_open:
      # 前一项是闭合，后一项打开，打开的开始索引
      open_list.append([index])
      index += 1
    elif prev_is_open and next_is_open:
      # 前一项是打开，后一项打开，跳过，继续寻找结束
      index += 1
    elif prev_is_open and next_is_close:
      # 前一项是打开，后一项闭合，打开的结束索引
      open_list[len(open_list) - 1].append(index)
      index += 1

  for open_item in open_list:
    start_index, end_index = open_item
    open_numbers = end_index - start_index + 1

    if open_numbers in strategies:
      strategies[open_numbers](lip_sync_list, start_index, end_index)

# TODO: 移动到 utils 中
def shape_key_keyframe_insert (shape_key, frame, value):
  shape_key.value = value
  shape_key.keyframe_insert(data_path = "value", frame = frame)

def keyframe_insert (lip_sync_list, shape_key):
  for item in lip_sync_list:
    frame = item.frame
    value = item.shape_key_value
    shape_key_keyframe_insert(shape_key, frame, value)

class Lip_Sync (get_operator()):
  bl_idname = "object.lip_sync"
  bl_label = "Lip Sync"

  def execute(self, context):
    scene = context.scene
    lip_sync_list = scene.lip_sync_list
    shape_key_name = scene.shape_key_name
    lip_sync_shape_key = scene.lip_sync_shape_key
    smart_mode = scene.smart_mode
    min_frame = scene.min_frame
    interpolation = scene.interpolation
    shape_keys = get_shape_keys(lip_sync_shape_key)
    shape_key = shape_keys[shape_key_name]
    passing = before(self, lip_sync_list)

    if passing:
      if smart_mode:
        smart_shape_key_value(lip_sync_list)
      
      keyframe_insert(lip_sync_list, shape_key)

      _shape_keys = get_data().shape_keys.get('Key')
      close_index_list = get_close_index_list(lip_sync_list, min_frame)
      set_constant(close_index_list, _shape_keys, shape_key_name, interpolation)

    return {'FINISHED'}
