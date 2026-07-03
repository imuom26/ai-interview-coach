import cv2
import mediapipe as mp
import time
from modules.eye_contact import *
from modules.head_pose import *
from scorer import *

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

start_time = time.time()

look_away_count = 0
looking_away = False

eye_contact_frames = 0
total_frames = 0

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Mirror effect
    frame = cv2.flip(frame, 1)

    # Convert BGR -> RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect face landmarks
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:

            # Frame size
            h, w, _ = frame.shape

            # All landmarks
            landmarks = face_landmarks.landmark

            # Draw face mesh
            mp_draw.draw_landmarks(
                frame,
                face_landmarks,
                mp_face.FACEMESH_CONTOURS
            )

            # =========================
            # RIGHT IRIS CENTER
            # =========================
            iris_x = 0
            iris_y = 0

            for idx in RIGHT_IRIS:
                iris_x += landmarks[idx].x
                iris_y += landmarks[idx].y

            iris_x /= len(RIGHT_IRIS)
            iris_y /= len(RIGHT_IRIS)

            # Convert to pixels
            iris_px = int(iris_x * w)
            iris_py = int(iris_y * h)

            # Draw green dot
            cv2.circle(
                frame,
                (iris_px, iris_py),
                5,
                (0, 255, 0),
                -1
            )

            # =========================
            # EYE RATIO
            # =========================

            corner1 = landmarks[RIGHT_EYE_LEFT].x * w
            corner2 = landmarks[RIGHT_EYE_RIGHT].x * w

            left_corner_x = min(corner1, corner2)
            right_corner_x = max(corner1, corner2)

            eye_width = right_corner_x - left_corner_x

            if eye_width != 0:
                eye_ratio = (
                    iris_px - left_corner_x
                ) / eye_width
            else:
                eye_ratio = 0
            
            # =========================
            # LOOK-AWAY WARNING
            # =========================
            warning = ""

            if eye_ratio < -2.0:
                warning = "Please look at the camera"

                if not looking_away:
                    look_away_count += 1
                    looking_away = True
            else:
                looking_away = False
            
            total_frames += 1

            if -2.5 < eye_ratio < 2.5:
               eye_contact_frames += 1

            eye_contact_percent = (
                eye_contact_frames / total_frames
            ) * 100
            
            rotation_vector, translation_vector = get_head_pose(
                landmarks,
                w,
                h
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

            # Debug info
            cv2.putText(
                frame,
                f"IrisX:{iris_px}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"Eye Contact: {eye_contact_percent:.0f}%",
                (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 255),
                2
            )
            
            cv2.putText(
                frame,
                f"Head Rot X:{rotation_vector[0][0]:.2f}",
                (20, 160),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"Head Rot Y:{rotation_vector[1][0]:.2f}",
                (20, 200),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 0),
                2
         )
            elapsed = int(time.time() - start_time)

            minutes = elapsed // 60
            seconds = elapsed % 60

            cv2.putText(
                frame,
                f"Duration: {minutes:02}:{seconds:02}",
                (20, 240),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2
            )

            if warning != "":
                cv2.putText(
                    frame,
                    warning,
                    (20, 280),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 0, 255),
                    2
     )

    # Show webcam
    cv2.imshow("AI Interview Coach", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
           
        elapsed = int(time.time() - start_time)

        minutes = elapsed // 60
        seconds = elapsed % 60

        print("\n========================")
        print("AI INTERVIEW REPORT")
        attention_score = calculate_attention_score(
            eye_contact_percent,
            look_away_count
     )

        print("\n========================")
        print("AI INTERVIEW REPORT")
        print("========================")
        print(f"Duration: {minutes:02}:{seconds:02}")
        print(f"Eye Contact: {eye_contact_percent:.0f}%")
        print(f"Looked Away: {look_away_count} times")
        print(f"Attention Score: {attention_score}%")
        if attention_score >= 85:
            print("Feedback: Excellent focus and eye contact.")
        elif attention_score >= 70:
            print("Feedback: Good attention. Try to look away less.")
        else:
            print("Feedback: Practice maintaining eye contact.")
      
# Cleanup
cap.release()
cv2.destroyAllWindows()