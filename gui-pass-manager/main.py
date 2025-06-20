import sys
import time 
import os
import pygame
import pygame_gui
#for database
import pickle  
#for exporting
import json , csv
#encyption and decryption
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
#settings 
from core.settings import Settings
#ui components
from core.ui.home import HomeScreen  
from core.ui.addpass import AddPass


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
        self.todos = []
        self.title = ''
        self.username = ''
        self.password = ''
        
        
        self.read_from_file()
        self.show_home_screen()




     # ----------------------- action save / read password list --------------
    
    def save_to_file(self):
        with open(self.settings.TODO_FILE, "wb") as file:
            pickle.dump(self.todos, file)

 
    def read_from_file(self):
        if os.path.exists(self.settings.TODO_FILE):
            with open(self.settings.TODO_FILE, "rb") as file:
                self.todos = pickle.load(file)    



    # -------------------------- add passwords / handle ----------------------------------    
        
    def add_pass(self):
        self.add_password = AddPass(
            manager=self.manager,
            position=(self.settings.WIDTH // 2 - self.settings.POPUP_WIDTH // 2, self.settings.HEIGHT // 2 - self.settings.POPUP_HEIGHT // 2),
            size=(self.settings.POPUP_WIDTH, self.settings.POPUP_HEIGHT),
            on_submit=self.handle_pass  
        )
        print(self.todos) 

    def handle_pass(self, title, username, password):
 
        print(f"Title: {title}")
        print(f"Username: {username}")
        print(f"Password: {password}")  
        
     
        self.title = title
        self.username = username
        self.password = password
        
        if hasattr(self, 'add_password'):
            self.add_password.kill()
            del self.add_password

        self.todo = self.title, self.username, self.password
        self.todos.append(self.todo)
        self.save_to_file()
    
 

    # ------------------ key genration / ecryption / decryption ---------------
    
    # def save_key():
       
    #     key = generate_key()
    #     with open(self.settings.KEY_FILE, "wb") as f:
    #         f.write(base64.b64encode(key))
    #     print(f"Encryption key saved to {KEY_FILE}. Keep it safe!")

    # def load_key():
       
    #     if not os.path.exists(KEY_FILE):
    #         raise FileNotFoundError("Encryption key file not found")
    #     with open(self.settings.KEY_FILE, "rb") as f:
    #         return base64.b64decode(f.read())

    # def encrypt_file(file_path, key):

    #     cipher = AES.new(key, AES.MODE_GCM)

    #     with open(file_path, "rb") as f:
    #         plaintext = f.read()

    #     ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    #     with open(file_path, "wb") as f:
    #         f.write(cipher.nonce)
    #         f.write(tag)
    #         f.write(ciphertext)

    # def decrypt_file(file_path, key):

    #     with open(file_path, "rb") as f:
    #         nonce = f.read(16)  # GCM nonce is 16 bytes
    #         tag = f.read(16)    # Authentication tag is 16 bytes
    #         ciphertext = f.read()

    #     cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    #     plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    #     with open(file_path, "wb") as f:
    #         f.write(plaintext)
     

 
   # ------------------------- home screen  -----------------------------

 
    def show_home_screen(self):

        self.home_screen = HomeScreen(self.manager,
            (self.settings.WIDTH, self.settings.HEIGHT),
            self.todos)


    # ---------------------------------------- all events --------------------------
   
    def handle_events(self):
      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               self.running = False
          

            #main key binds to exit the game
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.running = False


            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.home_screen.get_json():
                    print('json')
                elif event.ui_element == self.home_screen.get_csv():
                    print('csv')
                elif event.ui_element == self.home_screen.get_delete():
                    print('delete')  
                elif event.ui_element == self.home_screen.get_update():
                    print('update') 
                elif event.ui_element == self.home_screen.get_add():
                    print('add') 
                    self.add_pass()
                    
             
            if hasattr(self, 'add_password'):  
                self.add_password.handle_events(event)
            
                                               
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