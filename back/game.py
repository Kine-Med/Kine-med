import cv2
import mediapipe as mp
import time
import random
import numpy as np
from game_gesture import GAME_Gesture
from game_knee import GAME_Knee
from game_eat import GAME_Eat

class Game:
	def __init__(self, name):
		self.name = name
		if (self.name == "gesture"):
			self.curgame = GAME_Gesture()
		if (self.name == "knee"):
			self.curgame = GAME_Knee()
		if (self.name == "eat"):
			self.curgame = GAME_Eat()

	def runGame(self, frame):
		if not self.curgame:
			with open("back/images/not_found.jpeg", "rb") as f:
				img = f.read()
				return img
		return self.curgame.run_game(frame)