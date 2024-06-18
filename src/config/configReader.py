import json
from config.dataLoader import DataLoader
from config.paths import Paths
from models.theme import ThemeData


class ConfigReader:
  theme: ThemeData
  def __init__(self, paths: Paths):
    self.paths = paths
    self.dataLoader = DataLoader()
    
  def readThemeSetupFiles(self):
    mainSetupFilePath = self.paths.getMainSetupPath()
    themeSetupFilePath = self.paths.getThemeSetupPath()
    
    self.dataLoader.loadJson(mainSetupFilePath)
    return self.dataLoader.mergeDictionaries(
      self.dataLoader.loadJson(mainSetupFilePath),
      self.dataLoader.loadJson(themeSetupFilePath)
    )
     