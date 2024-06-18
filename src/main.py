from assets import Assets
from pygame_imports import *
from gameObjects.piece import Piece
from models.theme import *
pg.init()
WINDOW_SIZE = Vector2(1280,720)
MONITOR_SIZE = Vector2(pg.display.Info().current_w, pg.display.Info().current_h)
window = pg.display.set_mode(WINDOW_SIZE)


pg.display.set_icon(pg.image.load("./assets/icono.ico"))

class Game:

  thumbnail: pg.Surface = None
  def __init__(self, themeName: str):
    self.assets = Assets(themeName)
    self.clock = pg.time.Clock()
    self.running = False

  def run(self):
    self.running = True
    self.assets.board.setScale(WINDOW_SIZE.y/self.assets.board.dimensions.y)
    self.assets.board.setPosition(pg.Vector2(100,0))
    while self.running:
      
      dt = self.clock.tick(60)/1000
      
      events = pg.event.get()
      window.fill("#ffffff")
      for event in events:
        
        if (event.type == pg.QUIT): 
          self.running=False
          exit()
        if event.type == pg.MOUSEBUTTONDOWN:
          if event.button == 1:
            if self.assets.board.checkGlobalCollision(event.pos):
              self.assets.board.handleClick(event.pos)
        if event.type == pg.KEYDOWN:
          if event.key == pg.K_F11:
            if pg.display.is_fullscreen():
              pg.display.set_mode(WINDOW_SIZE)
            else:
              pg.display.set_mode((0,0), pg.FULLSCREEN)
          if event.key == pg.K_1:
            s: Piece
            for s in self.assets.board.layers.get("light_pieces").sprites():
              s.setAction("checkers")
              

      self.assets.board.update(dt)
      
      # for x in range(0,8):
      #   for y in range(0,3):
      #     for piece in theme.lightSprites:
      #       if (x%2 ^ y%2):
      #         piece.render(board,(x*piecesize + boardoffset, y*piecesize + boardoffset))

      # for x in range(0,8):
      #   for y in range(5,8):
      #     for piece in theme.darkSprites:
      #       if (x%2 ^ y%2):
      #         piece.render(board,(x*piecesize + boardoffset, y*piecesize + boardoffset))
      
          
      self.assets.board.render(window)
      # if (theme.thumbnail):
      #   window.blit(theme.thumbnail, (1160,0))
      
      pg.display.update()
  
    
        


      
    

    

    

  


game = Game("Chocolate")
# gameSurface = pg.Surface(())




# piecesize = theme.setup.data.get("pieces").get("dimensions")
# boardoffset = theme.setup.data.get("board").get("offset")

game.run()
