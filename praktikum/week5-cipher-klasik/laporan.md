# Laporan Praktikum Kriptografi
Minggu ke-: 5
Topik: [Cipher Klasik (Caesar, Vigenère, Transposisi]  
Nama: [uswatun khasanah]  
NIM: [230202782]  
Kelas: [5 IKKA]  

---

## 1. Tujuan
(Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
Mengimplementasikan algoritma transposisi sederhana.
Menjelaskan kelemahan algoritma kriptografi klasik)

---

## 2. Dasar Teori
(Cipher Caesar adalah metode substitusi paling sederhana, di mana setiap huruf dalam plaintext digeser sejumlah tetap (biasanya 3) dalam alfabet (misalnya, A → D, B → E, dst.). Kuncinya hanya berupa satu angka (0–25), sehingga hanya ada 26 kemungkinan kunci. Kelemahannya sangat mendasar: rentan terhadap brute-force (coba semua 26 pergeseran) dan analisis frekuensi, karena pola distribusi huruf dalam bahasa asli tetap terjaga. 
Cipher Vigenère merupakan penyempurnaan Caesar dengan menggunakan kata kunci (misalnya "KEY") yang diulang sepanjang plaintext, lalu setiap huruf plaintext digeser berdasarkan huruf kunci yang sesuai (A=0, B=1, ..., Z=25). Ini menghilangkan pola frekuensi tunggal (karena satu huruf bisa dienkripsi menjadi banyak simbol), sehingga lebih tahan terhadap analisis frekuensi sederhana. Namun, jika panjang kunci diketahui (misalnya via Kasiski examination atau index of coincidence), cipher ini dapat dipecahkan menjadi beberapa sandi Caesar terpisah — menjadikannya aman hanya jika kuncinya sama panjang dengan pesan dan benar-benar acak (yaitu one-time pad). 
Cipher Transposisi tidak mengganti huruf, tetapi mengacak posisi huruf-huruf dalam pesan sesuai pola tertentu (misalnya: tulis plaintext dalam baris, lalu baca per kolom; atau balik urutan, zig-zag, dll.). Contoh klasik adalah rail fence cipher. Kelemahannya: meskipun frekuensi huruf tetap tidak berubah (membuat analisis frekuensi tidak langsung efektif), struktur linguistik (seperti kata pendek, pola spasi, atau n-gram umum) tetap terlihat, sehingga pesan bisa dikenali atau direkonstruksi dengan teknik seperti anagramming atau pencarian pola jarak.   
Secara umum, ketiga cipher ini tidak aman untuk penggunaan modern karena ruang kunci kecil dan struktur deterministik, namun tetap penting untuk memahami prinsip dasar confusion (substitusi) dan diffusion (transposisi) yang menjadi landasan desain cipher modern seperti AES).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  

Cipher klasik seperti Caesar, Vigenère, dan Transposisi merupakan metode enkripsi awal yang mengandalkan manipulasi sederhana terhadap teks, baik melalui substitusi maupun pengacakan posisi huruf. Caesar menggunakan pergeseran tetap (misalnya +3) untuk setiap huruf, sehingga sangat rentan terhadap serangan brute-force (hanya 25 kemungkinan kunci) dan analisis frekuensi. Vigenère memperbaiki kelemahan ini dengan menggunakan kunci berulang berupa kata, sehingga satu huruf bisa dienkripsi menjadi berbagai simbol—mengaburkan frekuensi tunggal. Namun, jika panjang kunci berhasil diungkap (misalnya lewat metode Kasiski), cipher ini kembali bisa dipecahkan sebagai kumpulan sandi Caesar terpisah. 
Sementara itu, cipher Transposisi tidak mengubah huruf itu sendiri, melainkan mengubah urutannya sesuai pola tertentu (misalnya menulis per baris lalu membaca per kolom). Meskipun frekuensi huruf tetap utuh (tidak membocorkan identitas huruf), pola linguistik—seperti kemunculan bigram umum ("th", "er") atau struktur kata—masih terlihat, memungkinkan rekonstruksi melalui anagramming atau pencarian pola spasial. Ketiganya tidak lagi memadai untuk keamanan modern karena ruang kunci kecil, ketergantungan pada kunci pendek, dan kerentanan terhadap serangan statistik, namun tetap bernilai edukatif sebagai dasar konsep substitusi (confusion) dan transposisi (diffusion) yang dikembangkan lebih lanjut dalam algoritma kriptografi modern seperti AES

Cipher klasik adalah metode enkripsi manual atau mekanis yang dikembangkan sebelum era komputer, yang umumnya mengandalkan teknik sederhana seperti substitusi (mengganti huruf dengan huruf/simbol lain) atau transposisi (mengubah urutan huruf) untuk menyembunyikan makna pesan. Contohnya meliputi Caesar cipher (substitusi dengan pergeseran tetap), Vigenère cipher (substitusi polialfabetik menggunakan kunci berulang), dan transposition cipher (pengacakan posisi huruf tanpa mengubah identitasnya). Cipher ini dirancang untuk dioperasikan secara manual dengan pena-kertas atau alat mekanis sederhana, dan umumnya memiliki ruang kunci kecil serta struktur deterministik, sehingga rentan terhadap serangan statistik seperti analisis frekuensi atau brute-force—meskipun historis penting sebagai fondasi prinsip kriptografi modern.
Konsep dasar cipher klasik berpusat pada dua prinsip utama: substitusi dan transposisi.   
Substitusi berarti mengganti setiap huruf (atau kelompok huruf) dalam plaintext dengan huruf atau simbol lain berdasarkan aturan tertentu. Contohnya, pada Caesar cipher, setiap huruf digeser sejumlah tetap dalam alfabet; pada Vigenère cipher, pergeseran bervariasi sesuai huruf kunci, menciptakan substitusi polialfabetik yang lebih kuat. Tujuannya adalah menciptakan confusion—mengaburkan hubungan antara plaintext, ciphertext, dan kunci. 
Transposisi tidak mengubah huruf itu sendiri, tetapi mengacak urutannya sesuai pola tertentu (misalnya menulis plaintext dalam matriks lalu membacanya kolom per kolom). Ini menghasilkan diffusion, yaitu penyebaran pengaruh satu huruf plaintext ke banyak posisi di ciphertext, sehingga struktur linguistik (seperti kata umum atau pola kalimat) menjadi sulit dikenali. 
     )

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
- Pertanyaan 1: Kelemahan utama Caesar Cipher adalah ruang kuncinya sangat kecil — hanya 25 kemungkinan pergeseran (untuk alfabet 26 huruf) — sehingga sangat rentan terhadap serangan brute-force: cukup mencoba semua pergeseran hingga ditemukan plaintext yang bermakna. Selain itu, karena menggunakan substitusi monoalfabetik (satu huruf selalu menjadi huruf yang sama), distribusi frekuensi huruf dalam ciphertext tetap mencerminkan bahasa asli, memungkinkan analisis frekuensi (misalnya, huruf terbanyak kemungkinan besar adalah 'E' dalam Bahasa Inggris) untuk memecahkan kunci dengan cepat tanpa perlu mencoba semua kemungkinan. 
Sementara itu, Vigenère Cipher, meskipun lebih kuat karena menggunakan substitusi polialfabetik (satu huruf bisa menjadi banyak simbol), tetap memiliki kelemahan struktural: kuncinya bersifat periodik (diulang). Jika panjang kunci berhasil diungkap — misalnya melalui metode Kasiski examination (mencari jarak antar repetisi substring) atau index of coincidence — maka ciphertext dapat dibagi menjadi sebanyak m  (panjang kunci) alur, masing-masing berperilaku seperti sandi Caesar terpisah. Setelah itu, analisis frekuensi dapat diterapkan pada tiap alur secara independen, sehingga cipher ini bisa dipecahkan secara sistematis. Tanpa kunci yang acak dan sepanjang pesan (seperti pada one-time pad), Vigenère tetap tidak aman terhadap serangan kriptanalisis klasik

