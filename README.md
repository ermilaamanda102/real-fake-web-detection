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