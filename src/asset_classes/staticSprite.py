from asset_classes.graphicalAsset import GraphicalAsset
from models.theme.sprites import SpriteSpecsData


class StaticSprite(GraphicalAsset):
  def copy(self):
    return StaticSprite(self.image, SpriteSpecsData(self.dimensions, self.offset))