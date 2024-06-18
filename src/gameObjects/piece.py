from asset_classes.graphicalAsset import GraphicalAsset
from gameObjects.gameObject import GameObject
from models.genericDicts.piecesActions import PiecesActionKey, GenericPiecesActions
from pygame_imports import *
from pygame_imports import Vector2

class Piece(GameObject):
  actionSprites: GenericPiecesActions[GameObject]
  action: PiecesActionKey
  def __init__(self, actionSprites: GenericPiecesActions[GraphicalAsset], pos: Vector2 = ..., *groups, initAction: PiecesActionKey = "idle", scale: float = 1, parent: GameObject = None):
    super().__init__(actionSprites.get(initAction), pos, *groups, scale=scale, parent=parent)
    self.action = initAction
    self.actionSprites = actionSprites
    

  def setAction(self, action: PiecesActionKey):
    self.action = action
    self.sprite = self.actionSprites.get(action)

  def render(self, surface: pg.Surface):
    
    return super().render(surface)
