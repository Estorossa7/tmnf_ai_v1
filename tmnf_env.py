
from config import *
from game_utils import GameViewer, KeyboardInput

import pyautogui

class TmnfEnv:
    def __init__(self):
        self.action_space = ACTION_SPACE
        self.viewer = GameViewer()
        self.observation_shape = self.viewer.get_raw_frame().shape()
        
        self.set_training_hyperparas()
        
    def set_training_hyperparas(self):
        self.total_reward = 0.0
        self.n_steps = 0
        self.max_steps = 1000
        self.command_frequency = 50
        self.last_action = None


    def get_observation(self):
        return self.viewer.get_raw_frame()

    def step(self, action):
        reward = 0
        values = ACTION_SPACE.values()
        for i, a in enumerate(action):
            if a:
                pyautogui.press(values[i])
                
        obs = self.viewer.get_raw_frame()
        
        return obs
    
    def reset(self):
        pyautogui.press('backspace')
        self.set_training_hyperparas()
        