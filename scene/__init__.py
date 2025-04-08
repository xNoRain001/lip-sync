from .add_blink import add_blink
from .add_lip_sync import add_lip_sync

def register():
  add_blink()
  add_lip_sync()

def unregister():
  pass
