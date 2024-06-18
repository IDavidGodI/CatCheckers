from abc import ABC
from animationStrategies.animationStrategy import AnimationStrategy
from asset_classes.graphicalAsset import GraphicalAsset
from pygame_imports import *

class GameObject(Sprite, ABC):
  parent: 'GameObject'
  children: Group
  movement: AnimationStrategy
  def __init__(self, sprite: GraphicalAsset, pos: Vector2, *groups, scale: float = 1, parent: 'GameObject' = None):
    super().__init__(*groups)
    self.children = Group()
    self.parent = parent
    self.scale = scale
    self.pos = pos
    self.sprite = sprite
    self.movement = None
  @property
  def parent(self):
    return self._parent
  
  @parent.setter
  def parent(self, parent: 'GameObject'):
    self._parent = parent
    if parent:
      self.add(self.parent.children)

  @property
  def dimensions(self):
    return self.sprite.dimensions
  @property
  def offset(self):
    return self.sprite.offset

  def setMovement(self, movement: AnimationStrategy):
    self.movement = movement

  def getGlobalScale(self):
    if not self.parent:
      return self.scale
    
    return self.scale * self.parent.getGlobalScale()
  
  def getExternalOffset(self):
    return 0 if not self.parent else self.parent.offset

  def getGlobalPosition(self):
    if not self.parent: 
      return self.pos
    
    return ((self.pos + self.parent.offset)*self.parent.getGlobalScale()) + self.parent.getGlobalPosition()



  def setScale(self, scale: float):
    self.scale = scale
    
  
  def setPosition(self, pos:Vector2):
    self.pos = pos
  
  def _checkCollision(point: Vector2, pos: Vector2, dimensions: Vector2):
    return (pos.x <= point.x < pos.x + dimensions.x and
            pos.y <= point.y < pos.y + dimensions.y)

  def checkCollision(self, point: Vector2):
    if isinstance(point, tuple): point = Vector2(point)
    return GameObject._checkCollision(point, self.pos, self.dimensions*self.scale)
    

  def checkGlobalCollision(self, point: Vector2):
    if isinstance(point, tuple): point = Vector2(point)
    return GameObject._checkCollision(point, self.getGlobalPosition(), self.dimensions*self.getGlobalScale())
  
  def copy(self):
    return GameObject(self.pos, self.sprite.copy(), *self.groups(), scale=self.scale, parent = self.parent)

  def reset(self):
    ...

  def update(self, dt:float):
    """Should implement logic to execute before every render"""
    self.sprite.update(dt)

    if self.movement:
      self.setPosition(self.movement.update(dt))
      if self.movement.checkFinished(): self.movement = None
      
  # def draw(self, surface: pg.Surface, pos: Vector2):
  #   self.surface.blit(surface, self.offset + pos)

  def render(self, surface: pg.Surface):
    offset = self.parent.offset if self.parent else Vector2(0,0)
    surface.blit(
      pg.transform.scale_by(self.sprite.surface, self.scale), 
      offset + self.pos
    )