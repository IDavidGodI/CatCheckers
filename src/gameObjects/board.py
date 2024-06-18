from typing import Literal

from asset_classes.graphicalAsset import GraphicalAsset
from pygame_imports import *

from gameObjects.layeredGameObject import LayeredGameObject
from gameObjects.piece import Piece
from pygame_imports import Vector2


BoardLayersKeys = Literal["hightlighted","dark_pieces", "light_pieces", "moving_piece"]

class Board(LayeredGameObject[BoardLayersKeys]):

  def __init__(self, sprite: GraphicalAsset, pos: Vector2 = ..., *groups, **kwargs):
      super().__init__(sprite, pos, *groups, **kwargs)
      self.addLayer("hightlighted")
      self.addLayer("light_pieces")
      self.addLayer("dark_pieces")
      self.addLayer("moving_piece")

      self.initialLightPositions = None
      self.initialDarkPositions = None

  def getCellSize(self):
    return (self.dimensions-(2*self.offset))/8
  
  #TODO: CREATE MOVEMENT ANIMATION STRATEGIES FOR ANIMATING
  def getCellPosition(self,cell: Vector2 | tuple):
    if isinstance(cell, tuple): cell = Vector2(cell)
    cell_size = self.getCellSize()
    return Vector2(cell.x*cell_size.x, cell.y*cell_size.y)
    

  def update(self, dt: float):

    super().update(dt)
    pass


  def handleClick(self, clickPos: Vector2 | tuple):
    cell_size = self.getCellSize()*self.getGlobalScale()
    if isinstance(clickPos, tuple): clickPos = Vector2(clickPos)
    offsetClick = clickPos-(self.getGlobalPosition()+self.offset*self.getGlobalScale())
    print("cell:", offsetClick, int(offsetClick.x/cell_size.x), int(offsetClick.y/cell_size.y))

  def calcInitialPositions(self):
    if (not self.initialDarkPositions or not self.initialLightPositions):
      self.initialLightPositions: list[Vector2] = []
      self.initialDarkPositions: list[Vector2] = []

      for x in range(0,8):     
        for y in range(0,3):
            if (x%2 ^ y%2): self.initialLightPositions.append(Vector2(x,y))

      for x in range(0,8):      
        for y in range(5,8):
          if (x%2 ^ y%2): self.initialDarkPositions.append(Vector2(x,y))

  def orderPieces(self):
    self.calcInitialPositions()
    darkSprites: list[Piece] = self.layerSprites("dark_pieces")
    lightSprites: list[Piece] = self.layerSprites("light_pieces")

    for i in range(0,max(len(darkSprites),len(lightSprites))):
      dark_pos = self.initialDarkPositions[i]
      light_pos = self.initialLightPositions[i]
      darkSprites[i].setPosition(self.getCellPosition(dark_pos))
      lightSprites[i].setPosition(self.getCellPosition(light_pos))