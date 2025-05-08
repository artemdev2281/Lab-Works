import os
import face_recognition_models

MODELS_DIR = r"C:\models_dat"

def M(fname):
    return os.path.join(MODELS_DIR, fname)

face_recognition_models.pose_predictor_model_location            = lambda: M("shape_predictor_68_face_landmarks.dat")
face_recognition_models.pose_predictor_five_point_model_location  = lambda: M("shape_predictor_5_face_landmarks.dat")
face_recognition_models.cnn_face_detector_model_location         = lambda: M("mmod_human_face_detector.dat")
face_recognition_models.face_recognition_model_location          = lambda: M("dlib_face_recognition_resnet_model_v1.dat")

import face_recognition

known_image = face_recognition.load_image_file("known.jpg")
unknown_image = face_recognition.load_image_file("two_faces.jpg")

known_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[1]

results = face_recognition.compare_faces([known_encoding], unknown_encoding)

print(results[0])
print(known_encoding)
print(unknown_encoding)






































































































































