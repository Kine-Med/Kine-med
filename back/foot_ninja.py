import cv2
import numpy as np
import time
import random
import mediapipe as mp

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Initialize video capture
cap = cv2.VideoCapture(0)  # Change to the appropriate camera index if needed

# Set the height at which the red circles will appear
circle_height = 350

# Store information about the red circle and game state
red_circle = {
    'center': (0, 0),
    'radius': 20,
    'visible': False,
    'disappear_time': 0
}

game_start_time = time.time()
game_duration = 10  # 60 seconds
score = 0
game_paused = False

# Function to check if the knee is within the red circle
def is_knee_in_circle(knee, circle):
    distance = np.linalg.norm(np.array(knee) - np.array(circle['center']))
    return distance < circle['radius'] * 1.5

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Pose
    results = pose.process(frame_rgb)

    if results.pose_landmarks:
        # Get the pixel coordinates of the knee landmarks (left and right)
        h, w, _ = frame.shape
        left_knee = (
            int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE].x * w),
            int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE].y * h)
        )
        right_knee = (
            int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x * w),
            int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y * h)
        )

        # Check if the knees are in the red circle
        left_knee_in_circle = is_knee_in_circle(left_knee, red_circle)
        right_knee_in_circle = is_knee_in_circle(right_knee, red_circle)

        if red_circle['visible'] and (left_knee_in_circle or right_knee_in_circle):
            red_circle['visible'] = False
            score += 1

        # Draw the red circle after a certain time interval
        current_time = time.time()
        if current_time - red_circle['disappear_time'] > 5:  # Adjust the time interval as needed
            red_circle['center'] = (random.randint(150, w - 150), circle_height)
            red_circle['visible'] = True
            red_circle['disappear_time'] = current_time

        # Draw the red circle on the frame
        if red_circle['visible']:
            cv2.circle(frame, red_circle['center'], red_circle['radius'], (0, 0, 255), -1)

        # Draw the pose landmarks in blue with larger circles
        cv2.circle(frame, left_knee, 20, (255, 0, 0), -1)
        cv2.circle(frame, right_knee, 20, (255, 0, 0), -1)

    frame = cv2.flip(frame, 1)

    # Draw the score and remaining time
    cv2.putText(frame, f"Score: {score}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display the timer on the top-right corner
    elapsed_time = time.time() - game_start_time
    remaining_time = max(0, game_duration - elapsed_time)
    timer_text = f"Time: {int(remaining_time)}s"
    cv2.putText(frame, timer_text, (frame.shape[1] - 150, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Check if the game duration has elapsed
    if game_paused:
        # Display the final score in the center of the screen
        score_text = f"Score: {score}"
        text_size = cv2.getTextSize(score_text, cv2.FONT_HERSHEY_SIMPLEX, 2, 5)[0]
        text_x = (frame.shape[1] - text_size[0]) // 2
        text_y = (frame.shape[0] + text_size[1]) // 2
        cv2.putText(frame, score_text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)

    if elapsed_time >= game_duration:
        game_paused = True

    cv2.imshow("Knee Game", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
