# Laporan Praktikum Kriptografi
Minggu ke-: 2
Topik: [kriptosistem]  
Nama: [Uswatun Khasanah]  
NIM: [230202782]  
Kelas: [5 IKKA]  

---

## 1. Tujuan
(Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).
Menggambarkan proses enkripsi dan dekripsi sederhana.
Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).
)


## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1:membayangkan komponen utama dalam sebuah kriptosistem.
- Pertanyaa 2: Apa kelebihan dan kelemahan sistem simetri dibandingkan asimetris?
- Pertanyaa 3:Mengapa distribusi kunci masalah menjadi utama dalam kriptografi simetri? 
 jawab
1.1. Komponen Utama dalam Kriptosistem
Sebuah kriptosistem umumnya terdiri dari beberapa komponen utama:
Plaintext (Teks Biasa):
Pesan asli yang ingin dikirim atau disimpan dengan aman.
Ciphertext (Teks Sandi):
Hasil dari proses enkripsi yang tidak bisa dibaca tanpa kunci.
Algoritma Enkripsi:
Prosedur atau rumus untuk mengubah plaintext menjadi ciphertext.
Algoritma Dekripsi:
Prosedur untuk mengembalikan ciphertext menjadi plaintext.
Kunci (Key):
Nilai rahasia yang digunakan dalam proses enkripsi dan dekripsi.

2. Aspek	Kriptografi Simetri	Kriptografi Asimetris
Jumlah Kunci 1 kunci (sama untuk enkripsi & dekripsi)	2 kunci (publik & privat)
Kecepatan	Cepat karena proses matematikanya sederhana	Lebih lambat karena komputasi lebih kompleks
Keamanan	Aman hanya jika kunci tidak bocor	Lebih aman untuk pertukaran kunci
Distribusi Kunci	Sulit — kunci harus dikirim secara rahasia	Mudah — kunci publik bisa disebarkan bebas
Contoh Algoritma	AES, DES, RC4	RSA, ECC, ElGamal

3. Karena pengirim dan penerima menggunakan kunci yang sama, maka:
Kunci harus dikirim secara aman sebelum komunikasi dimulai.
Jika kunci bocor di tengah jalan, pihak ketiga bisa mendekripsi semua pesan.
Semakin banyak pengguna, semakin rumit pengelolaan dan pengiriman kunci rahasia.
Contoh sederhana:
Jika 100 orang ingin berkomunikasi aman menggunakan kriptografi simetri, dibutuhkan 4.950 kunci berbeda agar tiap pasangan punya kunci unik — ini sulit dikelola.

Sistem simetri lebih cepat, tapi bermasalah dalam distribusi kunci.
Sistem asimetris lebih aman dalam distribusi kunci, tapi lebih lambat.
Dalam praktik modern, keduanya sering digabung:
→ asimetris untuk pertukaran kunci,
→ simetris untuk mengenkripsi data utama (contohnya pada protokol HTTPS).)

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
