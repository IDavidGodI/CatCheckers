
from typing import Literal

from models.genericDicts.genericDict import *

PiecesActionKey = Literal["checkers", "idle", "checkidle", "death", "checkdeath"]


class GenericPiecesActions(GenericDict[PiecesActionKey, DictValuesType]): pass

__all__ = ["GenericPiecesActions", "PiecesActionKey"]

  