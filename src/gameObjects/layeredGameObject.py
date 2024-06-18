from typing import Generic, OrderedDict, TypeVar
from asset_classes.graphicalAsset import GraphicalAsset
from gameObjects.gameObject import GameObject
from pygame_imports import *

from gameObjects.gameObjectGroup import GameObjectGroup


T = TypeVar("T", bound=str)

class LayeredGameObject(Generic[T],GameObject):
  layers: OrderedDict[T, GameObjectGroup[GameObject]]

  def __init__(self, sprite: GraphicalAsset, pos: Vector2 = Vector2(0,0), *groups, **kwargs):
    super().__init__(sprite, pos, *groups, **kwargs)
    self.layers = {}
    print("children", self.layers)

  def layerSprites(self, layer: T):
    group = self.layers[layer]
    return group.sprites()
  
  def addLayer(self, layer: T):
    self.layers[layer] = GameObjectGroup[GameObject]()
  def clearLayer(self, layer: T):
    group = self.layers[layer]
    group.empty()

  def addChildren(self, layer: T, *children: GameObject):
    group = self.layers[layer]
    for obj in children:
      if (len(obj.groups())>0): obj.kill()

      obj.add(group)
      obj.parent = self


  def removeChildren(self,*children: GameObject):
    for obj in children:
      obj.kill()
  def update(self, dt: float):
    super().update(dt)
    for l in self.layers:
      self.layers[l].update(dt)

  def render(self, surface: pg.Surface):
    for l in self.layers:
      self.layers[l].render(self.sprite.surface)
    super().render(surface)