from asset_classes.staticSprite import StaticSprite
from config.piecesActions import PiecesActionsLoader
from config.configReader import ConfigReader
from config.paths import Paths
from gameObjects.gameObject import GameObject
from gameObjects.board import Board
from gameObjects.piece import Piece
from models.genericDicts.piecesActions import GenericPiecesActions
from models.theme import ThemeData
from models.theme.board import BoardData
from models.theme.colorSettings import ColorSettings
from pygame_imports import *

class Assets:
  
  
  board: Board
  colorSettings: ColorSettings

  def __init__(self, themeName: str):
    self.paths = Paths(themeName)
    self.config = ConfigReader(self.paths)
    
    self.loadAssets()

  def loadBoard(self, boardData: BoardData):
    return Board(StaticSprite(self.loadImage(self.paths.getBoardPath()), boardData.spriteSpecs))
    

  def loadImage(self, path: str):
    return pg.image.load(path)
  def copyActions(self, actionSprites: GenericPiecesActions[GameObject]):
    copy = actionSprites.copy()
    for k,v in copy.items():
      copy[k] = v.copy()
    return copy

  def loadAssets(self):
    theme = ThemeData.from_dict(self.config.readThemeSetupFiles())
    print(theme)
    boardSetUP = theme.board
    
    self.board = self.loadBoard(boardSetUP)

    
    actionsLoader = PiecesActionsLoader(self.paths, theme.pieces)
    

    for _ in range(0,12):
      self.board.addChildren("light_pieces", Piece(actionsLoader.lightActions))
      self.board.addChildren("dark_pieces", Piece(actionsLoader.darkActions))
        
    self.board.orderPieces()
