
import json


class DataLoader:
  def loadJson(self, path: str):
    with open(path) as file:
      return json.load(file)
  
  def mergeDictionaries(self, mainDict: dict, toMergeDict: dict):
    for k, v in toMergeDict.items():
      if (isinstance(v, dict) and k in mainDict and isinstance(mainDict[k], dict)):
        mainDict[k] |= self.mergeDictionaries(mainDict[k],v)
      else:
        mainDict[k] = v
    
    return mainDict