import pygame
import pygame_gui
from settings import *

class HomeScreen:  
    def __init__(self, manager, screen_dimensions):
        self.settings = Settings()
        self.manager = manager
        self.screen_width, self.screen_height = screen_dimensions
        
        self.create_ui()

    def create_ui(self):
        # ------------------------------------- nav bar ------------------------------------------------
        
        # Level label on left
        self.level_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((20, 20), (100, 30)),
            text="total password!",
            manager=self.manager
        )

        # Calculate positions for export group (aligned to right)
        export_label_width = 100
        button_width = 60
        spacing = 5
        total_width = export_label_width + (button_width * 2) + (spacing * 2)
        start_x = self.screen_width - total_width - 20  # 20px from right edge

        # "Export as" label
        self.export_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(
                (start_x, 20),
                (export_label_width, 30)
            ),
            text="Export as",
            manager=self.manager
        )

        # CSV button
        self.csv_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (start_x + export_label_width + spacing, 20),
                (button_width, 30)
            ),  
            text="CSV",
            manager=self.manager
        )

        # JSON button
        self.json_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (start_x + export_label_width + button_width + (spacing * 2), 20),
                (button_width, 30)
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

    def get_purpose_button(self):
        return self.purpose_button