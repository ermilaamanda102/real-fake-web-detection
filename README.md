# Real vs Fake Face Detection Web App

Aplikasi web untuk mendeteksi apakah sebuah gambar wajah merupakan **wajah asli (real)** atau **wajah hasil AI-generated (fake/deepfake)**, menggunakan model deep learning berbasis arsitektur **EfficientNetB0**.

## 📋 Deskripsi

Project ini merupakan sistem klasifikasi citra wajah untuk membedakan wajah asli dan wajah yang dihasilkan oleh AI (deepfake/GAN-generated). Model dilatih menggunakan transfer learning dengan EfficientNetB0 dan dideploy sebagai aplikasi web berbasis Flask.

## ✨ Fitur

- Upload gambar wajah melalui antarmuka web
- Klasifikasi otomatis: **Real** atau **Fake**
- Preprocessing gambar otomatis (resize, normalisasi)
- Hasil prediksi ditampilkan secara real-time

## 🛠️ Teknologi yang Digunakan

- **Backend**: Flask (Python)
- **Model**: TensorFlow/Keras — EfficientNetB0
- **Image Processing**: Pillow (PIL), NumPy
- **Frontend**: HTML, CSS, Jinja2 Templates

## 📁 Struktur Project

```
real-fake-web/
├── model/
│   └── realvsfake_effnetB0_final.h5
├── static/
│   └── uploads/
├── templates/
│   ├── about.html
│   ├── base.html
│   ├── demo.html
│   ├── home.html
│   ├── index.html
│   └── performance.html
├── app.py
├── requirements.txt
└── README.md
```

## 🚀 Cara Instalasi & Menjalankan

1. **Clone repository ini**
   ```bash
   git clone https://github.com/ermilaamanda102/real-fake-web-detection.git
   cd real-fake-web-detection
   ```

2. **Buat virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Aktifkan virtual environment**
   
   Windows (PowerShell):
   ```bash
   venv\Scripts\Activate.ps1
   ```
   
   Mac/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Jalankan aplikasi**
   ```bash
   python app.py
   ```

6. Buka browser dan akses `http://127.0.0.1:5000`

## 🖼️ Tampilan Aplikasi

### Halaman Home
![Halaman Home](screenshots/home.png)

### Halaman Demo / Deteksi
![Halaman Demo](screenshots/demo.png)

### Halaman Performance / Hasil Evaluasi Model
![Halaman Performance](screenshots/performance.png)

> Catatan: taruh file screenshot kamu di folder `screenshots/` dengan nama yang sesuai di atas, atau sesuaikan nama filenya di bagian ini.

## 📊 Performa Model

- Akurasi: **95.30%**
- AUC: **0.9902**
- F1-Score: **0.9530**
- Threshold klasifikasi: **0.62**

## 👤 Author

Dibuat oleh **Ermila Amanda** sebagai bagian dari tugas akhir/skripsi.

## 📄 Lisensi

Project ini dibuat untuk keperluan akademik.
