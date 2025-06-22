import os
import pickle
import json
import csv 
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from tkinter.ttk import Style
from core.settings import Settings
from core.ui.home import HomeScreen
from core.ui.addpass import AddPassDialog
from core.ui.action import ActionDialog
from core.ui.updatepass import UpdatePassDialog

class PasswordManager:
    def __init__(self, root):
        self.root = root
        self.settings = Settings()
        
        # Configure window
        self.root.title(self.settings.TITLE)
        self.root.geometry(f"{self.settings.WIDTH}x{self.settings.HEIGHT}")
        self.root.minsize(800, 600)

        try:
            self.root.iconbitmap(self.settings.ICON_PATH)
        except:
            pass
        
        # Configure style for modern look
        self.style = Style()
        self.style.theme_use('clam')
        self.configure_styles()
        
        # Initialize data
        self.todos = []
        self.read_from_file()
        
        # Create home screen
        self.home_screen = HomeScreen(self.root, self)
        
    def configure_styles(self):
        """Configure modern light styles for widgets"""
        # Base styles
        self.style.configure('.', 
                            background=self.settings.BACKGROUND,
                            foreground=self.settings.TEXT,
                            font=('Segoe UI', 10))
        
        # Frame styles
        self.style.configure('TFrame', 
                            background=self.settings.BACKGROUND)
        
        # Label styles
        self.style.configure('TLabel', 
                            background=self.settings.BACKGROUND,
                            foreground=self.settings.TEXT)
        self.style.configure('Header.TLabel', 
                            font=('Segoe UI', 12, 'bold'),
                            foreground=self.settings.TEXT)
        
        # Button styles
        self.style.configure('TButton', 
                            background=self.settings.SECONDARY_BG,
                            foreground=self.settings.TEXT,
                            borderwidth=1,
                            relief='solid',
                            padding=5)
        self.style.configure('Accent.TButton', 
                            background=self.settings.ACCENT,
                            foreground='white')
        self.style.map('TButton',
                      background=[('active', self.settings.TERTIARY_BG)],
                      relief=[('pressed', 'sunken')])
        self.style.map('Accent.TButton',
                      background=[('active', self.settings.ACCENT_HOVER), 
                                 ('!active', self.settings.ACCENT)])
        
        # Entry styles
        self.style.configure('TEntry',
                            fieldbackground=self.settings.SECONDARY_BG,
                            foreground=self.settings.TEXT,
                            insertcolor=self.settings.TEXT,
                            bordercolor=self.settings.BORDER,
                            lightcolor=self.settings.BORDER,
                            darkcolor=self.settings.BORDER)
        
        # Treeview styles
        self.style.configure('Treeview',
                            background=self.settings.SECONDARY_BG,
                            foreground=self.settings.TEXT,
                            fieldbackground=self.settings.SECONDARY_BG,
                            borderwidth=0)
        self.style.configure('Treeview.Heading',
                            background=self.settings.TERTIARY_BG,
                            foreground=self.settings.TEXT,
                            font=('Segoe UI', 10, 'bold'))
        self.style.map('Treeview',
                      background=[('selected', self.settings.ACCENT)],
                      foreground=[('selected', 'white')])
        
        # Scrollbar styles
        self.style.configure('Vertical.TScrollbar',
                            background=self.settings.TERTIARY_BG,
                            troughcolor=self.settings.BACKGROUND,
                            bordercolor=self.settings.BACKGROUND,
                            arrowcolor=self.settings.TEXT)
        self.style.configure('Horizontal.TScrollbar',
                            background=self.settings.TERTIARY_BG,
                            troughcolor=self.settings.BACKGROUND,
                            bordercolor=self.settings.BACKGROUND,
                            arrowcolor=self.settings.TEXT)
    
    # -------------------------- delete password -------------------------------
    def show_delete_dialog(self, selected_id=None):
        if selected_id is None:
            messagebox.showwarning("No Selection", "Please select an item from the table first")
            return
            
        dialog = ActionDialog(self.root, "Delete Password", self.handle_action, selected_id)
        
    def handle_action(self, id_no):
        try:
            todo_id = int(id_no) - 1  # Convert to 0-based index
            if 0 <= todo_id < len(self.todos):
                del self.todos[todo_id]
                self.save_to_file()
                self.home_screen.update_table_data(self.todos)
            else:
                messagebox.showwarning("Invalid ID", "Please enter a valid ID number")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number")
    
    # ------------------------------ export to csv ----------------------------------
    def export_to_csv(self):
        try:
            if not self.todos:
                messagebox.showinfo("No Data", "There are no passwords to export")
                return False
                
            file_path = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV Files", "*.csv")],
                initialfile="passwords.csv"
            )
            
            if not file_path:
                return False
                
            with open(file_path, mode="w", newline="", encoding="utf-8") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["Title", "Username", "Password"])
                for todo in self.todos:
                    if isinstance(todo, tuple) and len(todo) >= 3:
                        writer.writerow([todo[0], todo[1], todo[2]])
            
            messagebox.showinfo("Success", f"Passwords successfully exported to {file_path}")
            return True
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export: {str(e)}")
            return False
    
    # --------------------------- export to json -------------------------------------   
    def export_to_json(self):
        try:
            if not self.todos:
                messagebox.showinfo("No Data", "There are no passwords to export")
                return False
                
            file_path = filedialog.asksaveasfilename(
                defaultextension=".json",
                filetypes=[("JSON Files", "*.json")],
                initialfile="passwords.json"
            )
            
            if not file_path:
                return False
                
            json_data = {
                "passwords": [
                    {
                        "title": todo[0] if isinstance(todo, tuple) and len(todo) >= 1 else "",
                        "username": todo[1] if isinstance(todo, tuple) and len(todo) >= 2 else "",
                        "password": todo[2] if isinstance(todo, tuple) and len(todo) >= 3 else ""
                    }
                    for todo in self.todos
                ]
            }
            
            with open(file_path, "w") as json_file:
                json.dump(json_data, json_file, indent=4)
            
            messagebox.showinfo("Success", f"Passwords successfully exported to {file_path}")
            return True
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export: {str(e)}")
            return False
    
    # ------------------------- action save / read password list --------------
    def save_to_file(self):
        try:
            with open(self.settings.TODO_FILE, "wb") as file:
                pickle.dump(self.todos, file)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {str(e)}")
    
    def read_from_file(self):
        if os.path.exists(self.settings.TODO_FILE):
            try:
                with open(self.settings.TODO_FILE, "rb") as file:
                    self.todos = pickle.load(file)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load data: {str(e)}")
                self.todos = []
    
    # -------------------------- add passwords / handle ----------------------------------    
    def show_add_password_dialog(self):
        dialog = AddPassDialog(self.root, self.handle_pass)


    # ------------------------------ update passwords / handle ------------------------------
    def show_update_dialog(self, selected_id=None):
        if not self.todos:
            messagebox.showinfo("No Passwords", "There are no passwords to update")
            return
        if selected_id is None:
            messagebox.showwarning("No Selection", "Please select an item from the table first")
            return
            
        dialog = UpdatePassDialog(self.root, self.todos, self.handle_update, selected_id)


    def handle_update(self, todo_id, title, username, password):
        self.todos[todo_id] = (title, username, password)
        self.save_to_file()
        self.home_screen.update_table_data(self.todos) 


    def handle_search(self):
        search_text = self.home_screen.search_var.get().strip().lower()
        
        if not search_text:
            # If search is empty, reload original data
            self.read_from_file()
            self.home_screen.update_table_data(self.todos)
            return
        
        # Search in todos (title, username, or password)
        search_results = []
        for todo in self.todos:
            if (search_text in todo[0].lower() or  # title
                search_text in todo[1].lower() or  # username
                search_text in todo[2].lower()):    # password
                search_results.append(todo)
        
        if search_results:
            self.home_screen.update_table_data(search_results)
        else:
            messagebox.showinfo("No Results", "No matching passwords found")
            self.home_screen.search_var.set("")  # Clear search field

    def reset_search(self):
        """Reset the search and show all todos"""
        self.home_screen.search_var.set("")
        self.read_from_file()
        self.home_screen.update_table_data(self.todos)
    
    def handle_pass(self, title, username, password):
        if not title or not username or not password:
            messagebox.showwarning("Missing Fields", "Please fill in all fields")
            return
            
        self.todos.append((title, username, password))
        self.save_to_file()
        self.home_screen.update_table_data(self.todos)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = PasswordManager(root)
    app.run()