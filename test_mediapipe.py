import mediapipe as mp

mp_face = mp.solutions.face_mesh

face_mesh = mp_face.FaceMesh(
    refine_landmarks=True,
    max_num_faces=1,
    min_detection_confidence=0.7
)

print("MediaPipe OK")
