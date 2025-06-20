import pygame
import pygame_gui
from ..settings import *

class HomeScreen:  
    def __init__(self, manager, screen_dimensions, todos):
        self.settings = Settings()
        self.manager = manager
        self.screen_width, self.screen_height = screen_dimensions
        self.todos = todos 
        self.table_rows = []
        
        self.create_ui()
        self.create_todos_table()  # Add this line to create the table when initializing

    def create_ui(self):
        # ------------------------------------- nav bar ------------------------------------------------
        
        # Level label on left
        self.level_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((20, 20), (150, 30)),
            text=f"Total Passwords [ {len(self.todos)} ]",  
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


    def create_todos_table(self):
        if not self.todos:
            no_todos_label = pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect((20, 80), (self.screen_width - 40, 30)),
                text="No todos to display",
                manager=self.manager
            )
            return

        # Table parameters
        start_y = 80
        row_height = 30
        padding = 10
        
        # Calculate column widths (now with 4 columns including ID)
        id_width = int(self.screen_width * 0.1)  # For ID column
        col1_width = int(self.screen_width * 0.25)  # Username
        col2_width = int(self.screen_width * 0.35)  # Password
        col3_width = int(self.screen_width * 0.3)   # Website
        
        # Create headers with ID as first column
        headers = ["ID", "Username", "Password", "Website"]
        header_x = 20
        
      
        self.id_header = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((header_x, start_y), (id_width, row_height)),
            text=headers[0],
            manager=self.manager
        )
        header_x += id_width + padding
        
      
        self.col1_header = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((header_x, start_y), (col1_width, row_height)),
            text=headers[1],
            manager=self.manager
        )
        header_x += col1_width + padding
        
       
        self.col2_header = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((header_x, start_y), (col2_width, row_height)),
            text=headers[2],
            manager=self.manager
        )
        header_x += col2_width + padding
        
        
        self.col3_header = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((header_x, start_y), (col3_width, row_height)),
            text=headers[3],
            manager=self.manager
        )
        
        # Create horizontal line under headers
        self.header_line = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect((20, start_y + row_height + 5), (self.screen_width - 40, 1)),
            starting_height=0,
            manager=self.manager
        )
        self.header_line.background_colour = pygame.Color(self.settings.WHITE)
        
        # Create todo rows with ID numbers
        for i, todo in enumerate(self.todos, start=1):  # Start counting from 1
            row_y = start_y + row_height + 10 + ((i-1) * row_height)  # Adjust for 1-based index
            row_x = 20
            
            # ID Column (row number)
            id_label = pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect((row_x, row_y), (id_width, row_height)),
                text=str(i),  # This shows the row number
                manager=self.manager
            )
            row_x += id_width + padding
            
            # Username Column (first item in tuple)
            col1_label = pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect((row_x, row_y), (col1_width, row_height)),
                text=str(todo[0]),
                manager=self.manager
            )
            row_x += col1_width + padding
            
            # Password Column (second item in tuple)
            col2_label = pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect((row_x, row_y), (col2_width, row_height)),
                text=str(todo[1]),
                manager=self.manager
            )
            row_x += col2_width + padding
            
            # Website Column (third item in tuple)
            col3_label = pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect((row_x, row_y), (col3_width, row_height)),
                text=str(todo[2]),
                manager=self.manager
            )
            
            # Add horizontal line between rows
            if i < len(self.todos):
                row_line = pygame_gui.elements.UIPanel(
                    relative_rect=pygame.Rect((20, row_y + row_height + 5), (self.screen_width - 40, 1)),
                    starting_height=0,
                    manager=self.manager
                )
                row_line.background_colour = pygame.Color(self.settings.WHITE)


    def clear_table_rows(self):
        """Remove all existing table row elements"""
        for element in self.table_rows:
            element.kill()
        self.table_rows = []

    def update_table_data(self, new_todos):
        """Update the table with new data"""
        self.todos = new_todos
        self.create_todos_table()
        
        # Update the count label
        self.level_label.set_text(f"Total Passwords [ {len(self.todos)} ]")            




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