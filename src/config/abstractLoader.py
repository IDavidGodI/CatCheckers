
from abc import ABC

from config.paths import Paths


class AbstractLoader(ABC):
  paths: Paths
  def __init__(self, paths: Paths, autoload = True):
    self.paths = paths
    if (autoload):
      self.load()
  
  def load(self) -> None:
    """Implement the load method with all the instructions a concrete loader will need"""