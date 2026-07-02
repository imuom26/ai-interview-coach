import cv2
import mediapipe as mp
from modules.eye_contact import *

# Setup MediaPipe
mp_face = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils

face_mesh = mp_face.FaceMesh(
    refine_landmarks=True,
    max_num_faces=1,
    min_detection_confidence=0.7
)

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Mirror effect
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect face landmarks
    results = face_mesh.process(rgb)

    # If a face is detected
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:

            # Get frame size
            h, w, _ = frame.shape

            # Get all landmarks
            landmarks = face_landmarks.landmark

            # Draw face mesh
            mp_draw.draw_landmarks(
                frame,
                face_landmarks,
                mp_face.FACEMESH_CONTOURS
            )

            # =========================
            # LEFT IRIS CENTER
            # =========================
            left_iris_x = 0
            left_iris_y = 0

            for idx in LEFT_IRIS:
                left_iris_x += landmarks[idx].x
                left_iris_y += landmarks[idx].y

            left_iris_x /= len(LEFT_IRIS)
            left_iris_y /= len(LEFT_IRIS)

            # Convert normalized coordinates to pixels
            left_iris_px = int(left_iris_x * w)
            left_iris_py = int(left_iris_y * h)

            # Draw green dot on iris center
            cv2.circle(
                frame,
                (left_iris_px, left_iris_py),
                5,
                (0, 255, 0),
                -1
            )

            # =========================
            # EYE RATIO
            # =========================
            left_corner_x = landmarks[LEFT_EYE_LEFT].x * w
            right_corner_x = landmarks[LEFT_EYE_RIGHT].x * w

            eye_ratio = (
                left_iris_px - left_corner_x
            ) / (
                right_corner_x - left_corner_x
            )

            # Display ratio
            cv2.putText(
                frame,
                f"Ratio: {eye_ratio:.2f}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

    # Show webcam
    cv2.imshow("AI Interview Coach", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()