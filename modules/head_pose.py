import cv2
import numpy as np


def get_head_pose(landmarks, w, h):

    nose = landmarks[1]
    chin = landmarks[152]
    left_eye = landmarks[33]
    right_eye = landmarks[263]
    left_mouth = landmarks[61]
    right_mouth = landmarks[291]

    image_points = np.array([
        (nose.x * w, nose.y * h),
        (chin.x * w, chin.y * h),
        (left_eye.x * w, left_eye.y * h),
        (right_eye.x * w, right_eye.y * h),
        (left_mouth.x * w, left_mouth.y * h),
        (right_mouth.x * w, right_mouth.y * h)
    ], dtype="double")

    model_points = np.array([
        (0.0, 0.0, 0.0),
        (0.0, -330.0, -65.0),
        (-225.0, 170.0, -135.0),
        (225.0, 170.0, -135.0),
        (-150.0, -150.0, -125.0),
        (150.0, -150.0, -125.0)
    ])

    focal_length = w
    center = (w / 2, h / 2)

    camera_matrix = np.array([
        [focal_length, 0, center[0]],
        [0, focal_length, center[1]],
        [0, 0, 1]
    ], dtype="double")

    dist_coeffs = np.zeros((4, 1))

    success, rotation_vector, translation_vector = cv2.solvePnP(
        model_points,
        image_points,
        camera_matrix,
        dist_coeffs
    )

    return rotation_vector, translation_vector