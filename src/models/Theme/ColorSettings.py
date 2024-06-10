from dataclasses import dataclass
from models.BaseDataClass import ParseableDataClass
from models.Theme import ColorScheme
from models.Theme.ColorSchemesDict import ColorSchemes


@dataclass
class ColorSettings(ParseableDataClass):
  defaultScheme: ColorScheme
  schemes: ColorSchemes