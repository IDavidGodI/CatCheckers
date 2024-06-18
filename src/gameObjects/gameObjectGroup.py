from typing import Callable, Generic, TypeVar
from gameObjects.gameObject import GameObject
from pygame_imports import *


GameObjectGroupType = TypeVar("GameObjectGroupType", bound=GameObject)

class GameObjectGroup(Generic[GameObjectGroupType], Group):
  sprites: Callable[[],list[GameObjectGroupType]] 
  def update(self, dt: float):
    
    for sprite in self.sprites():
      sprite.update(dt)

  def render(self, surface: pg.Surface):
    for sprite in self.sprites():
      sprite.render(surface)