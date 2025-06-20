import os
import pygame

class Settings:
    def __init__(self):
        
        # Window settings
        self.WIDTH = 1300
        self.HEIGHT = 700
        self.TITLE = "pass-manager"
        self.FPS = 60

        # Colors
        self.BACKGROUND_COLOR = (30, 30, 30)  
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.NAV_BUTTON_COLOR = (70, 70, 70)
        self.NAV_BUTTON_HOVER_COLOR = (100, 100, 100)
        self.BUTTON_TEXT_COLOR = (220, 220, 220)

        #database / export
        self.TODO_FILE = "core/data.pkl"
        self.JSON_FILE = os.path.join(os.path.expanduser("~"), "Desktop", "pass.json")
        self.CSV_FILE = os.path.join(os.path.expanduser("~"), "Desktop", "pass.csv")

        # Popup settings
        self.POPUP_WIDTH = 500
        self.POPUP_HEIGHT = 600
        self.POPUP_TITLE_COLOR = (70, 130, 180)


   
 
        
       
        
      
    
   