
from config import *


# Launcher imports
import subprocess
import time

"""
Launching the game
"""

class GameLauncher:
    def __init__(self):
        self.game_path = GAME_PATH
        self.game_window_name = GAME_WINDOW_NAME
        self.game_running = False
    
    def start_game(self):
        try:
            # Launch the program
            subprocess.Popen(self.game_path)
            self.game_running = True
            print(f"Launched {self.game_window_name} successfully.")
        except Exception as e:
            print(f"An error occurred while trying to launch the program: {e}")
            
        time.sleep(1)




"""
Viewer

get env frames,
contains the onservations as np

"""
import cv2
import numpy as np
import win32.win32gui as wind32
from mss import mss

def getWindowGeometry(name: str) -> tuple:
    """
    Get the geometry of a window.
    """
    hwnd = wind32.FindWindow(None, name)
    if hwnd == 0:
        raise ValueError(f"Window '{name}' not found")
    if not wind32.IsWindow(hwnd):
        raise ValueError(f"Invalid window handle for '{name}'")
    left, top, right, bottom = wind32.GetWindowRect(hwnd)

    return left + 10, top + 40, right - 10, bottom - 10


class GameViewer:
    def __init__(self) -> None:
        self.window_name = GAME_WINDOW_NAME
        self.sct = mss()

    @property
    def bounding_box(self):
        return getWindowGeometry(self.window_name)

    def get_raw_frame(self):
        """
        Returns the raw frame
        """
        frame = np.array(self.sct.grab(self.bounding_box))
        return frame

    def view(self):
        """
        Shows the current frame
        """
        it = 0
        while True:
            it += 1
            cur_frame = self.get_raw_frame()

            cv2.imshow("frame", cur_frame)

            if (cv2.waitKey(1) & 0xFF) == ord("q"):
                cv2.destroyAllWindows()
                break






























