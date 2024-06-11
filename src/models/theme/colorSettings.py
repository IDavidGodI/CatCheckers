from dataclasses import dataclass
from models.baseDataClass import ParseableDataClass
from models.theme.colorScheme import ColorScheme
from models.genericDicts.colorSchemes import ColorSchemes


@dataclass
class ColorSettings(ParseableDataClass):
  defaultScheme: ColorScheme
  schemes: ColorSchemes[ColorScheme]