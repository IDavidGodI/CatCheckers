
from dataclasses import dataclass

from models.baseDataClass import ParseableDataClass
from models.theme.board import BoardData
from models.theme.colorSettings import ColorSettings
from models.theme.pieces import PiecesData

@dataclass
class ThemeData (ParseableDataClass):
  pieces: PiecesData
  board: BoardData
  colorSettings: ColorSettings


__all__ = ["ThemeData"]