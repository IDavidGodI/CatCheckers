from pygame_imports import *

class AssetLoader:
  def loadImage(self, path: str):
    return pg.image.load(path)