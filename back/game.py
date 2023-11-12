import cv2
import mediapipe as mp
import time
import random
import numpy as np
from game_gesture import GAME_Gesture

class Game:
	def __init__(self, name):
		self.name = name
		if (self.name == "GAME_GESTURE"):
			self.curgame = GAME_Gesture()

	def runGame(self, frame):
		return self.curgame.run_game(frame)