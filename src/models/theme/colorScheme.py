from dataclasses import dataclass

from models.baseDataClass import ParseableDataClass

@dataclass
class ColorScheme(ParseableDataClass):
  bgColor: str
  fgColor: str


