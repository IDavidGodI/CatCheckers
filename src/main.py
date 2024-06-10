from paths import Paths
import pygame as pg
import json
import os
from models.Theme import Pieces, Theme



json_data = {
    "pieces": {
        "spriteSpecs": {
            "dimensions": 64,
            "offset": 10
        },
        "actions": {
            "test": {
                "frames": 10,
                "fps": 24
            }
        }
    },
    "board": {
        "spriteSpecs": {
            "dimensions": 128,
            "offset": 5
        }
    },
    "colorSettings": {
        "defaultScheme": {
            "bgColor": "#3498db",
            "fontColor": "#ffffff"
        },
        "schemes":{
          "primary": {
              "bgColor": "#3498db",
              "fontColor": "#ffffff"
          },
          "secondary": {
              "bgColor": "#2ecc71",
              "fontColor": "#ffffff"
          }
        }
    }
}




print(Theme.from_dict(json_data))
exit()
WINDOW_SIZE = (1280,720)
window = pg.display.set_mode(WINDOW_SIZE)


pg.display.set_icon(pg.image.load("./src/assets/icono.ico"))

running = True

class SetUP:
  data: dict
  def __init__(self, paths: Paths):
    self.loadData(paths)
    
  def loadData(self, paths: Paths):
    mainSetupFilePath = paths.getMainSetupPath()
    themeSetupFilePath = paths.getThemeSetupPath()
    with open(mainSetupFilePath) as mainSetupFile:
      self.data = json.load(mainSetupFile)
      with open(themeSetupFilePath) as themeSetupFile:
        self.data |= json.load(themeSetupFile)


class AbstractSprite:
  sprite: pg.Surface
  def __init__(self, sprite: pg.Surface = None, dimensions = (0,0), index: int = 0):
    if (sprite):
      self.setSprite(sprite, dimensions, index)

  def setSprite(self, sprite: pg.Surface, dimensions: tuple, index: int):
    
    self.sprite = pg.Surface(dimensions, pg.SRCALPHA)
    
    # self.sprite.set_colorkey((0, 0, 0))
    s = (index*dimensions[0])
    self.sprite.blit(sprite,(0,0), (s,0)+dimensions)
    self.sprite = self.sprite.convert_alpha()
  
  def render(self, surface: pg.Surface, coordinate: tuple):
    surface.blit(self.sprite, coordinate)




class ThemeL:
  setup: SetUP
  lightSprites: list[AbstractSprite]
  darkSprites: list[AbstractSprite]
  board: pg.Surface
  colorPalette: dict
  thumbnail: pg.Surface = None
  def __init__(self, themeName: str):
    self.paths = Paths(themeName)
    self.setup = SetUP(self.paths)
    self.lightSprites = []
    self.darkSprites = []
    self.loadTheme()

  def loadTheme(self):
    piecesSetUP = self.setup.data["pieces"]
    boardSetUP = self.setup.data["board"]
    self.colorPalette = self.setup.data["colorPalette"]
    
    self.board = pg.image.load(self.paths.getBoardPath())
    thumbnailpath = self.paths.getThumbnailPath()
    if (thumbnailpath):
      self.thumbnail = pg.image.load(thumbnailpath)
    dimensions = (piecesSetUP.get("dimensions"),)*2
    for animacion in piecesSetUP["flow"]:
      name = animacion.get("name")
      darkSprites = pg.image.load(self.paths.getDarkSpritesPath(name))
      lightSprites = pg.image.load(self.paths.getLightSpritesPath(name))
      static = animacion.get("static")
      if (static):
        for index in static:
          self.lightSprites.append(AbstractSprite(lightSprites, dimensions, index-1))
          self.darkSprites.append(AbstractSprite(darkSprites, dimensions, index-1))
        


      
    

    

    

  


theme = ThemeL("Chocolate")
# gameSurface = pg.Surface(())

clock = pg.time.Clock()



piecesize = theme.setup.data.get("pieces").get("dimensions")
boardoffset = theme.setup.data.get("board").get("offset")

board = theme.board
while running:
  DISPLAY_SIZE = (pg.display.Info().current_w,pg.display.Info().current_h)
  clock.tick(12)
  events = pg.event.get()
  window.fill(theme.colorPalette["primary"])
  
  for event in events:
    if (event.type == pg.QUIT): 
      running=False
      exit()
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_F11:
        if pg.display.is_fullscreen():
          pg.display.set_mode(WINDOW_SIZE)
        else:
          pg.display.set_mode((0,0), pg.FULLSCREEN)

  
  for x in range(0,8):
    for y in range(0,3):
      for piece in theme.lightSprites:
        if (x%2 ^ y%2):
          piece.render(board,(x*piecesize + boardoffset, y*piecesize + boardoffset))

  for x in range(0,8):
    for y in range(5,8):
      for piece in theme.darkSprites:
        if (x%2 ^ y%2):
          piece.render(board,(x*piecesize + boardoffset, y*piecesize + boardoffset))
  
  scaled_board=pg.transform.scale(board, (DISPLAY_SIZE[1],)*2)
  
  window.blit(scaled_board,(0,0))
  if (theme.thumbnail):
    window.blit(theme.thumbnail, (1160,0))
  
  pg.display.update()