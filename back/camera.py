import cv2
import threading
import time
from game import Game

thread = None

class Camera:
	def __init__(self,fps=60,video_source=0):
		self.fps = fps
		self.video_source = video_source
		self.camera = cv2.VideoCapture(self.video_source)
		# We want a max of 5s history to be stored, thats 5s*fps
		self.max_frames = 5*self.fps
		self.frames = []
		self.isrunning = False
		self.game = Game("gesture")

	def setGame(self, gameName):
		self.game = Game(gameName)

	def run(self):
		global thread
		if thread is None:
			thread = threading.Thread(target=self._capture_loop,daemon=True)
			self.isrunning = True
			thread.start()

	def _capture_loop(self):
		dt = 1/self.fps
		while self.isrunning:
			v,im = self.camera.read()
			im = cv2.flip(im, 1)
			im = self.game.runGame(im)
			if v:
				if len(self.frames)==self.max_frames:
					self.frames = self.frames[1:]
				self.frames.append(im)
			time.sleep(dt)

	def stop(self):
		self.isrunning = False
	def get_frame(self, _bytes=True):
		if len(self.frames)>0:
			if _bytes:
				img = cv2.imencode('.png',self.frames[-1])[1].tobytes()
			else:
				img = self.frames[-1]
		else:
			with open("back/images/not_found.jpeg", "rb") as f:
				img = f.read()
				return img
		return img