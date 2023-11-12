import mediapipe as mp
import numpy as np
import random, time, cv2

class GAME_Gesture:
    def __init__(self, screen_width=640, screen_height=480, game_duration=30):
        # Initialize MediaPipe Hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()

        # Initialize the video capture
        self.cap = cv2.VideoCapture(0)  # You can change 0 to the path of a video file or a different camera index

        # Define the screen dimensions
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Initialize game variables
        self.blue_circles = []  # List to store blue circle positions
        self.red_circle = (0, 0)  # Initialize red circle as (0, 0)
        self.orange_circle = (0, 0)  # Initialize orange circle as (0, 0)
        self.green_circle = (0, 0)  # Initialize green circle as (0, 0)
        self.score = 0

        # Initial positions for blue circles on left and right fingers
        self.left_blue_circle = (0, 0)
        self.right_blue_circle = (0, 0)

        # Delay for red, orange, and green circle spawning
        self.red_circle_spawn_time = time.time()
        self.orange_circle_spawn_time = time.time()
        self.green_circle_spawn_time = time.time()

        # Game timer
        self.start_time = time.time()
        self.game_duration = game_duration  # Game duration in seconds
        self.game_paused = False

    def spawn_red_circle(self):
        x = random.randint(20, self.screen_width - 20)
        y = random.randint(20, self.screen_height - 20)
        return x, y

    def spawn_orange_circle(self):
        x = random.randint(20, self.screen_width - 20)
        y = random.randint(20, self.screen_height - 20)
        return x, y

    def run_game(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(frame_rgb)

        if results.multi_hand_landmarks and not self.game_paused:
            for hand_landmarks in results.multi_hand_landmarks:
                left_index = hand_landmarks.landmark[8] if len(hand_landmarks.landmark) > 8 else None
                right_index = hand_landmarks.landmark[12] if len(hand_landmarks.landmark) > 12 else None

                if left_index:
                    left_index_x = int(left_index.x * self.screen_width)
                    left_index_y = int(left_index.y * self.screen_height)
                    self.left_blue_circle = (left_index_x, left_index_y)

                if right_index:
                    right_index_x = int(right_index.x * self.screen_width)
                    right_index_y = int(right_index.y * self.screen_height)
                    self.right_blue_circle = (right_index_x, right_index_y)

        # Spawn a red circle every 2 seconds
        if not self.game_paused and time.time() - self.red_circle_spawn_time > 2:
            self.red_circle_spawn_time = time.time()
            self.red_circle = self.spawn_red_circle()

        # Spawn an orange circle every 4 seconds
        if not self.game_paused and time.time() - self.orange_circle_spawn_time > 4:
            self.orange_circle_spawn_time = time.time()
            self.orange_circle = self.spawn_orange_circle()

        # Merge blue circles into a green circle if fingers are close
        if (
            np.linalg.norm(np.array(self.left_blue_circle) - np.array(self.right_blue_circle)) < 30
        ):
            self.green_circle = ((self.left_blue_circle[0] + self.right_blue_circle[0]) // 2, (self.left_blue_circle[1] + self.right_blue_circle[1]) // 2)
            self.blue_circles = []  # Reset blue circles
        else:
            self.green_circle = (-50, -50)  # Reset green circle if fingers are separated

        # Detect collisions between blue/green circles and red/orange circles
        if self.red_circle is not None:
            if (
                np.linalg.norm(np.array(self.left_blue_circle) - np.array(self.red_circle)) < 20
                or np.linalg.norm(np.array(self.green_circle) - np.array(self.red_circle)) < 20
            ):
                self.red_circle = (-50, -50)  # Reset the red circle's position
                self.score += 1

            if (
                np.linalg.norm(np.array(self.right_blue_circle) - np.array(self.red_circle)) < 20
                or np.linalg.norm(np.array(self.green_circle) - np.array(self.red_circle)) < 20
            ):
                self.red_circle = (-50, -50)  # Reset the red circle's position
                self.score += 1

        if self.orange_circle is not None:
            if (
                np.linalg.norm(np.array(self.left_blue_circle) - np.array(self.orange_circle)) < 30
                and np.linalg.norm(np.array(self.right_blue_circle) - np.array(self.orange_circle)) < 30
            ):
                self.orange_circle = (-50, -50)  # Reset the orange circle's position
                self.score += 2

        # Draw blue/green circles
        for circle in self.blue_circles:
            cv2.circle(frame, circle, 20, (255, 0, 0), -1)
        cv2.circle(frame, self.left_blue_circle, 20, (255, 0, 0), -1)
        cv2.circle(frame, self.right_blue_circle, 20, (255, 0, 0), -1)

        # Draw red circle if it exists
        if self.red_circle != (0, 0):
            cv2.circle(frame, self.red_circle, 20, (0, 0, 255), -1)

        # Draw orange circle if it exists
        if self.orange_circle != (0, 0):
            cv2.circle(frame, self.orange_circle, 20, (0, 165, 255), -1)

        # Draw green circle if it exists
        if self.green_circle != (0, 0):
            cv2.circle(frame, self.green_circle, 30, (0, 255, 0), -1)

        # Display the score
        if self.game_paused:
            # If the game is paused, display the score in the center of the screen
            score_text = f"Score: {self.score}"
            text_size = cv2.getTextSize(score_text, cv2.FONT_HERSHEY_SIMPLEX, 2, 5)[0]
            text_x = (self.screen_width - text_size[0]) // 2
            text_y = (self.screen_height + text_size[1]) // 2
            cv2.putText(frame, score_text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 5)
        else:
            score_text = f"Score: {self.score}"
            cv2.putText(frame, score_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        # Display the timer in the top-right corner
        elapsed_time = int(time.time() - self.start_time)
        remaining_time = max(0, self.game_duration - elapsed_time)
        timer_text = f"Time: {remaining_time}s"
        cv2.putText(frame, timer_text, (self.screen_width - 170, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Check if the game duration has elapsed
        if elapsed_time >= self.game_duration and not self.game_paused:
            # Pause the game when time is up
            self.game_paused = True
        return frame