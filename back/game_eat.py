import cv2
import mediapipe as mp
import numpy as np
import random
import time
import os

class FallingCircle:
    def __init__(self, x, speed, size, fruit_image):
        self.x = x
        self.y = 0
        self.speed = speed
        self.size = size
        self.fruit_image = fruit_image

    def fall(self):
        self.y += self.speed

class GAME_Eat:
    def __init__(self, duration=60):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()
        self.cap = cv2.VideoCapture(0)

        self.circles = []
        self.score = 0
        self.game_duration = duration
        self.start_time = time.time()

        self.load_fruit_images()
        
    def load_fruit_images(self):
        fruit_images_directory = './back/images/fruits/'
        self.fruit_images = [f for f in os.listdir(fruit_images_directory) if os.path.isfile(os.path.join(fruit_images_directory, f))]

    def choose_random_fruit_image(self):
        random_fruit_image = random.choice(self.fruit_images)
        fruit_image_path = os.path.join('./back/images/fruits/', random_fruit_image)
        return cv2.imread(fruit_image_path, cv2.IMREAD_UNCHANGED)

    def check_collision(self, circle1, circle2):
        distance = np.sqrt((circle1[0] - circle2[0])**2 + (circle1[1] - circle2[1])**2)
        return distance < (circle1[2] + circle2[2])

    def run_game(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(frame_rgb)
        if results.pose_landmarks:
            landmarks = []
            h, w, _ = frame.shape
            for landmark_id in [0, 1, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]:
                landmark = results.pose_landmarks.landmark[landmark_id]
                x, y = int(landmark.x * w), int(landmark.y * h)
                landmarks.append((x, y))
            for circle in self.circles:
                resized_fruit = cv2.resize(circle.fruit_image, (2 * circle.size, 2 * circle.size))
                roi = frame[int(max(0, circle.y)):int(min(h, circle.y + 2 * circle.size)),
                            int(max(0, circle.x)):int(min(w, circle.x + 2 * circle.size))]
                alpha = resized_fruit[:, :, 3] / 255.0
                if roi.shape[0] == resized_fruit.shape[0] and roi.shape[1] == resized_fruit.shape[1]:
                    for c in range(0, 3):
                        roi[:, :, c] = (1 - alpha) * roi[:, :, c] + alpha * resized_fruit[:, :, c]
                circle.fall()
            player_circle = landmarks[0]
            for circle in self.circles:
                if self.check_collision((circle.x, circle.y, circle.size),
                                        (player_circle[0], player_circle[1], 30)):
                    self.circles.remove(circle)
                    self.score += 1
            self.circles = [circle for circle in self.circles if circle.y < h]
            if time.time() - self.start_time < self.game_duration:
                if time.time() % 3 < 0.1:
                    x = random.randint(50, 600)
                    speed = random.uniform(3, 8)
                    size = random.randint(20, 50)
                    fruit_image = self.choose_random_fruit_image()
                    self.circles.append(FallingCircle(x, speed, size, fruit_image))
            else:
                cv2.putText(frame, f"Score: {self.score} !", (int(w / 4), int(h / 2)), cv2.FONT_HERSHEY_SIMPLEX, 2,
                            (255, 255, 255), 2)
        cv2.putText(frame, f"Score: {self.score}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        remaining_time = max(0, self.game_duration - int(time.time() - self.start_time))
        cv2.putText(frame, f"Time: {remaining_time}s", (int(w - 150), 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        return frame