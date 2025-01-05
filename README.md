# CLI Password Manager

A simple Command Line Interface (CLI) Password Manager application for securely storing and managing your passwords. The application allows you to add, update, delete, search, and export stored credentials in JSON or CSV formats.

---

## Features

1. **Add Passwords:** Store a new password entry with a title, username, and password.
2. **View Passwords:** Display all saved entries in a formatted table.
3. **Update Passwords:** Edit an existing entry without losing its position in the list.
4. **Delete Passwords:** Remove any saved entry.
5. **Search Passwords:** Find entries using a search term.
6. **Export to JSON or CSV:** Save all stored credentials into JSON or CSV files for backup or sharing purposes.

---

## File Structure

- **`data.pkl`**: Stores the encrypted data for todos using Python's `pickle` module.
- **`todos.json`**: JSON export of the stored credentials.
- **`todos.csv`**: CSV export of the stored credentials.

---

## Setup and Usage

### Installation

1. Clone or download the repository.
2. Install Python if it’s not already installed.

### Running the Application

Run the application by executing:

```bash
python pass.py
```

### Command-line Arguments

- **Export to JSON:**

```bash
python pass.py json
```

- **Export to CSV:**

```bash
python pass.py csv
```

---

## Application Workflow

1. **First-time Setup:** If no `data.pkl` file exists, the app will prompt you to add your first entry.
2. **Interactive Options:**
   - `A`: Add a new password entry.
   - `D`: Delete an entry.
   - `U`: Update an entry.
   - `S`: Search for entries.
   - `Q`: Quit the application.
3. **Data Persistence:** All changes are automatically saved in `data.pkl`.

---


## Security Note

This application saves passwords in plain text. It is advisable to use it only for personal or non-critical data. For a more secure implementation, consider using encryption techniques.

---

## Customization

- **File Paths:** Modify the `TODO_FILE`, `JSON_FILE`, and `CSV_FILE` variables to change the default storage and export locations.
---

## Acknowledgments

Special thanks to the Python community for the tools and libraries used in this project.

