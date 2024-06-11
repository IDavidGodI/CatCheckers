from typing import Literal

from models.genericDicts.genericDict import *


ColorSchemeKeys = Literal[None]

class ColorSchemes(GenericDict[ColorSchemeKeys, DictValuesType]): pass


__all__ = ["ColorSchemes", "ColorSchemeKeys"]