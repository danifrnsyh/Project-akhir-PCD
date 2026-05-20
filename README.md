# Deteksi dan Penghitungan Orang Menggunakan Dua Kamera Realtime

Project akhir mata kuliah Pengolahan Citra Digital menggunakan Python dan OpenCV untuk mendeteksi dan menghitung jumlah orang secara realtime menggunakan dua kamera.

## Deskripsi Project

Sistem ini menggunakan dua kamera realtime yang ditempatkan pada:

* Pintu masuk
* Pintu keluar

Logika sistem:

* Jika kamera masuk mendeteksi wajah manusia maka jumlah orang dalam ruangan bertambah `+1`
* Jika kamera keluar mendeteksi wajah manusia maka jumlah orang dalam ruangan berkurang `-1`

Sistem akan menampilkan total jumlah orang dalam ruangan secara realtime.

## Fitur

* Realtime face detection
* Dua kamera realtime
* Penghitungan orang masuk
* Penghitungan orang keluar
* Monitoring jumlah orang dalam ruangan
* OpenCV face detection
* Python realtime processing

## Teknologi

* Python
* OpenCV
* Haar Cascade Classifier

## Install Library

```bash
py -3.10 -m pip install opencv-python
```

## Struktur Folder

```bash
projectakhir/
│
├── main.py
├── README.md
```

## Cara Menjalankan Program

Masuk ke folder project:

```bash
cd projectakhir
```

Jalankan program:

```bash
py -3.10 main.py
```

## Cara Kerja Sistem

### Kamera Masuk

Jika kamera masuk mendeteksi wajah manusia:

```text
Jumlah Orang +1
```

### Kamera Keluar

Jika kamera keluar mendeteksi wajah manusia:

```text
Jumlah Orang -1
```

### Total Orang

Sistem akan menampilkan total jumlah orang dalam ruangan secara realtime pada layar.

## Tampilan Sistem

Program akan menampilkan:

* Kamera masuk
* Kamera keluar
* Bounding box wajah
* Status masuk/keluar
* Total orang dalam ruangan

## Tombol Keluar

Tekan tombol:

```text
ESC
```

untuk menghentikan program.

## Tujuan Project

Project ini dibuat untuk memenuhi tugas Project Akhir mata kuliah Pengolahan Citra Digital dengan implementasi sistem monitoring realtime berbasis computer vision menggunakan dua kamera.

## Anggota Kelompok

* Azizan Rizqan Ramadhan
* Freshy Lugina Bella
* Dani Feriansyah

## Dosen Pengampu

Irma Amelia Dewi, S.Kom., M.T.

## Kampus

Institut Teknologi Nasional Bandung
Program Studi Informatika
