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
.)

---

## 2. Dasar Teori
(Enkripsi adalah proses mengubah pesan asli (disebut plaintext) menjadi pesan tersembunyi atau tidak terbaca (disebut ciphertext) agar hanya pihak yang berhak yang bisa memahaminya.
Bagaimana caranya?
Proses ini membutuhkan dua hal:
Algoritma enkripsi: Aturan atau metode matematis yang digunakan untuk mengacak data.
Contoh: AES (Advanced Encryption Standard), DES, atau bahkan sandi Caesar.
Kunci (key): Sebuah nilai rahasia (biasanya berupa angka atau string) yang digunakan dalam proses pengacakan.
Tanpa kunci yang tepat, sangat sulit (atau hampir mustahil) untuk mengembalikan ciphertext ke plaintext aslinya.
Ilustrasi Sederhana:
Misalnya, Anda punya pesan:
Plaintext: "HALO"
Gunakan algoritma Caesar cipher (menggeser huruf sebanyak 3 posisi) dengan kunci = 3.
Maka:
H → K
A → D
L → O
O → R
Hasilnya:
Ciphertext: "KDOR"
Hanya orang yang tahu algoritma (Caesar) dan kunci (3) yang bisa mengembalikannya ke "HALO".
Tujuan Enkripsi:
Menjaga kerahasiaan data.
Melindungi informasi saat dikirim melalui internet, disimpan di perangkat, atau dibagikan.
Mencegah pihak tidak sah membaca isi pesan.
Dekripsi: Ciphertext → [Algoritma + Kunci] → Plaintext
Apa itu?
Dekripsi adalah proses mengembalikan ciphertext (pesan terenkripsi) menjadi plaintext (pesan asli) yang bisa dibaca kembali. Ini adalah kebalikan dari enkripsi.
Bagaimana caranya?
Sama seperti enkripsi, dekripsi juga membutuhkan dua hal:
Algoritma dekripsi: Biasanya merupakan kebalikan (invers) dari algoritma enkripsi yang digunakan.
Kunci yang sama (dalam kriptografi simetris): Kunci yang digunakan saat enkripsi harus sama dengan kunci yang digunakan saat dekripsi.
Catatan: Ini berlaku untuk kriptografi simetris (seperti AES, DES). Pada kriptografi asimetris (seperti RSA), kunci enkripsi dan dekripsi berbeda (kunci publik vs kunci privat). 
Ilustrasi Sederhana (lanjutan dari contoh sebelumnya):
Anda menerima pesan terenkripsi:
Ciphertext: "KDOR"
Anda tahu
Algoritmanya: Caesar cipher
Kuncinya: 3 (artinya huruf digeser maju 3 saat enkripsi, jadi saat dekripsi harus digeser mundur 3)
Maka:
K → H
D → A
O → L
R → O
Hasilnya:
Plaintext: "HALO"
Pesan asli berhasil dipulihkan!
Tujuan Dekripsi:
Memungkinkan penerima yang sah membaca kembali informasi yang telah diamankan.
Menjamin bahwa hanya pihak yang memiliki kunci yang benar yang bisa memahami isi pesan.
Hubungan Antara Enkripsi dan Dekripsi
Keduanya adalah dua sisi dari sistem kriptografi simetris:
Enkripsi: melindungi data.
Dekripsi: mengakses data yang dilindungi.
.  )

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(<img width="1341" height="694" alt="asli week2" src="https://github.com/user-attachments/assets/691c5205-6e33-430e-8bee-96555ee707f9" />


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
