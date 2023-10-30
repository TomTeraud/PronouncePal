import os
import sys

def resource_path(relative_path):
    # Check if the script is running as a bundled executable
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        return os.path.join(os.path.abspath('.'), relative_path)
