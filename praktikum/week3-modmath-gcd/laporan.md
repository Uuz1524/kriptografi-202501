# Laporan Praktikum Kriptografi
Minggu ke-: 3
Topik: [Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit]  
Nama: [Uswatun Khasanah]  
NIM: [230202782]  
Kelas: [5 IKKA]  

---

## 1. Tujuan
(Menyelesaikan operasi aritmetika modular.
Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor)
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
- Pertanyaan 1:ran Aritmetika Modular dalam Kriptografi Modern 
Aritmetika modular adalah operasi aritmetika (penjumlahan, perkalian, eksponensiasi, dll.) yang dilakukan dalam himpunan bilangan bulat modulo n , yaitu himpunan Zn​={0,1,2,...,n−1}  dengan operasi dilakukan "dalam siklus" sebesar n . 
Mengapa penting dalam kriptografi? 
Sifat satu arah (one-way function): Operasi seperti eksponensiasi modular (c=memodn ) mudah dihitung, tetapi membalikkannya (mencari m  dari c  tanpa mengetahui kunci privat) sangat sulit — inilah dasar keamanan RSA.
Struktur grup siklik: Grup multiplikatif Zp∗​  (untuk p  prima) atau Zn∗​  (untuk n=pq ) memiliki struktur matematis yang cocok untuk membangun fungsi trapdoor dan protokol pertukaran kunci (misalnya Diffie-Hellman).
Keterbatasan ruang: Ruang output terbatas (0 sampai n−1 ), memungkinkan representasi data dalam bentuk yang efisien dan konsisten untuk enkripsi/dekripsi.
Kompatibilitas dengan teorema bilangan: Teorema seperti Fermat’s Little Theorem, Euler’s Theorem, dan Chinese Remainder Theorem (CRT) memberi dasar untuk efisiensi dan keamanan.
     
- Pertanyaan 2:2. Mengapa Invers Modular Penting dalam Algoritma Kunci Publik (misalnya RSA)? 
Invers modular dari a  modulo n  adalah bilangan a−1  sehingga: 
a⋅a−1≡1(modn) 
Dalam RSA: 
Kunci publik: (e,n) , dengan e  dipilih relatif prima terhadap ϕ(n)=(p−1)(q−1) 
Kunci privat: d , yang merupakan invers modular dari e  modulo ϕ(n) , yaitu:  
d≡e−1(modϕ(n))ataue⋅d≡1(modϕ(n)) 
Saat dekripsi:  
cd≡(me)d=med≡m1+kϕ(n)≡m⋅(mϕ(n))k≡m⋅1k=m(modn) 
(berlaku jika gcd(m,n)=1 , dan dapat diperluas ke semua m  via CRT.) 
Tanpa invers modular, tidak mungkin membangun kunci dekripsi d , sehingga RSA tidak akan berfungsi. Invers modular juga digunakan dalam: 
Penandatanganan digital (DSA, ECDSA)
Protokol zero-knowledge
Skema enkripsi berbasis kurva eliptik (modular inverse dalam field hingga
Invers modular dihitung efisien dengan Extended Euclidean Algorithm, asalkan gcd(a,n)=1 .

Pertanyaan 3:Tantangan Utama dalam Menyelesaikan Logaritma Diskrit untuk Modulus Besar 
Masalah logaritma diskrit (DLP — Discrete Logarithm Problem): 
Diberikan grup siklik G , generator g∈G , dan elemen h=gx∈G , temukan x∈Z . 
Dalam konteks modular: untuk modulus prima p , cari x  sehingga: 
gx≡h(modp) 
Tantangan utama: 
Kompleksitas eksponensial
Tidak ada algoritma klasik yang diketahui dapat memecahkan DLP dalam waktu polinomial untuk grup umum. Algoritma terbaik (e.g.,
Number Field Sieve
untuk Zp∗​ ) masih memiliki kompleksitas sub-eksponensial: exp(O((logp)1/3(loglogp)2/3)) . Untuk modulus 2048-bit, ini tetap tidak praktis.
Tidak ada struktur linear
Tidak seperti logaritma real, tidak ada sifat kontinuitas atau kalkulus yang bisa dimanfaatkan — semua operasi diskret dan diskontinu.
Ketergantungan pada struktur grup
Efisiensi serangan sangat bergantung pada pilihan grup:\
• Zp∗​ : rentan terhadap NFS jika p tidak dipilih hati-hati.\
• Kurva eliptik (ECC): DLP jauh lebih sulit (tidak ada algoritma sub-eksponensial umum), sehingga kunci 256-bit ECC setara dengan 3072-bit RSA.
Quantum threat
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
Author: uswatun khasanah <khasanah8952@gamil.com>
Date:   2025-11-15

    week3-modmath: Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit )
```
