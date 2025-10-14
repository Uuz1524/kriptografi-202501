# Laporan Praktikum Kriptografi
Minggu ke-: 2
Topik: [kriptosistem]  
Nama: [Uswatun Khasanah]  
NIM: [230202782]  
Kelas: [5 IKKA]  

---

## 1. Tujuan
1.Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).
2.Menggambarkan proses enkripsi dan dekripsi sederhana.
3.Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).)

---

## 2. Dasar Teori
laintext adalah data/teks asli yang dapat dibaca manusia atau diproses oleh sistem sebelum dilakukan enkripsi. Plaintext adalah input pada proses kriptografi — bentuk yang bermakna, seperti pesan, dokumen, password, file, atau payload jaringan.  )
Karakteristik Plaintext
Mudah dibaca / bermakna — manusia atau aplikasi bisa mengerti isinya tanpa proses dekripsi.
Bervariasi formatnya — bisa teks ASCII/UTF-8, data terstruktur (XML/JSON), atau data biner.
Sifatnya sensitif — sering mengandung informasi pribadi/rahasia (password, data kartu, pesan).
Rentan bila tersimpan/ditransmisikan tanpa proteksi — dapat bocor, dimodifikasi, atau disalahgunakan.
Peran Plaintext dalam Kriptosistem
Input enkripsi: Plaintext + Kunci + Algoritma → Ciphertext.
Output dekripsi: Ciphertext + Kunci + Algoritma → Plaintext (kembali ke bentuk semula).
Basis analisis serangan: serangan seperti known-plaintext menggunakan pasangan plaintext–ciphertext untuk memecah algoritma/kunci.

Apa itu Ciphertext?
Ciphertext adalah keluaran dari proses enkripsi—bentuk data yang sudah diubah sedemikian rupa sehingga tidak bermakna (tidak bisa dibaca) tanpa kunci yang sesuai. Jika plaintext adalah pesan asli, maka ciphertext adalah versi terenkripsi yang aman untuk disimpan atau dikirim.

Karakteristik Ciphertext
Tidak dapat dibaca secara langsung — hanya pihak yang memiliki kunci yang dapat mengembalikannya ke plaintext.
Tampak acak (pada cipher kuat): tidak memperlihatkan pola plaintext.
Tergantung pada kunci dan parameter (mis. IV/nonce, mode operasi). Mengubah kunci atau IV menghasilkan ciphertext berbeda.
Bisa berisi metadata seperti IV atau tag autentikasi yang diperlukan untuk dekripsi dan verifikasi.

Peran Ciphertext dalam Kriptosistem
Menjaga kerahasiaan data ketika disimpan (at rest) atau dikirim (in transit).
Menjadi objek serangan: model serangan berbeda berdasarkan apa yang penyerang lihat (hanya ciphertext = ciphertext-only attack; pasangan plaintext–ciphertext = known-plaintextKunci adalah nilai rahasia yang digunakan dalam proses enkripsi dan dekripsi. Kunci menentukan bagaimana algoritma bekerja terhadap plaintext untuk menghasilkan ciphertext, dan sebaliknya.

Fungsi Kunci
Mengontrol enkripsi dan dekripsi → tanpa kunci yang benar, ciphertext tidak bisa dikembalikan ke plaintext.
Membedakan hasil enkripsi → plaintext sama akan menghasilkan ciphertext berbeda bila kuncinya berbeda.
Menjadi inti keamanan kriptosistem → algoritma biasanya terbuka (security by design), tapi kunci harus dirahasiakan.

Jenis Kunci
Kunci Simetris
Sama untuk enkripsi dan dekripsi.
Contoh: AES, DES.
Tantangan: distribusi kunci (harus dikirim aman ke penerima).
Kunci Asimetris (Public & Private Key)
Sepasang kunci berbeda:
Public key → bisa dibagikan, untuk enkripsi/verifikasi.
Private key → rahasia, untuk dekripsi/penandatanganan.
Contoh: RSA, ECC.
Lebih aman dalam distribusi kunci, tapi lebih lambat., dsb.).
Menyertakan proteksi integritas bila menggunakan algoritma AEAD (Authenticated Encryption with Associated Data), sehingga selain rahasia juga terjamin tidak berubah.

Algoritma adalah prosedur matematika/logika yang digunakan untuk mengubah plaintext menjadi ciphertext (enkripsi), dan ciphertext menjadi plaintext (dekripsi).
Fungsi Algoritma
Menentukan cara kerja proses enkripsi/dekripsi.
Bekerja sama dengan kunci untuk menjamin keamanan data.
Harus terbuka dan standar (agar bisa diuji keamanannya), sedangkan kuncinya tetap rahasia.

Algoritma Simetris

👉 Ciri utama: kunci yang digunakan untuk enkripsi = kunci untuk dekripsi.

Kelebihan: cepat, cocok untuk enkripsi data dalam jumlah besar (misalnya file, database, komunikasi real-time).

Kekurangan: masalah distribusi kunci (bagaimana mengirimkan kunci ke pihak lain dengan aman).

a) Block Cipher
Data diproses dalam blok-blok tetap (contoh: 64-bit, 128-bit).
Jika data tidak cukup panjang, akan ditambahkan padding.
Bisa digunakan dengan berbagai mode operasi (ECB, CBC, CTR, GCM).
Contoh algoritma:
AES (Advanced Encryption Standard): blok 128-bit, sangat aman, standar global.
DES (Data Encryption Standard): blok 64-bit, kini dianggap tidak aman karena kunci pendek (56-bit).
Blowfish: blok 64-bit, cepat, kunci hingga 448-bit.

Stream Cipher
Mengenkripsi bit per bit atau byte per byte secara berurutan.
Menggunakan keystream generator (aliran bit acak) yang digabungkan dengan plaintext.
Cocok untuk komunikasi real-time (misalnya VoIP, streaming).
Contoh algoritma:
RC4: dulunya populer (misalnya di WEP/WPA), sekarang dianggap lemah.
ChaCha20: modern, cepat, aman, digunakan pada protokol TLS (misalnya HTTPS).

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
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

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
