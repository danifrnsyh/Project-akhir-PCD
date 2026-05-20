import cv2
import dlib
import time
import math
from imutils import face_utils

detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor(
    "shape_predictor_68_face_landmarks.dat"
)

kamera_masuk = cv2.VideoCapture(0)
kamera_keluar = cv2.VideoCapture(1)

if not kamera_keluar.isOpened():
    kamera_keluar = cv2.VideoCapture(0)

jumlah_orang = 0

tracked_masuk = []
tracked_keluar = []

jarak_maksimal = 80

def euclidean(p1, p2):

    return math.sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2
    )

while True:

    ret1, frame_masuk = kamera_masuk.read()
    ret2, frame_keluar = kamera_keluar.read()

    if not ret1:
        break

    if not ret2:
        frame_keluar = frame_masuk.copy()

    frame_masuk = cv2.resize(
        frame_masuk,
        (640, 480)
    )

    frame_keluar = cv2.resize(
        frame_keluar,
        (640, 480)
    )

    gray_masuk = cv2.cvtColor(
        frame_masuk,
        cv2.COLOR_BGR2GRAY
    )

    gray_keluar = cv2.cvtColor(
        frame_keluar,
        cv2.COLOR_BGR2GRAY
    )

    garis_y = 240

    cv2.line(
        frame_masuk,
        (0, garis_y),
        (640, garis_y),
        (0,255,0),
        2
    )

    cv2.line(
        frame_keluar,
        (0, garis_y),
        (640, garis_y),
        (255,255,0),
        2
    )

    wajah_masuk = detector(gray_masuk)

    current_masuk = []

    for face in wajah_masuk:

        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        center_x = int((x1 + x2) / 2)
        center_y = int((y1 + y2) / 2)

        current_masuk.append(
            (center_x, center_y)
        )

        cv2.rectangle(
            frame_masuk,
            (x1, y1),
            (x2, y2),
            (0,255,0),
            2
        )

        shape = predictor(
            gray_masuk,
            face
        )

        shape = face_utils.shape_to_np(shape)

        for (x, y) in shape:

            cv2.circle(
                frame_masuk,
                (x, y),
                1,
                (0,0,255),
                -1
            )

        cv2.circle(
            frame_masuk,
            (center_x, center_y),
            4,
            (255,0,0),
            -1
        )

        cv2.putText(
            frame_masuk,
            "MASUK",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )

        sudah_terdeteksi = False

        for titik in tracked_masuk:

            jarak = euclidean(
                titik,
                (center_x, center_y)
            )

            if jarak < jarak_maksimal:
                sudah_terdeteksi = True
                break

        if not sudah_terdeteksi:

            if center_y > garis_y:

                jumlah_orang += 1

                tracked_masuk.append(
                    (center_x, center_y)
                )

    wajah_keluar = detector(gray_keluar)

    current_keluar = []

    for face in wajah_keluar:

        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        center_x = int((x1 + x2) / 2)
        center_y = int((y1 + y2) / 2)

        current_keluar.append(
            (center_x, center_y)
        )

        cv2.rectangle(
            frame_keluar,
            (x1, y1),
            (x2, y2),
            (255,255,0),
            2
        )

        shape = predictor(
            gray_keluar,
            face
        )

        shape = face_utils.shape_to_np(shape)

        for (x, y) in shape:

            cv2.circle(
                frame_keluar,
                (x, y),
                1,
                (255,0,0),
                -1
            )

        cv2.circle(
            frame_keluar,
            (center_x, center_y),
            4,
            (0,255,255),
            -1
        )

        cv2.putText(
            frame_keluar,
            "KELUAR",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255,255,0),
            2
        )

        sudah_terdeteksi = False

        for titik in tracked_keluar:

            jarak = euclidean(
                titik,
                (center_x, center_y)
            )

            if jarak < jarak_maksimal:
                sudah_terdeteksi = True
                break

        if not sudah_terdeteksi:

            if center_y > garis_y:

                jumlah_orang -= 1

                if jumlah_orang < 0:
                    jumlah_orang = 0

                tracked_keluar.append(
                    (center_x, center_y)
                )

    tracked_masuk = current_masuk
    tracked_keluar = current_keluar

    cv2.putText(
        frame_masuk,
        f"TOTAL ORANG : {jumlah_orang}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0,0,255),
        2
    )

    cv2.putText(
        frame_keluar,
        f"TOTAL ORANG : {jumlah_orang}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0,0,255),
        2
    )

    cv2.imshow(
        "KAMERA MASUK",
        frame_masuk
    )

    cv2.imshow(
        "KAMERA KELUAR",
        frame_keluar
    )

    tombol = cv2.waitKey(1)

    if tombol == 27:
        break

kamera_masuk.release()
kamera_keluar.release()

cv2.destroyAllWindows()