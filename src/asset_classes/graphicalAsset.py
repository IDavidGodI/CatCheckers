from abc import ABC, abstractmethod
from models.theme.sprites import SpriteSpecsData
from pygame_imports import *

class GraphicalAsset(ABC):
  image: pg.Surface
  def __init__(self, image: pg.Surface, spriteSpecs: SpriteSpecsData):
    self.dimensions = Vector2(spriteSpecs.dimensions)
    self.offset = Vector2(spriteSpecs.offset or 0)
    self.surface = pg.Surface(self.dimensions, pg.SRCALPHA)
    self.image = image
    self.image_pos = Vector2(0)

  def update(self, dt: float):
    """A method that can change the state of the asset every frame"""
    self.surface.fill((0,0,0,0))
    self.surface.blit(self.image, self.image_pos)

  @abstractmethod
  def copy(self):
    """The method must be implemented allowing to generate a copy of the Graphical Asset"""