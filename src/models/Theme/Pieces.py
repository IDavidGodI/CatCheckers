
from dataclasses import dataclass

from typing import Dict


from models.Theme.ActionsDict import Actions
from models.Theme.Sprites import Sprite



@dataclass
class Pieces (Sprite):
  actions: Actions
