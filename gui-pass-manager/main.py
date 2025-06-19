import sys
import time 
import os
import pygame
import pygame_gui

#settings
from settings import Settings

#ui components
from home import HomeScreen  


class PygameWindow:
    def __init__(self):
        pygame.init()
        
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT))
        pygame.display.set_caption(self.settings.TITLE)
        
        # Initialize UI
        self.manager = pygame_gui.UIManager((self.settings.WIDTH, self.settings.HEIGHT))
        
        # variable and states
        self.running = True


        self.show_home_screen()

 
   # ------------------------- home screen  -----------------------------

 
    def show_home_screen(self):

        self.home_screen = HomeScreen(self.manager, (self.settings.WIDTH, self.settings.HEIGHT))
       

    # ---------------------------------------- all events --------------------------
   
    def handle_events(self):
      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               self.running = False
          

            #main key binds to exit the game
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.running = False
            
           
    
                                               
            # Always pass events to the UI manager
            self.manager.process_events(event)




    # ------------------------------- update instance --------------------------------
    
    def update(self):
        
        self.screen.fill(self.settings.BACKGROUND_COLOR)
        self.manager.update(pygame.time.Clock().tick(self.settings.FPS) / 1000.0)
        self.manager.draw_ui(self.screen)
        pygame.display.flip()

    # -------------------------------- main running ----------------------------------
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
        pygame.quit()

if __name__ == "__main__":
    game = PygameWindow()
    game.run()