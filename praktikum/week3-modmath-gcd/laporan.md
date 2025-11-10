# Laporan Praktikum Kriptografi
Minggu ke-: 3
Topik: [Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit]  
Nama: [Uswatun Khasanah]  
NIM: [230202782]  
Kelas: [5 IKKA]  

---

## 1. Tujuan
(Menyelesaikan operasi aritmetika modular.
Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi)

---

## 2. Dasar Teori
(Aritmetika Modular (Modular Arithmetic)
Pengertian
Aritmetika modular adalah sistem operasi bilangan di mana kita hanya memperhatikan sisa hasil bagi terhadap suatu bilangan tetap yang disebut modulus.
Kita tulis:
a≡b(modn)
a≡b(modn)
yang berarti:
“a dan b memberikan sisa yang sama jika dibagi dengan n”,
atau secara matematis:
n∣(a−b)
n∣(a−b)
Contoh:
17≡5(mod12)
17≡5(mod12), karena 
17−5=12
17−5=12 adalah kelipatan dari 12.

23≡3(mod10)
23≡3(mod10), karena keduanya menyisakan 3 jika dibagi 10.
Operasi Dasar:
Jika 
a≡b(modn)
a≡b(modn) dan 
c≡d(modn)
c≡d(modn), maka:
Penjumlahan:
a+c≡b+d(modn)
a+c≡b+d(modn)
Pengurangan:
a−c≡b−d(modn)
a−c≡b−d(modn)
Perkalian:
a⋅c≡b⋅d(modn)
a⋅c≡b⋅d(modn)
Pangkat:
ak≡bk(modn)
a
k
≡b
k
(modn)
Contoh Perhitungan:

Hitung 
(7+9) mod 5
(7+9)mod5

7+9=16
7+9=16
16 mod 5=1
16mod5=1
Jadi: 
7+9≡1(mod5)
7+9≡1(mod5)
Aplikasi:
Digunakan dalam kriptografi (RSA, Diffie-Hellman)
Dalam jam (misal 15:00 + 10 jam = 1:00 → mod 12)
Dalam algoritma komputer dan hashing.  )




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
