from dataclasses import dataclass

from models.BaseDataClass import ParseableDataClass

@dataclass
class ColorScheme(ParseableDataClass):
  bgColor: str
  fontColor: str


