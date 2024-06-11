
from typing import Literal

from models.genericDicts.genericDict import *

PiecesActionKey = Literal["checkers", "idle", "checkidle", "death", "checkdeath"]


class PiecesActions(GenericDict[PiecesActionKey, DictValuesType]): pass

__all__ = ["PiecesActions", "PiecesActionKey"]

  