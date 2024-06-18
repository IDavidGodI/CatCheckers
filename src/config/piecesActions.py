from asset_classes.graphicalAsset import GraphicalAsset
from asset_classes.staticSprite import StaticSprite
from config.abstractLoader import AbstractLoader
from config.assetLoader import AssetLoader
from config.paths import Paths
from asset_classes.animatedSprite import AnimatedSprite
from models.genericDicts.piecesActions import GenericPiecesActions
from models.theme.pieces import PiecesData

class PiecesActions(GenericPiecesActions[GraphicalAsset]):
  def copy(self) -> GenericPiecesActions[GraphicalAsset]:
    copy = super().copy()
    for k,v in copy.items():
      copy[k] = v.copy()
    return copy
  
class PiecesActionsLoader(AbstractLoader):  

  def __init__(self, paths: Paths, piecesConfig: PiecesData):
    self.assetLoader = AssetLoader()
    self._lightActions = PiecesActions()
    self._darkActions = PiecesActions()
    self.piecesConfig = piecesConfig
    super().__init__(paths)
    
  @property
  def lightActions(self):
    return self._lightActions.copy()

  @property
  def darkActions(self):
    return self._darkActions.copy()

  def load(self):
    spriteSpecs = self.piecesConfig.spriteSpecs
    for action, data in  self.piecesConfig.actions.items():
      lightImage = self.assetLoader.loadImage(self.paths.getLightSpritesPath(action))
      darkImage = self.assetLoader.loadImage(self.paths.getDarkSpritesPath(action))
      if (not data.fps):
        self._lightActions[action] = StaticSprite(lightImage, spriteSpecs)
        self._darkActions[action] = StaticSprite(darkImage, spriteSpecs)
      else:
        self._lightActions[action] = AnimatedSprite(data, lightImage, spriteSpecs)
        self._darkActions[action] = AnimatedSprite(data, darkImage, spriteSpecs)