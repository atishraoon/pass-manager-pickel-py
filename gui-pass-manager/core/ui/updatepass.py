# updatepass.py
from tkinter import Toplevel, ttk, Label, Entry, StringVar, messagebox
from ..settings import Settings

class UpdatePassDialog:
    def __init__(self, parent, todos, on_submit, selected_id):
        self.parent = parent
        self.todos = todos
        self.on_submit = on_submit
        self.selected_id = selected_id
        self.settings = Settings()
        
        self.window = Toplevel(parent)
        self.window.title("Update Password")
        self.window.geometry("400x350")
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
        
        self.create_widgets()
    
    def center_window(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'+{x}+{y}')
    
    def create_widgets(self):
        # Display selected ID (read-only)
        Label(self.window, text="Selected Item ID:").pack(pady=(10, 5))
        id_label = Label(self.window, text=str(self.selected_id + 1))  # Show as 1-based index
        id_label.pack()
        
        # Get current values
        current_title, current_username, current_password = self.todos[self.selected_id]
        
        # Title field
        Label(self.window, text="New Title:").pack(pady=(10, 5))
        self.title_var = StringVar(value=current_title)
        self.title_entry = Entry(self.window, textvariable=self.title_var, width=45)
        self.title_entry.pack(ipady=5)
        
        # Username field
        Label(self.window, text="New Username:").pack(pady=(10, 5))
        self.username_var = StringVar(value=current_username)
        self.username_entry = Entry(self.window, textvariable=self.username_var, width=45)
        self.username_entry.pack(ipady=5)
        
        # Password field
        Label(self.window, text="New Password:").pack(pady=(10, 5))
        self.password_var = StringVar(value=current_password)
        self.password_entry = Entry(
            self.window, 
            textvariable=self.password_var, 
            width=45,
            # show="*"  # Show password as asterisks
        )
        self.password_entry.pack(ipady=5)
        
        # Submit button
        submit_btn = ttk.Button(
            self.window,
            text="Update",
            style='Accent.TButton',
            command=self.submit
        )
        submit_btn.pack(pady=20)
    
    def submit(self):
        # Get new values
        new_title = self.title_var.get().strip()
        new_username = self.username_var.get().strip()
        new_password = self.password_var.get().strip()
        
        # Call the submit handler with all values
        self.on_submit(self.selected_id, new_title, new_username, new_password)
        self.window.destroy()