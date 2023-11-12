import cv2
import mediapipe as mp
import numpy as np
import random
import time
import os

# Define constants
INVISIBLE_RADIUS = 30  # Adjust the size of the invisible circle
NUM_CIRCLES = 5
GAME_DURATION = 15  # Game duration in seconds

# Get a list of all fruit images in the directory
fruit_images_directory = './back/images/fruits/'
fruit_images = [f for f in os.listdir(fruit_images_directory) if os.path.isfile(os.path.join(fruit_images_directory, f))]

# Function to choose a random fruit image
def choose_random_fruit_image():
    random_fruit_image = random.choice(fruit_images)
    fruit_image_path = os.path.join(fruit_images_directory, random_fruit_image)
    return cv2.imread(fruit_image_path, cv2.IMREAD_UNCHANGED)

# Define a class for the falling circles
class FallingCircle:
    def __init__(self, x, speed, size):
        self.x = x
        self.y = 0
        self.speed = speed
        self.size = size
        self.fruit_image = choose_random_fruit_image()

    def fall(self):
        self.y += self.speed

# Function to check collision between two circles
def check_collision(circle1, circle2):
    distance = np.sqrt((circle1[0] - circle2[0])**2 + (circle1[1] - circle2[1])**2)
    return distance < (circle1[2] + circle2[2])

# Function to run the game
def run_game():
    # Initialize MediaPipe Pose
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()

    # Initialize the video capture
    cap = cv2.VideoCapture(0)

    # Create a list to store the falling circles
    circles = []

    # Initialize the player's score
    score = 0

    # Get the start time of the game
    start_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        # Convert the frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with MediaPipe Pose
        results = pose.process(frame_rgb)

        if results.pose_landmarks:
            # Get the pixel coordinates of the head landmarks
            landmarks = []
            h, w, _ = frame.shape
            for landmark_id in [0, 1, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]:
                landmark = results.pose_landmarks.landmark[landmark_id]
                x, y = int(landmark.x * w), int(landmark.y * h)
                landmarks.append((x, y))

            # Draw the falling circles
            for circle in circles:
                # Resize the fruit image to match the dimensions of the ROI
                resized_fruit = cv2.resize(circle.fruit_image, (2 * circle.size, 2 * circle.size))

                # Extract the region of interest
                roi = frame[int(max(0, circle.y)):int(min(h, circle.y + 2 * circle.size)),
                            int(max(0, circle.x)):int(min(w, circle.x + 2 * circle.size))]

                alpha = resized_fruit[:, :, 3] / 255.0

                # Ensure the dimensions match before blending
                if roi.shape[0] == resized_fruit.shape[0] and roi.shape[1] == resized_fruit.shape[1]:
                    for c in range(0, 3):
                        roi[:, :, c] = (1 - alpha) * roi[:, :, c] + alpha * resized_fruit[:, :, c]

                circle.fall()

            # Draw the invisible circle around the player's face
            player_circle = landmarks[0]
            # cv2.circle(frame, player_circle, INVISIBLE_RADIUS, (255, 255, 255), -1, cv2.LINE_AA)

            # Check for collisions
            for circle in circles:
                if check_collision((circle.x, circle.y, circle.size), (player_circle[0], player_circle[1], INVISIBLE_RADIUS)):
                    circles.remove(circle)
                    # Increment the player's score when a circle is destroyed
                    score += 1

            # Check if a circle has reached the bottom
            circles = [circle for circle in circles if circle.y < h]

            # Generate a new circle every 3 seconds
            if time.time() - start_time < GAME_DURATION:
                if time.time() % 3 < 0.1:
                    circles.append(FallingCircle(random.randint(50, 600), random.uniform(3, 8), random.randint(20, 50)))
            else:
                # Game over, display the final score
                cv2.putText(frame, f"Score: {score} !", (int(w/4), int(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

        # Display the score on the top-left corner of the screen during the game
        cv2.putText(frame, f"Score: {score}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        # Display the remaining time on the top-right corner of the screen during the game
        remaining_time = max(0, GAME_DURATION - int(time.time() - start_time))
        cv2.putText(frame, f"Time: {remaining_time}s", (int(w - 150), 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("Circle Game", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Run the game
run_game()
