from tkinter import Toplevel, ttk, Label, Entry, StringVar, messagebox
from ..settings import Settings  

class AddPassDialog:
    def __init__(self, parent, on_submit):
        self.parent = parent
        self.on_submit = on_submit
        self.settings = Settings()
        
        self.window = Toplevel(parent)
        self.window.title("Add Password")
        self.window.geometry("400x300")
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
        # Title field
        Label(self.window, text="Title:").pack(pady=(20, 5))
        self.title_var = StringVar()
        self.title_entry = Entry(self.window, textvariable=self.title_var, width=45)
        self.title_entry.pack(ipady=5)
        
        # Username field
        Label(self.window, text="Username:").pack(pady=(15, 5))
        self.username_var = StringVar()
        self.username_entry = Entry(self.window, textvariable=self.username_var, width=45)
        self.username_entry.pack(ipady=5)
        
        # Password field
        Label(self.window, text="Password:").pack(pady=(15, 5))
        self.password_var = StringVar()
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
            text="Submit",
            style='Accent.TButton',
            command=self.submit
        )
        submit_btn.pack(pady=20)
    
    def submit(self):
        title = self.title_var.get().strip()
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        
        if title and username and password:
            self.on_submit(title, username, password)
            self.window.destroy()
        else:
            messagebox.showwarning("Missing Fields", "Please fill in all fields")