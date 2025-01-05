import os
import pickle
import json
import sys
import csv
 
todos = []
TODO_FILE = "E:/tool/scripts/data.pkl"
JSON_FILE = os.path.join(os.path.expanduser("~"), "Desktop", "todos.json")
CSV_FILE = os.path.join(os.path.expanduser("~"), "Desktop", "todos.csv")

def clear_console():
    """Clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')


class Todo:
    def __init__(self, title, username, password):
        self.title = title
        self.username = username
        self.password = password


def save_to_file():
    with open(TODO_FILE, "wb") as file:
        pickle.dump(todos, file)


def read_from_file():
    global todos
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "rb") as file:
            todos = pickle.load(file)


def add_todo():
    title = input("Enter the title: ")
    username = input("Type username: ")
    password = input("Type password: ")

    todo = Todo(title, username, password)
    todos.append(todo)
    save_to_file()


def print_all_todos(todos_to_print=None):
    clear_console()
    todos_to_print = todos_to_print if todos_to_print is not None else todos
    print("+----+--------------------------------+------------------------------------------+---------------------+")
    print("| ID |            Title               |                Username                  |      Password       |")
    print("+----+--------------------------------+------------------------------------------+---------------------+")

    for i, todo in enumerate(todos_to_print):
        print(f"| {i + 1:2} | {todo.title:30} | {todo.username:40} | {todo.password:20}|")

    print("+----+--------------------------------+------------------------------------------+---------------------+")


def update_todo():
    try:
        todo_id = int(input("Enter the ID of the todo to update: ")) - 1
        if 0 <= todo_id < len(todos):
            print("Leave a field blank to keep the current value.")
            new_title = input(f"Enter new title (current: {todos[todo_id].title}): ").strip() or todos[todo_id].title
            new_username = input(f"Enter new username (current: {todos[todo_id].username}): ").strip() or todos[todo_id].username
            new_password = input(f"Enter new password (current: {todos[todo_id].password}): ").strip() or todos[todo_id].password
            
            todos[todo_id].title = new_title
            todos[todo_id].username = new_username
            todos[todo_id].password = new_password
            
            save_to_file()
        else:
            print("Invalid todo ID.")
    except ValueError:
        print("Invalid input.")


def delete_todo():
    try:
        todo_id = int(input("Enter the ID: ")) - 1
        if 0 <= todo_id < len(todos):
            del todos[todo_id]
            save_to_file()
        else:
            print("Invalid todo ID.")
    except ValueError:
        print("Invalid input.")


def search_todos(search_term):
    clear_console()
    results = [(i + 1, todo) for i, todo in enumerate(todos) if search_term.lower() in todo.title.lower()]
    if not results:
        print("No matching todos found.")
    else:
        print("+----+--------------------------------+------------------------------------------+---------------------+")
        print("| ID |            Title               |                Username                  |      Password       |")
        print("+----+--------------------------------+------------------------------------------+---------------------+")
        for i, todo in results:
            print(f"| {i:2} | {todo.title:30} | {todo.username:40} | {todo.password:20}|")
        print("+----+--------------------------------+------------------------------------------+---------------------+")

    exit(0)    

def show_options():
    while True:
        user_choice = input("Type 'A' to add, 'D' to delete, 'U' to update, 'S' to search, 'Q' to quit: ").upper()
        if user_choice == 'A':
            add_todo()
        elif user_choice == 'D':
            delete_todo()
        elif user_choice == 'U':
            update_todo()
        elif user_choice == 'S':
            search_term = input("Enter search term: ")
            search_todos(search_term)         
        elif user_choice == 'Q':
            break
        else:
            print("Command not found.")

        print_all_todos()


def is_this_first_time():
    if os.path.exists(TODO_FILE):
        read_from_file()
        print_all_todos()
    else:
        print("Welcome to CLI Password Manager App")
        add_todo()
        print_all_todos()


def export_to_json():
    json_data = {
        "passwords": [
            {"title": todo.title, "username": todo.username, "password": todo.password} for todo in todos
        ]
    }
    with open(JSON_FILE, "w") as json_file:
        json.dump(json_data, json_file, indent=4)
    print(f"Todos exported to {JSON_FILE}")


def export_to_csv():

    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(["Title", "Username", "Password"])

        for todo in todos:
            writer.writerow([todo.title, todo.username, todo.password])
    
    print(f"Todos exported to {CSV_FILE}")


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[32;1m")
    
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'json':
        read_from_file()
        export_to_json()
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'csv':
        read_from_file()
        export_to_csv()
    else:
        is_this_first_time()
        show_options()