from dataclasses import dataclass

from models.BaseDataClass import ParseableDataClass

@dataclass
class Action(ParseableDataClass):
  frames: int
  fps: int | None

@dataclass
class Actions(ParseableDataClass):
  test: Action