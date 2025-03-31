import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui.app_window import AppWindow

def main():
    app = AppWindow()
    app.run()
    
if __name__ == "__main__":
    main()