from typing import Callable
from animationStrategies.animationStrategy import AnimationStrategy
from animationStrategies.curveFunctions import linear
from pygame_imports import *

class LerpTransition(AnimationStrategy):

  def __init__(self, initial: Vector2, to: Vector2, ms: int, curveFunc: Callable[[float],float] = linear):
    self.initial = initial
    self.to = to
    self.current = initial
    self.time_elapsed = 0
    self.duration = ms/1000
    self.curveFunc = curveFunc

  def checkFinished(self) -> bool:
    return self.initial.distance_to(self.to) == 0  
  def update(self, dt: float):
    self.time_elapsed += dt
    if self.time_elapsed < self.duration:
      t = self.curveFunc(self.time_elapsed/self.duration)
      self.current = self.initial.lerp(self.to, t)
    else:
      self.current = self.to

    return self.current