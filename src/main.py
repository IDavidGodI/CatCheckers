from asset_classes.assets import Assets
from pygame_imports import *
from gameObjects.piece import Piece
from models.theme import *
import window

pg.init()
pg.display.set_icon(pg.image.load("./assets/icono.ico"))

FONT = pg.font.SysFont("arial", 15)

class Game:

  thumbnail: pg.Surface = None
  def __init__(self, themeName: str):
    self.assets = Assets(themeName)
    self.clock = pg.time.Clock()
    self.running = False
    window.addObserver(self)

  def resized(self):
    self.assets.board.setScale(window.getDisplaySize().y/self.assets.board.dimensions.y)

  def run(self):
    self.running = True
    self.assets.board.setPosition(pg.Vector2(100,0))
    self.resized()
    while self.running:
      
      dt = self.clock.tick(60)/1000
      
      events = pg.event.get()
      window.display.fill("#ffffff")
      for event in events:
        
        if (event.type == pg.QUIT): 
          self.running=False
          exit()
        if event.type == pg.MOUSEBUTTONDOWN:
          if event.button == 1:
            if self.assets.board.checkGlobalCollision(event.pos):
              self.assets.board.handleClick(event.pos)
        if event.type == pg.KEYDOWN:
          if event.key == pg.K_F1:
            print(f"FPS: {self.clock.get_fps()}")

          if event.key == pg.K_F11:
            window.toggleFullScreen()
          if event.key == pg.K_1:
            s: Piece
            for s in self.assets.board.layers.get("light_pieces").sprites():
              s.setAction("checkers")
              

      self.assets.board.update(dt)
      
          
      self.assets.board.render(window.display)
      window.display.blit(FONT.render(f"FPS: {self.clock.get_fps()}",True, "#00000000"), (0,0))
      
      # if (theme.thumbnail):
      #   window.blit(theme.thumbnail, (1160,0))
      
      pg.display.update()
  
    
        


      
    

    

    

  


game = Game("Classic")
# gameSurface = pg.Surface(())




# piecesize = theme.setup.data.get("pieces").get("dimensions")
# boardoffset = theme.setup.data.get("board").get("offset")

game.run()
