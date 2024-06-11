from dataclasses import dataclass

from models.baseDataClass import ParseableDataClass

@dataclass
class SpriteSpecsData(ParseableDataClass):
  dimensions: int
  offset: int

@dataclass
class SpriteData(ParseableDataClass):
  spriteSpecs: SpriteSpecsData

