from ..libs.blender_utils import  get_data, get_operator, get_object_, get_shape_keys, get_context

def set_constant (index_list, a, shape_key_name, interpolation, my_list):
  # 获取形态键的动画数据
  fcurves = a.animation_data.action.fcurves

  # 查找与指定形态键相关的关键帧曲线
  for fcurve in fcurves:
    if fcurve.data_path.endswith(f'key_blocks["{shape_key_name}"].value'):
      keyframe_points = fcurve.keyframe_points

      for keyframe_point in keyframe_points:
        keyframe_point.interpolation = interpolation

      for i in index_list:
        keyframe_points[i].interpolation = 'CONSTANT'
        keyframe_points[i + 1].interpolation = interpolation

      break

def get_index_list (my_list):
  index_list = []
  last_index = len(my_list) - 1

  for index, item in enumerate(my_list):
    frame = item.int_value
    enum_value = item.enum_value

    if (
      enum_value == 'close' and 
      index < last_index and 
      my_list[index + 1].int_value - frame > 3
    ):
      index_list.append(index)

  return index_list

def before (self, my_list):
  def get_repeat_frame (list):
    seen = set()
    duplicates = set()

    for item in list:
      if item in seen:
        duplicates.add(item)
      else:
        seen.add(item)

    return duplicates

  list = [item.int_value for item in my_list]
  duplicates = get_repeat_frame(list)
  passing = True

  # TODO: 闭合时，值一定要为0x
  # 这里根据类型选择，可能出现类型为 close，float_value 不为 0 的情况
  # 根据 float_value 进行选择
  
  if len(duplicates):
    passing = False
    self.report({'WARNING'}, f'存在重复的帧{ str(duplicates) }')

  return passing

def one (my_list, start_index, end_index):
  print(start_index)
  my_list[start_index].float_value = 0.5

def two (my_list, start_index, end_index):
  res = my_list[start_index:end_index + 1]
  res[0].float_value = 0.5
  res[1].float_value = 0.25

def three (my_list, start_index, end_index):
  res = my_list[start_index:end_index + 1]
  res[0].float_value = 0.33
  res[1].float_value = 0.66
  res[2].float_value = 0.33

def four (my_list, start_index, end_index):
  res = my_list[start_index:end_index + 1]
  res[0].float_value = 0.33
  res[1].float_value = 0.66
  res[2].float_value = 1
  res[3].float_value = 0.5

def five (my_list, start_index, end_index):
  res = my_list[start_index:end_index + 1]
  res[0].float_value = 0.33
  res[1].float_value = 0.66
  res[2].float_value = 1
  res[3].float_value = 0.66
  res[4].float_value = 0.33

strategies = {
  1: one,
  2: two,
  3: three,
  4: four,
  5: five
}

def smart_v (my_list):
  # 每段话的开始和结束都需要标记，标记的开始的帧数提前 3 帧张嘴，设置成闭合
  # 标记结束的帧数延迟 3 帧闭嘴，设置成闭合
  open_list = []
  last_index = len(my_list) - 1

  index = 0
  while index <= last_index:
    item = my_list[index]
    is_open = item.enum_value == 'open'

    if not is_open:
      index += 1
      continue

    if index == 0:
      end_index = 0

      for i, item in enumerate(my_list):
        if item.enum_value == 'close':
          end_index = i
          open_list.append([index, i - 1])
          break

      index += (end_index + 1)
      continue

    if index == last_index:
      last_open_item = open_list[len(open_list) - 1]

      if len(last_open_item) == 1:
        last_open_item.append(index)
      else:
        last_open_item.append([index, index])
      
      index += 1
      continue

    prev = my_list[index - 1]
    next = my_list[index + 1]
    prev_is_open = prev.enum_value == 'open'
    prev_is_close = prev.enum_value == 'close'
    next_is_open = next.enum_value == 'open'
    next_is_close = next.enum_value == 'close'

    if prev_is_close and next_is_close:
      # 前一项是闭合，后一项闭合，唯一的打开
      open_list.append([index, index])
      # 下一项一定是闭合，直接跳过
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
    number = end_index - start_index + 1

    if number in strategies:
      strategies[number](my_list, start_index, end_index)

def shape_key_keyframe_insert (shape_key, frame, value):
  shape_key.value = value
  shape_key.keyframe_insert(data_path = "value", frame = frame)

def keyframe_insert (my_list, shape_key):
  for item in my_list:
    frame = item.int_value
    value = item.float_value
    shape_key_keyframe_insert(shape_key, frame, value)

class Lip_Sync (get_operator()):
  bl_idname = "my_ui.lip_sync"
  bl_label = "Lip Sync"

  def execute(self, context):
    scene = context.scene
    my_list = scene.my_list
    shape_key_name = scene.shape_key_name
    shape_keys = get_shape_keys('Key')
    shape_key = shape_keys[shape_key_name]
    smart_mode = scene.smart_mode
    interpolation = scene.interpolation
    passing = before(self, my_list)

    if passing:
      if smart_mode:
        smart_v(my_list)
      
      keyframe_insert(my_list, shape_key)

      a = get_data().shape_keys.get('Key')
      index_list = get_index_list(my_list)
      set_constant(index_list, a, shape_key_name, interpolation, my_list)

    return {'FINISHED'}
