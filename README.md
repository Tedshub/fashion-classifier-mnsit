
# Fashion‑Classifier‑MNIST 👗🧠

Fashion‑Classifier‑MNIST adalah proyek machine learning yang membangun model klasifikasi gambar menggunakan dataset Fashion-MNIST. Proyek ini memanfaatkan TensorFlow untuk membedakan 10 kategori pakaian berbasis gambar 28×28 piksel dalam skala abu-abu.

---

## 🎯 Fitur Utama
- Training model deep learning (Fully Connected) untuk klasifikasi gambar fashion.
- Evaluasi akurasi dan visualisasi performa training.
- Struktur proyek bersih dan modular.
- Dependensi dikelola menggunakan `requirements.txt`.

---

## 💾 Dataset
Fashion‑MNIST adalah versi kompleks dari dataset MNIST yang berisi:
- **60.000** gambar untuk pelatihan.
- **10.000** gambar untuk pengujian.
- 10 Kelas:  
  `T‑shirt/top`, `Trouser`, `Pullover`, `Dress`, `Coat`, `Sandal`, `Shirt`, `Sneaker`, `Bag`, `Ankle boot`.

---

## 🛠️ Instalasi

1. Clone repository:
   ```bash
   git clone https://github.com/Tedshub/fashion-classifier-mnsit.git
   cd fashion-classifier-mnsit
   ```

2. Buat virtual environment:
   ```bash
   python -m venv venv
   ```

3. Aktifkan environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Cara Menjalankan

Jalankan script utama:
```bash
python model_fashion_mnsit.py
```

Output:
- Progres training per epoch
- Akurasi model pada data test
- Visualisasi loss & akurasi (jika ditambahkan)

---

## 📁 Struktur Proyek

```
fashion-classifier-mnsit/
├── model_fashion_mnsit.py     # Script utama klasifikasi
├── requirements.txt           # Daftar library yang dibutuhkan
├── .gitignore                 # Mengecualikan folder dan file besar
└── README.md                  # Dokumentasi proyek
```

---

## 📈 Hasil & Performa

Model sederhana dengan layer fully-connected dapat menghasilkan akurasi:
- ±85–90% tanpa tuning lanjut

Untuk akurasi lebih tinggi:
- Gunakan CNN (Conv2D, MaxPooling)
- Lakukan augmentasi data
- Eksperimen hyperparameter (epoch, batch size, learning rate)

---

## 🔧 Pengembangan Selanjutnya
- Migrasi ke model CNN
- Tambahkan validasi data dan visualisasi prediksi
- Export model ke format `.h5` atau `.tflite` untuk deployment

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

---

## 🙋 Kontak

- GitHub: [@Tedshub](https://github.com/Tedshub)
- Email: *(tambahkan jika ingin mencantumkan)*

---

Selamat belajar dan bereksperimen dengan deep learning di dunia fashion! ✨
