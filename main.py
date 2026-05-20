import cv2
import time

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_frontalface_default.xml'
)

kamera_masuk = cv2.VideoCapture(0)
kamera_keluar = cv2.VideoCapture(1)

if not kamera_keluar.isOpened():
    kamera_keluar = cv2.VideoCapture(0)

jumlah_orang = 0

last_detect_masuk = 0
last_detect_keluar = 0

cooldown = 3

while True:

    ret1, frame_masuk = kamera_masuk.read()
    ret2, frame_keluar = kamera_keluar.read()

    if not ret1:
        break

    if not ret2:
        frame_keluar = frame_masuk.copy()

    frame_masuk = cv2.resize(frame_masuk, (640, 480))
    frame_keluar = cv2.resize(frame_keluar, (640, 480))

    gray_masuk = cv2.cvtColor(
        frame_masuk,
        cv2.COLOR_BGR2GRAY
    )

    gray_keluar = cv2.cvtColor(
        frame_keluar,
        cv2.COLOR_BGR2GRAY
    )

    wajah_masuk = face_cascade.detectMultiScale(
        gray_masuk,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in wajah_masuk:

        cv2.rectangle(
            frame_masuk,
            (x, y),
            (x+w, y+h),
            (0,255,0),
            2
        )

        cv2.putText(
            frame_masuk,
            "MASUK",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )

        now = time.time()

        if now - last_detect_masuk > cooldown:

            jumlah_orang += 1
            last_detect_masuk = now

    wajah_keluar = face_cascade.detectMultiScale(
        gray_keluar,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in wajah_keluar:

        cv2.rectangle(
            frame_keluar,
            (x, y),
            (x+w, y+h),
            (255,255,0),
            2
        )

        cv2.putText(
            frame_keluar,
            "KELUAR",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255,255,0),
            2
        )

        now = time.time()

        if now - last_detect_keluar > cooldown:

            jumlah_orang -= 1

            if jumlah_orang < 0:
                jumlah_orang = 0

            last_detect_keluar = now

    cv2.putText(
        frame_masuk,
        f"TOTAL DALAM RUANGAN : {jumlah_orang}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,0,255),
        2
    )

    cv2.putText(
        frame_keluar,
        f"TOTAL DALAM RUANGAN : {jumlah_orang}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
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