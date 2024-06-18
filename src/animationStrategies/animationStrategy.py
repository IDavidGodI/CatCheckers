from typing import Protocol


class AnimationStrategy(Protocol):

  def checkFinished(self) -> bool: ...

  def update(self, dt: float):
    ...