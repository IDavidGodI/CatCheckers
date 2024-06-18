from asset_classes.graphicalAsset import GraphicalAsset
from models.theme.action import FramesData
from models.theme.sprites import SpriteSpecsData
from pygame_imports import *

class AnimatedSprite(GraphicalAsset):
  def __init__(self, framesData: FramesData, image: pg.Surface,spriteSpecs: SpriteSpecsData, loop = False):
    super().__init__(image, spriteSpecs)
    self.fps = framesData.fps
    self.frames = framesData.frames
    self.current_frame = 0
    self.done = False
    self.loop = loop
    self.frameTime = 1/self.fps
    self.ticks = 0
    
  
  def copy(self):
    return AnimatedSprite(FramesData(self.frames, self.fps), self.image, SpriteSpecsData(self.dimensions.x, self.offset))

  def reset(self):
    self.ticks = 0
    self.current_frame = 0
    self.done = False

  def setLoop(self, l: bool):
    self.loop = l
  def updateImagePos(self):
    if (not self.done): 
      imageDimensions = Vector2(self.image.get_size())
      self.image_pos = -Vector2(
        self.current_frame*self.dimensions.x%imageDimensions.x,
        0# self.current_frame*self.dimensions.y // imageDimensions.y
      )
      
  def update(self, dt: float):
    if (self.current_frame<self.frames-1) or self.loop:
      if self.current_frame==0: self.done = False
      self.ticks += dt
      if (self.ticks>=self.frameTime):
        self.ticks = 0
        self.current_frame += 1
        self.updateImagePos()
        
        
    if self.current_frame==self.frames-1 and (not self.done or self.loop): 
      self.done = True
      if self.loop:
        self.reset()

    super().update(dt)