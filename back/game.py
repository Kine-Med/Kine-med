import cv2
import mediapipe as mp
import time
import random
import numpy as np
from game_gesture import GAME_Gesture

class Game:
	def __init__(self, name):
		self.name = name
		if (self.name == "gesture"):
			self.curgame = GAME_Gesture()

	def runGame(self, frame):
		if not self.curgame:
			with open("back/images/not_found.jpeg", "rb") as f:
				img = f.read()
				return img
		return self.curgame.run_game(frame)