# action.py
from tkinter import Toplevel, ttk, Label, messagebox
from ..settings import Settings

class ActionDialog:
    def __init__(self, parent, title, on_submit, selected_id=None):
        self.parent = parent
        self.on_submit = on_submit
        self.settings = Settings()
        
        self.window = Toplevel(parent)
        self.window.title(title)
        self.window.geometry("300x150")
        self.window.resizable(False, False)
        
        # Set icon
        try:
            self.window.iconbitmap(self.settings.ICON_PATH)
        except:
            pass  # Icon not found, continue without it
            
        # Center the window
        self.center_window()
        self.window.transient(parent)
        self.window.grab_set()
        
        self.create_widgets(title, selected_id)
    
    def center_window(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'+{x}+{y}')
    
    def create_widgets(self, title, selected_id):
        if selected_id is None:
            Label(self.window, text=f"Select an item to {title.lower()} from the table").pack(pady=(30, 10))
        else:
            Label(self.window, text=f"Are you sure you want to {title.lower()} item #{selected_id + 1}?").pack(pady=(30, 10))
        
        submit_btn = ttk.Button(
            self.window,
            text="Confirm" if selected_id is not None else "Close",
            style='Accent.TButton' if selected_id is not None else '',
            command=lambda: self.submit(selected_id) if selected_id is not None else self.window.destroy()
        )
        submit_btn.pack(pady=20)
    
    def submit(self, selected_id):
        if selected_id is not None:
            self.on_submit(str(selected_id + 1))  # Convert to 1-based index
        self.window.destroy()