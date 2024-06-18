
from dataclasses import dataclass

from models.genericDicts.piecesActions import *
from models.theme.sprites import SpriteData
from models.theme.action import FramesData



@dataclass
class PiecesData(SpriteData):
  actions: GenericPiecesActions[FramesData]
