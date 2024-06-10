from dataclasses import dataclass

from models.BaseDataClass import ParseableDataClass

@dataclass
class SpriteSpecs(ParseableDataClass):
  dimensions: int
  offset: int

@dataclass
class Sprite(ParseableDataClass):
  spriteSpecs: SpriteSpecs

