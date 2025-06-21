from tkinter import ttk, Frame, Label
from tkinter.font import Font
from tkinter import ttk, Frame, Label, Entry, StringVar
from tkinter.font import Font

class HomeScreen:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.frame = Frame(root)
        self.frame.pack(fill='both', expand=True)
        
        self.create_header()
        self.create_table()
    
    def create_header(self):
        header_frame = Frame(self.frame)
        header_frame.pack(fill='x', padx=10, pady=10)
        
        # Count label
        self.count_label = Label(
            header_frame,
            text=f"Total Passwords [ {len(self.app.todos)} ]",
            font=('Segoe UI', 10, 'bold')
        )
        self.count_label.pack(side='left', padx=(0, 20))
        
        # Action buttons frame
        btn_frame = Frame(header_frame)
        btn_frame.pack(side='left', padx=10)
        
        # Action buttons
        self.add_btn = ttk.Button(
            btn_frame, 
            text="Add", 
            style='Accent.TButton',
            command=self.app.show_add_password_dialog
        )
        self.add_btn.pack(side='left', padx=5)
        
        self.update_btn = ttk.Button(
            btn_frame, 
            text="Update", 
            command=lambda: self.app.show_update_dialog(self.get_selected_id())
        )
        self.update_btn.pack(side='left', padx=5)
        
        self.delete_btn = ttk.Button(
            btn_frame, 
            text="Delete", 
            command=lambda: self.app.show_delete_dialog(self.get_selected_id())
        )
        self.delete_btn.pack(side='left', padx=5)
        
        # Search frame
        search_frame = Frame(header_frame)
        search_frame.pack(side='right', padx=10)
        
        self.search_var = StringVar()
        self.search_entry = Entry(
            search_frame, 
            textvariable=self.search_var,
            width=25,
            font=('Segoe UI', 10)
        )
        self.search_entry.pack(side='left', padx=5 , ipady=5) 
        
        self.search_btn = ttk.Button(
            search_frame,
            text="Search",
            command=self.app.handle_search
        )
        self.search_btn.pack(side='left')
        
        # Export buttons frame
        export_frame = Frame(header_frame)
        export_frame.pack(side='right', padx=10)
        
        Label(export_frame, text="Export as:").pack(side='left', padx=5)
        
        self.csv_btn = ttk.Button(
            export_frame, 
            text="CSV", 
            command=self.app.export_to_csv
        )
        self.csv_btn.pack(side='left', padx=5)
        
        self.json_btn = ttk.Button(
            export_frame, 
            text="JSON", 
            command=self.app.export_to_json
        )
        self.json_btn.pack(side='left', padx=5)
    
    def get_selected_id(self):
            selected_item = self.tree.selection()
            if selected_item:
                item = self.tree.item(selected_item[0])
                return int(item['values'][0]) - 1  # Return 0-based index
            return None    
    
    def create_table(self):
        # Create a frame for the table
        table_frame = Frame(self.frame)
        table_frame.pack(fill='both', expand=True, padx=10, pady=(0, 10))
        
        # Create a Treeview widget
        self.tree = ttk.Treeview(
            table_frame,
            columns=('ID', 'Title', 'Username', 'Password'),
            show='headings',
            selectmode='browse'
        )
        
        # Define columns
        self.tree.heading('ID', text='ID', anchor='w')
        self.tree.heading('Title', text='Title', anchor='w')
        self.tree.heading('Username', text='Username', anchor='w')
        self.tree.heading('Password', text='Password', anchor='w')
        
        # Set column widths
        self.tree.column('ID', width=50, minwidth=50)
        self.tree.column('Title', width=200, minwidth=100)
        self.tree.column('Username', width=200, minwidth=100)
        self.tree.column('Password', width=200, minwidth=100)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(fill='both', expand=True)
        
        # Populate table with data
        self.update_table_data(self.app.todos)
    
    def update_table_data(self, todos):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Add new items
        for i, todo in enumerate(todos, start=1):
            if isinstance(todo, tuple) and len(todo) >= 3:
                self.tree.insert('', 'end', values=(
                    i, 
                    todo[0], 
                    todo[1], 
                    # '*' * len(todo[2])
                    todo[2] 
                    )  
                )
        
        # Update count label
        self.count_label.config(text=f"Total Passwords [ {len(todos)} ]")