from dataclasses import dataclass
from typing import TypedDict


from models.BaseDataClass import ParseableDataClass

  

@dataclass
class Action(ParseableDataClass):
  frames: int
  fps: int | None
