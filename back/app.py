from flask import Flask, request, render_template, Response
from flask_cors import CORS
from pathlib import Path
from camera import Camera

app = Flask(__name__)
CORS(app)

camera = Camera()
camera.run()

@app.route("/video_feed")
def video_feed():
	gameName = request.args.get('game')
	camera.setGame(gameName)
	return Response(gen(camera),
		mimetype="multipart/x-mixed-replace; boundary=frame")

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
			   b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')

if __name__ == '__main__':
    app.run()
