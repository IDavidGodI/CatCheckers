
from dataclasses import dataclass

from typing import Dict


from models.theme.ActionsDict import Actions
from models.theme.Sprites import Sprite



@dataclass
class Pieces (Sprite):
  actions: Actions
