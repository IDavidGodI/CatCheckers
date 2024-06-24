
from abc import ABC, abstractmethod


class AnimationStrategy(ABC):

  @abstractmethod
  def checkFinished(self) -> bool: ...

  @abstractmethod
  def update(self, dt: float):
    ...