
from dataclasses import dataclass

from models.BaseDataClass import ParseableDataClass
from models.theme.Board import Board
from models.theme.ColorSettings import ColorSettings
from models.theme.Pieces import Pieces

@dataclass
class Theme (ParseableDataClass):
  pieces: Pieces
  board: Board
  colorSettings: ColorSettings


__all__ = ["Theme"]