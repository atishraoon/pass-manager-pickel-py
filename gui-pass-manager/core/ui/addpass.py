import pygame
import pygame_gui


class AddPass:
    def __init__(self, manager, position, size, on_submit):
        self.manager = manager
        self.on_submit = on_submit
        self.window = pygame_gui.elements.UIWindow(
            rect=pygame.Rect(position, size),
            manager=manager,
            window_display_title="Add Password"
        )

        if hasattr(self.window, 'close_window_button'):
                self.window.set_blocking(False)
        
        # Create form elements
        self.title_field = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(50, 50, 300, 30),
            manager=manager,
            container=self.window,
            placeholder_text="Title"
        )
        self.title_field.set_text_length_limit(200)
        
        
        self.username_field = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(50, 150, 300, 30),
            manager=manager,
            container=self.window,
            placeholder_text="Username"
        )
        self.username_field.set_text_length_limit(200)
        
        self.password_field = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(50, 200, 300, 30),
            manager=manager,
            container=self.window,
            placeholder_text="Password"
        )
        self.password_field.set_text_hidden(True)
        self.password_field.set_text_length_limit(200)
        
        self.submit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(150, 250, 100, 40),
            text="Submit",
            manager=manager,
            container=self.window
        )
    
    def handle_events(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.submit_button:
                    title = self.title_field.get_text()
                    username = self.username_field.get_text()
                    password = self.password_field.get_text()
                    if title and username and password:  
                        if callable(self.on_submit):  
                            self.on_submit(title, username, password) 
    
    def kill(self):
        self.window.kill()