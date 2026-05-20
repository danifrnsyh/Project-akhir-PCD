# Deteksi dan Penghitungan Orang Menggunakan Dua Kamera Realtime dengan Metode Facial Landmark Detection

Project akhir mata kuliah Pengolahan Citra Digital menggunakan Python, OpenCV, dan metode Facial Landmark Detection untuk mendeteksi dan menghitung jumlah orang secara realtime menggunakan dua kamera.

## Deskripsi Project

Sistem ini menggunakan dua kamera realtime yang ditempatkan pada:

* Pintu masuk
* Pintu keluar

Metode utama yang digunakan adalah:

```text id="ax7b4v"
Facial Landmark Detection
```

Metode ini digunakan untuk mendeteksi titik-titik penting pada wajah manusia seperti:

* Mata
* Hidung
* Bibir
* Garis wajah

Sistem bekerja secara realtime untuk mendeteksi wajah manusia dan menghitung jumlah orang yang masuk dan keluar ruangan.

## Logika Sistem

### Kamera Masuk

Jika kamera masuk mendeteksi wajah manusia:

```text id="ek1ntm"
Jumlah Orang +1
```

### Kamera Keluar

Jika kamera keluar mendeteksi wajah manusia:

```text id="xdxvks"
Jumlah Orang -1
```

### Total Orang

Sistem akan menampilkan total jumlah orang dalam ruangan secara realtime.

## Fitur Sistem

* Realtime face detection
* Facial landmark detection
* Dua kamera realtime
* Penghitungan orang masuk
* Penghitungan orang keluar
* Monitoring jumlah orang realtime
* Bounding box wajah
* Computer vision realtime

## Teknologi yang Digunakan

* Python
* OpenCV
* dlib
* Facial Landmark Detection
* Haar Cascade
* Computer Vision

## Install Library

```bash id="6a5u5u"
pip install opencv-python
pip install dlib
pip install imutils
pip install numpy
pip install scipy
```

## Struktur Folder

```bash id="1ghm0l"
projectakhir/
│
├── main.py
├── shape_predictor_68_face_landmarks.dat
├── README.md
```

## Download Shape Predictor

Download file:

```text id="3tz2g0"
shape_predictor_68_face_landmarks.dat
```

Link download:

https://github.com/davisking/dlib-models

Simpan file tersebut di folder project.

## Cara Menjalankan Program

Masuk ke folder project:

```bash id="lsl7f3"
cd projectakhir
```

Jalankan program:

```bash id="zjlwmn"
py -3.10 main.py
```

## Cara Kerja Sistem

1. Kamera mengambil video realtime.
2. Sistem melakukan preprocessing citra.
3. Sistem mendeteksi wajah manusia.
4. Facial landmark digunakan untuk menentukan titik-titik penting wajah.
5. Kamera masuk menambah jumlah orang.
6. Kamera keluar mengurangi jumlah orang.
7. Sistem menampilkan total jumlah orang dalam ruangan secara realtime.

## Tampilan Sistem

Program akan menampilkan:

* Kamera masuk
* Kamera keluar
* Landmark wajah
* Bounding box wajah
* Status masuk dan keluar
* Total orang dalam ruangan

## Tombol Keluar

Tekan tombol:

```text id="ewh1bi"
ESC
```

untuk menghentikan program.

## Tujuan Project

Project ini dibuat untuk memenuhi tugas Project Akhir mata kuliah Pengolahan Citra Digital dengan implementasi metode Facial Landmark Detection pada sistem monitoring jumlah orang berbasis dua kamera realtime.

## Anggota Kelompok

* Azizan Rizqan Ramadhan
* Freshy Lugina Bella
* Dani Feriansyah

## Dosen Pengampu

Irma Amelia Dewi, S.Kom., M.T.

## Kampus

Institut Teknologi Nasional Bandung
Program Studi Informatika