- Pertanyaan 2: Cipher klasik seperti Caesar dan transposisi (serta Vigenère dengan kunci pendek) mudah diserang dengan analisis frekuensi karena mereka tidak menyembunyikan pola statistik bahasa asli, terutama distribusi kemunculan huruf. Dalam bahasa alami (misalnya Bahasa Indonesia atau Inggris), beberapa huruf jauh lebih sering muncul daripada yang lain — contohnya, dalam Bahasa Inggris, 'E', 'T', 'A' adalah huruf paling umum, sedangkan 'Q', 'Z', 'X' jarang muncul. Pada Caesar cipher (substitusi monoalfabetik), setiap huruf selalu dipetakan ke huruf tetap yang sama, sehingga frekuensi relatif tetap utuh — hanya “digeser”. Dengan memetakan huruf terbanyak di ciphertext ke 'E' (atau huruf dominan dalam bahasa sasaran), kunci bisa langsung ditebak.   

Pada cipher transposisi, huruf tidak diganti sama sekali — hanya posisinya yang diacak — sehingga distribusi frekuensi persis sama dengan plaintext. Ini memungkinkan penyerang mengenali bahasa dan bahkan menebak isi pesan dari pola frekuensi saja. Bahkan Vigenère cipher, yang awalnya dianggap “tak terpecahkan”, rentan jika kuncinya pendek: periodisitas kunci menyebabkan huruf yang sama dalam plaintext kadang dienkripsi ke simbol berbeda, tapi dalam satu posisi siklus kunci, tetap terjadi substitusi monoalfabetik sehingga setelah panjang kunci diketahui, analisis frekuensi bisa diterapkan per sub-cipher. 
- pertanyaan 3: 
Cipher substitusi (seperti Caesar atau Vigenère) memiliki kelebihan dalam menyembunyikan identitas huruf asli, sehingga distribusi frekuensi tampak berubah — terutama pada substitusi polialfabetik (Vigenère), yang lebih tahan terhadap analisis frekuensi sederhana. Namun, kelemahannya terletak pada monoalfabetik yang kaku: pada substitusi sederhana, satu huruf selalu menjadi huruf yang sama, sehingga pola frekuensi tetap utuh dan mudah dianalisis; bahkan pada Vigenère, periodisitas kunci membuka celah bagi serangan Kasiski atau indeks koincidensi. 
Sebaliknya, cipher transposisi (seperti rail fence atau columnar transposition) unggul dalam mempertahankan integritas karakter (tidak ada distorsi simbol), sehingga cocok untuk data yang sensitif terhadap perubahan nilai (misalnya angka atau kode biner jika diadaptasi), dan lebih efektif dalam menciptakan diffusion — pengacakan posisi menyulitkan pengenalan pola kata atau frasa. Namun, kelemahan utamanya adalah frekuensi huruf tetap persis seperti aslinya, sehingga penyerang mudah mengenali bahasa dan menggunakan teknik seperti anagramming atau analisis bigram/trigram untuk merekonstruksi pesan. Secara umum, keduanya lemah jika digunakan sendiri, tetapi kombinasi keduanya (substitusi + transposisi) seperti pada mesin Enigma atau desain modern AES — jauh lebih kuat karena menciptakan confusion sekaligus diffusion. )
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

Author: uswatun khasanah <khasanah8952@gmail.com>
Date:   2025-11-16
week5-cipher-klasik: Cipher Klasik (Caesar, Vigenère, Transposisi )
```
