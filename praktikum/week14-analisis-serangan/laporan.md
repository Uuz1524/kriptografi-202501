# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: [Analisis Serangan Kriptografi]  
Nama: [Uswatun Khasanah]  
NIM: [230202782]  
Kelas: [5 IKKA]  

---

## 1. Tujuan
(Mengidentifikasi jenis serangan pada sistem informasi nyata.
Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.)

---

## 2. Dasar Teori
Identifikasi Serangan
(Pada tahun 2012, database LinkedIn bocor berisi sekitar 117 juta password pengguna.
Masalah utamanya: LinkedIn saat itu masih menggunakan hash MD5 tanpa salt.
MD5 adalah algoritma hash lama yang sangat cepat → cocok untuk penyerang melakukan brute force.
Serangannya Terjadi karena Hacker mendapatkan file database berisi hash MD5.
Karena:MD5 cepat dihitung Tidak memakai saltHacker menggunakan: Rainbow tableDictionary attackGPU untuk brute force
Dalam waktu singkat, jutaan password berhasil dikembalikan ke bentuk aslinya.
dampaknya:Akun LinkedIn diambil alih
Password yang sama dipakai di email, bank, media sosial → banyak akun lain ikut dibobol
Kerugian reputasi besar bagi LinkedIn

Evaluasi Kelemahan Sistem
Penggunaan algoritma hash yang sudah usang
LinkedIn masih menggunakan MD5, padahal saat itu MD5 sudah dikenal lemah dan mudah di-brute force menggunakan GPU.
Tidak menggunakan salt
Password yang sama menghasilkan hash yang sama. Ini memudahkan penyerang memakai rainbow table dan dictionary attack.
Kecepatan hash terlalu tinggiMD5 sangat cepat dihitung sehingga jutaan kombinasi password bisa dicoba hanya dalam hitungan detik.
Tidak ada perlindungan lanjutan setelah kebocoran
Sistem tidak mampu mendeteksi bahwa hash database telah bocor sebelum digunakan penyerang
Ketergantungan pada sistem lama (legacy system)
Tidak dilakukan migrasi cepat ke standar keamanan terbaru.
Kelemahan pada algoritma kriptografi
Ya, ada kelemahan.
LinkedIn menggunakan MD5, yaitu algoritma hash yang sudah terbukti tidak aman dan sangat cepat di-brute force.
Kelemahan pada implementasi
Ada juga Walaupun MD5 sudah lemah, kesalahan makin fatal karena:
Tidak menggunakan saltTidak memakai password hashing khusus seperti bcrypt atau Argon2Ini menunjukkan cara penerapan kriptografi sangat buruk.
Kelemahan pada konfigurasi sistem
Juga ada Sistem tidak memiliki:Deteksi kebocoran database Kebijakan keamanan seperti pemantauan akses mencurigakan dan perlindungan ekstra setelah insiden.

Jelaskan alasan pemilihan algoritma dan dampaknya terhadap keamanan sistem.
LinkedIn memilih MD5 karena:Cepat diproses → tidak membebani serverMudah diimplementasikanPopuler pada masanya → dulu dianggap cukup aman Cocok untuk sistem besar dengan jutaan penggunaNamun, seiring berkembangnya teknologi, alasan ini justru menjadi sumber kelemahan.

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
- Pertanyaan 1: Karena pada saat sistem itu dibuat, standar keamanannya masih rendah dibandingkan kondisi sekarang.
Penyebab utamanya: Penyebab	Penjelasan
Panjang password pendek	Dulu password 6–8 karakter sudah dianggap aman
Tidak ada pembatasan login	Bisa mencoba ribuan kali tanpa diblokir
Hash lama (MD5, SHA-1)	Hash ini cepat dihitung → mudah di-crack
Tidak menggunakan salt	Password sama menghasilkan hash sama
Perangkat lama	Server lama tidak mendukung algoritma modern
Akibatnya,
satu file database bocor saja bisa dipecahkan hanya dalam hitungan menit.
- Pertanyaan 2: Kelemahan algoritma terjadi jika algoritma kriptografinya sendiri sudah tidak aman. Walaupun dipakai dengan benar, tetap bisa dibobol. Contohnya MD5 atau DES. Solusinya: ganti algoritmanya.
Kelemahan implementasi terjadi jika algoritma sebenarnya aman, tetapi cara penggunaannya salah. Contohnya AES tapi password lemah, kunci disimpan di kode, atau tidak ada batas percobaan login. Solusinya: perbaiki cara penerapannya.
Pertanyaan 3: Selalu memperbarui algoritma dan standar keamanan
Gunakan algoritma yang masih direkomendasikan seperti AES-256, RSA minimal 2048 bit, atau ECC. Untuk password gunakan hashing modern seperti bcrypt, scrypt, atau Argon2.
Melakukan audit dan pengujian keamanan secara berkala
Sistem harus dicek rutin melalui penetration testing dan vulnerability scanning untuk menemukan celah sejak dini.
Mengamankan proses autentikasi pengguna
Terapkan password kuat, batasi percobaan login, dan aktifkan multi-factor authentication (MFA).
Melatih pengembang dan pengguna
Pengembang harus paham cara implementasi kriptografi yang benar, dan pengguna diedukasi agar tidak memakai password lemah.
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
Author: Uswatun Khasanah <Khasanah8952@gmail.com>
Date:   2026-09-1

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
