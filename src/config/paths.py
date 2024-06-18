from os import path


ASSETS_PATH = "assets"
THEMES_PATH = path.join(ASSETS_PATH,"themes")



DARK_PIECES_FILE = "dark_%s.png"
LIGHT_PIECES_FILE = "light_%s.png"
THUMBNAIL_FILE = "thumbnail.png"
BOARD_FILE = "board.png"
SETUP_FILE = "setup.json"


class Paths:
  themePath: str

  def __init__(self, themeName = None):
    if (themeName):
      self.themePath = self.getThemePath(themeName)

  def joinThemeAsset(self, assetName: str):
    directory = path.join(self.themePath, assetName)
    if path.isfile(directory):
      return directory
  def getDarkSpritesPath(self, animacion: str) -> str:
    return self.joinThemeAsset(DARK_PIECES_FILE%animacion)
  def getLightSpritesPath(self,animacion: str) -> str:
    return self.joinThemeAsset(LIGHT_PIECES_FILE%animacion)
  def getBoardPath(self) -> str:
    return self.joinThemeAsset(BOARD_FILE)
  def getThumbnailPath(self) -> str:
    return self.joinThemeAsset(THUMBNAIL_FILE)
  def getThemeSetupPath(self) -> str:
    return self.joinThemeAsset(SETUP_FILE)

  def getMainSetupPath(self) -> str:
    directory = path.join(THEMES_PATH, SETUP_FILE)
    if path.isfile(directory):
      return directory

  def getThemePath(self,themeName: str) -> str | None :
    directory = path.join(THEMES_PATH, themeName)
    if path.isdir(directory):
      return directory
  
