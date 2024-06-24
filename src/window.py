from pygame_imports import *

pg.display.init()

display_info = pg.display.Info()

MONITOR_SIZE = Vector2(display_info.current_w, display_info.current_h)
WINDOW_SIZE = Vector2(1280,720)

display = pg.display.set_mode(WINDOW_SIZE)

subs = []

def addObserver(resizable):
  subs.append(resizable)

def removeObserver(resizable):
  subs.remove(resizable)

def notify():
  for sub in subs:
    sub.resized()

def getDisplaySize():
  display_info = pg.display.Info()
  return Vector2(display_info.current_w, display_info.current_h)

def toggleFullScreen():
  if pg.display.is_fullscreen():
    pg.display.set_mode(WINDOW_SIZE)
  else:
    pg.display.set_mode(MONITOR_SIZE, pg.FULLSCREEN)
  
  notify()
