import pygame
import pygame_gui
from ..settings import *

class HomeScreen:  
    def __init__(self, manager, screen_dimensions,todos):
        self.settings = Settings()
        self.manager = manager
        self.screen_width, self.screen_height = screen_dimensions
        self.todos = todos 
        
        self.create_ui()

    def create_ui(self):
        # ------------------------------------- nav bar ------------------------------------------------
        
        # Level label on left
        self.level_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((20, 20), (150, 30)),
            text="Total Passwords",
            manager=self.manager
        )

        # Calculate positions for all components
        search_input_width = 200
        search_button_width = 80
        action_button_width = 80
        export_label_width = 80
        export_button_width = 60
        spacing = 10
        
        # Calculate start positions for each group
        search_start_x = 180  # After "Total Passwords" label
        
        # Search input field
        self.search_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(
                (search_start_x, 20),
                (search_input_width, 30)
            ),
            manager=self.manager
        )
        self.search_input.set_text_hidden(False)
        
        # Search button
        self.search_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (search_start_x + search_input_width + spacing, 20),
                (search_button_width, 30)
            ),
            text="Search",
            manager=self.manager
        )
        
        # Action buttons (Add, Update, Delete)
        action_buttons_start_x = search_start_x + search_input_width + search_button_width + (spacing * 2)
        
        # Add button
        self.add_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (action_buttons_start_x, 20),
                (action_button_width, 30)
            ),
            text="Add",
            manager=self.manager
        )
        
        # Update button
        self.update_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (action_buttons_start_x + action_button_width + spacing, 20),
                (action_button_width, 30)
            ),
            text="Update",
            manager=self.manager
        )
        
        # Delete button
        self.delete_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (action_buttons_start_x + (action_button_width + spacing) * 2, 20),
                (action_button_width, 30)
            ),
            text="Delete",
            manager=self.manager
        )
        
        # Export components (aligned to right)
        export_buttons_start_x = self.screen_width - (export_label_width + (export_button_width * 2) + (spacing * 2)) - 20
        
        # "Export as" label
        self.export_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(
                (export_buttons_start_x, 20),
                (export_label_width, 30)
            ),
            text="Export as",
            manager=self.manager
        )
        
        # CSV button
        self.csv_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (export_buttons_start_x + export_label_width + spacing, 20),
                (export_button_width, 30)
            ),  
            text="CSV",
            manager=self.manager
        )
        
        # JSON button
        self.json_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (export_buttons_start_x + export_label_width + export_button_width + (spacing * 2), 20),
                (export_button_width, 30)
            ),
            text="JSON",
            manager=self.manager
        )
        
        # Horizontal line below the header
        self.line = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect((0, 60), (self.screen_width, 1)),
            starting_height=0,
            manager=self.manager
        )
        self.line.background_colour = pygame.Color(self.settings.WHITE)

    
    def get_json(self):
        return self.json_button
    def get_csv(self):
        return self.csv_button
    def get_delete(self):
        return self.delete_button
    def get_update(self):
        return self.update_button
    def get_add(self):
        return self.add_button