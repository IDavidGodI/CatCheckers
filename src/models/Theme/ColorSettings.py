from typing import Dict
from dataclasses import dataclass

from models.BaseDataClass import ParseableDataClass

@dataclass
class ColorSetting(ParseableDataClass):
  bgColor: str
  fontColor: str


@dataclass
class ColorSettings(ParseableDataClass):
  defaultScheme: ColorSetting
  schemes: Dict[str,ColorSetting]