
from dataclasses import dataclass

from models.BaseDataClass import ParseableDataClass
from models.Theme.Board import Board
from models.Theme.ColorSettings import ColorSettings
from models.Theme.Pieces import Pieces

@dataclass
class Theme (ParseableDataClass):
  pieces: Pieces
  board: Board
  colorSettings: ColorSettings


__all__ = ["Theme"]