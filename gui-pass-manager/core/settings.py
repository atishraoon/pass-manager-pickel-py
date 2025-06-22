# settings.py
import os
 
class Settings:
    def __init__(self):
        # Window settings
        self.WIDTH = 1300
        self.HEIGHT = 700
        self.TITLE = "pass-manager"
        self.FPS = 60
        self.ICON_PATH = os.path.join("core", "icon.ico")

        # Modern Light UI Color Scheme
        self.BACKGROUND = "#f5f5f5"  # Light background
        self.SECONDARY_BG = "#ffffff"  # White for contrast
        self.TERTIARY_BG = "#e0e0e0"  # For widgets
        self.ACCENT = "#4a90e2"  # Blue accent color
        self.ACCENT_HOVER = "#3a7bc8"  # Darker blue for hover
        self.TEXT = "#333333"  # Dark text
        self.TEXT_SECONDARY = "#666666"  # Secondary text
        self.SUCCESS = "#4CAF50"  # Green for success
        self.WARNING = "#FF9800"  # Amber for warnings
        self.ERROR = "#F44336"  # Red for errors
        self.BORDER = "#cccccc"  # Border color

        #database / export
        self.TODO_FILE = "core/data.pkl"
        self.JSON_FILE = os.path.join(os.path.expanduser("~"), "Desktop", "pass.json")
        self.CSV_FILE = os.path.join(os.path.expanduser("~"), "Desktop", "pass.csv")