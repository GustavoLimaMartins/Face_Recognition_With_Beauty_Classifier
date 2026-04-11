import cv2
import numpy as np
import os
import face_recognition as fr

def load_images_from_folder(folder):
    images = []
    labels = []

    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))

        if filename.endswith(('.jpg', '.jpeg', '.png')) and img is not None:
            image_path = os.path.join(folder, filename)
            image = fr.load_image_file(image_path)

            face_encodings = fr.face_encodings(image)
            if face_encodings:
                face_encoding = face_encodings[0]
                images.append(face_encoding)
                labels.append(filename[:11])  # Use filename (without extension) as label

    return images, labels

def main():
    known_face_encodings, known_face_labels = load_images_from_folder('images')

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

        face_locations = fr.face_locations(rgb_small_frame)
        face_encodings = fr.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = fr.compare_faces(known_face_encodings, face_encoding)
            name = "Desconhecido"

            face_distances = fr.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_face_labels[best_match_index]

            face_names.append(name)
        
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow('Facial Recognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
