from dataclasses import dataclass


from models.baseDataClass import ParseableDataClass

  

@dataclass
class FramesData(ParseableDataClass):
  frames: int
  fps: int | None