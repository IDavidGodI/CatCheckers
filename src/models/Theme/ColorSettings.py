from dataclasses import dataclass
from models.BaseDataClass import ParseableDataClass
from models.theme import ColorScheme
from models.theme.ColorSchemesDict import ColorSchemes


@dataclass
class ColorSettings(ParseableDataClass):
  defaultScheme: ColorScheme
  schemes: ColorSchemes