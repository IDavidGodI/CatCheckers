from dataclasses import dataclass

from models.Theme.Action import Actions
from models.Theme.Sprites import Sprite

@dataclass
class Pieces (Sprite):
  actions: Actions