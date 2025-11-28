# Laporan Praktikum Kriptografi
Minggu ke-: 6 
Topik: [Cipher Modern (DES, AES, RSA)]  
Nama: [Uswatun Khasanah]  
NIM: [230202782]  
Kelas: [5IKKA]  

---

## 1. Tujuan
(Mengimplementasikan algoritma DES untuk blok data sederhana.
Menerapkan algoritma AES dengan panjang kunci 128 bit.
Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.
)

---

## 2. Dasar Teori
1. (DES (Data Encryption Standard)
   Konsep Dasar
DES adalah algoritma enkripsi blok simetris yang bekerja pada blok data berukuran 64 bit dengan kunci 56 bit.
Artinya: data diubah menjadi blok-blok 64 bit, dan tiap blok dienkripsi menggunakan kunci yang sama untuk pengirim dan penerima.
Struktur Internal DES
DES menggunakan arsitektur Feistel Network, di mana proses enkripsi dan dekripsi memiliki struktur yang sama (hanya urutan subkey-nya dibalik).
Langkah-langkah DES:
Initial Permutation (IP):
64-bit plaintext diacak sesuai tabel permutasi tertentu.
16 Feistel Rounds:
Setiap putaran terdiri dari:
Pembagian data menjadi Left (L) dan Right (R).
Fungsi F(R, K):
R diperluas menjadi 48 bit.
Di-XOR dengan subkey 48 bit.
Masuk ke S-Box (Substitution Box) → mengubah 48 bit menjadi 32 bit.
Dilakukan permutasi (P) untuk menyebarkan bit.
Nilai hasil di-XOR dengan bagian kiri (L).
Final Permutation (IP⁻¹):
Setelah 16 round, bagian kiri dan kanan di
gabung kembali dan dipermutasi ulang.
Pembangkitan Subkey
Kunci utama 56 bit diproses menjadi 16 subkey, masing-masing 48 bit, untuk setiap round.
Kelebihan & Kekurangan
Kelebihan
Struktur sederhana, mudah dipahami
Cepat di perangkat keras
Menjadi dasar banyak algoritma lain
Kekurangan
Panjang kunci terlalu pendek (56-b
Rentan brute-force (dapat dipecahkan dalam hitungan jam dengan superkomputer)
Tidak cocok untuk keamanan modern
penerapan
Dulu digunakan pada ATM, sistem telekomunikasi, dan enkripsi file pemerintah AS, tapi kini digantikan oleh AES dan Triple-DES (3DES).


2. AES (Advanced Encryption Standard)
Konsep Dasar
AES adalah cipher blok simetris modern dengan panjang blok tetap 128 bit dan panjang kunci 128, 192, atau 256 bit.
AES menggantikan DES sebagai standar enkripsi pada tahun 2001 setelah kompetisi internasional oleh NIST.
Struktur Internal AES
AES bukan jaringan Feistel, tapi menggunakan struktur Substitution–Permutation Network (SPN).
Proses enkripsi:
Key Expansion:
Kunci utama diperluas menjadi beberapa round key.
Initial Round:
Tambahkan kunci awal ke blok data (AddRoundKey).
Main Rounds (10, 12, atau 14):
Tiap round berisi langkah:
SubBytes: Tiap byte diubah menggunakan tabel substitusi (S-box).
ShiftRows: Baris matriks digeser berbeda jumlah langkah.
MixColumns: Kolom dicampur menggunakan operasi aljabar modulo.
AddRoundKey: Setiap byte di-XOR dengan bagian dari kunci round.
Final Round:
Sama dengan main round tapi tanpa MixColumns.
Dekripsi AES menggunakan operasi kebalikan dari langkah di atas.
Keunggulan
Keamanan tinggi: belum ada serangan praktis yang memecahkan AES.
Cepat di perangkat keras dan perangkat lunak.
Fleksibel: mendukung panjang kunci berbeda.
Tersertifikasi NIST dan digunakan global.
Kelemahan
Karena sangat kuat, kadang terlalu “berat” untuk perangkat kecil jika menggunakan AES-256.
Enkripsi simetris → memerlukan cara aman untuk berbagi kunci.
Penerapan Nyata
Wi-Fi Security (WPA2/WPA3)
VPN (IPsec, OpenVPN)
File Encryption (WinRAR, 7zip, BitLocker)
Komunikasi aman (HTTPS, TLS)

3.RSA (Rivest–Shamir–Adleman)
Konsep Dasar
RSA adalah cipher asimetris → menggunakan dua kunci berbeda:
Kunci publik (public key) untuk enkripsi.
Kunci privat (private key) untuk dekripsi.
Berdasarkan matematika bilangan prima besar dan faktorisasi.
Dasar Matematika
Pilih dua bilangan prima besar: p dan q.
Hitung:
n = p × q (modulus)
φ(n) = (p−1)(q−1)
Pilih e (kunci publik) yang relatif prima terhadap φ(n).
Hitung d (kunci privat) sebagai kebalikan dari e modulo φ(n):
d × e ≡ 1 (mod φ(n))
Proses
Enkripsi:
Ciphertext = Mᵉ mod n
Dekripsi:
Plaintext = Cᵈ mod n
Kelebihan

Aman, karena berbasis teori bilangan
Tidak perlu berbagi kunci rahasia	
Cocok untuk digital signature dan SSL
Kekurangan
Lebih lambat dibanding AES
Enkripsi/dekripsi besar butuh komputasi tinggi
Kurang efisien untuk data besar

Penerapan
Keamanan website (HTTPS / SSL Certificates)
Tanda tangan digital
Autentikasi email (PGP, GPG)
Pengiriman kunci simetris (misalnya AES)

Hubungan Antara Ketiganya
Dalam sistem keamanan modern (misalnya HTTPS):
RSA digunakan untuk mengamankan pertukaran kunci AES.
Setelah kunci rahasia AES diterima, AES digunakan untuk enkripsi data aktual karena cepat.
DES sudah jarang dipakai, tapi penting dalam sejarah kriptografi modern.


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
- Pertanyaan 1:
| Aspek                 | **DES**                                  | **AES**                                          | **RSA**                                           |

| **Jenis Cipher**      | Simetris                                 | Simetris                                         | Asimetris        |
| **Jumlah Kunci**      | 1 kunci (sama untuk enkripsi & dekripsi) | 1 kunci (sama untuk enkripsi & dekripsi)         | 2 kunci (publik & privat)                         |
| **Panjang Kunci**     | 56 bit                                   | 128, 192, atau 256 bit                           | 1024 – 4096 bit  |
| **Struktur Internal** | Feistel Network (16 putaran)             | Substitution–Permutation Network (10–14 putaran) | Operasi matematika pada bilangan prima besar      |
| **Keamanan**          | Lemah (mudah brute-force)                | Sangat kuat (belum pernah dipecahkan)            | Sangat kuat (berbasis faktorisasi bilangan prima) |
| **Kecepatan**         | Cepat (tapi tidak aman)                  | Sangat cepat dan aman                            | Lambat (karena operasi matematika besar)          |
| **Penggunaan Umum**   | Sistem lama, 3DES                        | Enkripsi data modern (Wi-Fi, VPN, TLS)           | Enkripsi kunci & tanda tangan digital             |

 Kesimpulan singkat:
DES dan AES menggunakan satu kunci yang sama (simetris).
RSA menggunakan dua kunci berbeda (asimetris).
AES mengalahkan DES karena panjang kuncinya jauh lebih besar dan aman dari brute-force.
RSA lebih cocok untuk pertukaran kunci atau autentikasi, bukan untuk enkripsi data besar karena lebih lambat.
- Pertanyaan 2: …  
Mengapa AES Lebih Banyak Digunakan Dibanding DES di Era Modern
Ada beberapa alasan kuat mengapa AES menggantikan DES:
a. Panjang Kunci
DES hanya menggunakan 56-bit key, yang berarti hanya ada 
2
56
2
56
 kemungkinan kunci (sekitar 72 triliun).
Superkomputer modern bisa mencoba seluruh kombinasi itu dalam beberapa jam saja.
AES memiliki 128–256 bit key, yang berarti 
2
128
2
128
 atau lebih kombinasi — tidak mungkin dipecahkan dengan brute-force bahkan oleh semua komputer di dunia sekalipun.
b. Kecepatan dan Efisiensi
AES lebih efisien di software dan hardware modern.
Algoritma AES dioptimalkan untuk prosesor modern dan mendukung parallel processing, sedangkan DES tidak.
c. Keamanan Struktur
AES menggunakan Substitution–Permutation Network (SPN), bukan Feistel seperti DES.
SPN lebih kuat terhadap berbagai serangan modern seperti differential cryptanalysis dan linear cryptanalysis.
d. Standar Global
AES ditetapkan sebagai standar resmi NIST (FIPS-197) sejak 2001.
Saat ini digunakan di WPA2/WPA3, HTTPS, VPN, BitLocker, SSH, OpenSSL, dan banyak sistem keamanan lainnya.
Kesimpulan:
AES lebih cepat, lebih aman, dan dirancang khusus untuk kebutuhan keamanan masa kini.
DES dianggap tidak aman lagi sejak akhir 1990-an.

Pertanyaan 3
Mengapa RSA Dikatakan Asimetris dan Bagaimana Proses Pembangkitan Kuncinya
a. Mengapa RSA Disebut Asimetris
RSA disebut algoritma asimetris karena:
Kunci untuk enkripsi dan dekripsi berbeda.
Kunci publik digunakan oleh siapa pun untuk mengenkripsi pesan.
Kunci privat hanya dimiliki penerima untuk mendekripsi pesan.
Dengan kata lain:
Public Key ≠ Private Key, tetapi keduanya saling berkaitan secara matematis.
Berbeda dengan DES/AES (simetris) yang menggunakan satu kunci sama, RSA memisahkan peran kedua kunci tersebut untuk keamanan lebih tinggi.
b. Proses Pembangkitan Kunci RSA
Langkah-langkahnya:
Pilih dua bilangan prima besar:
𝑝
dan 
𝑞
p dan q
Contoh sederhana: p = 17, q = 11.
Hitung hasil kali keduanya (modulus):
𝑛
=
𝑝
×
𝑞
n=p×q

(n digunakan dalam kunci publik & privat)
Hitung fungsi totien Euler:
𝜑
(
𝑛
)
=
(
𝑝
−
1
)
(
𝑞
−
1
)
φ(n)=(p−1)(q−1)
Pilih bilangan bulat e (public exponent):
e harus relatif prima terhadap φ(n).
Biasanya dipilih e = 65537 (standar karena efisien dan aman).
Hitung d (private exponent):
𝑑
=
𝑒
−
1
m
o
d 
𝜑
(
𝑛
)
d=e
−1
modφ(n)
Artinya, 
𝑑
×
𝑒
≡
1
(
m
o
d
𝜑
(
𝑛
)
)
d×e≡1(modφ(n))
Hasil akhir:
Kunci Publik (public key): (e, n)
Kunci Privat (private key): (d, n)
c. Contoh Sederhana RSA
Misal:
p = 17, q = 11
n = 187
φ(n) = 160
Pilih e = 7
Hitung d = 23 (karena 7×23 ≡ 1 mod 160)
Kunci publik: (7, 187)
Kunci privat: (23, 187)
Enkripsi:
𝐶
=
𝑀
𝑒
m
o
d
𝑛
C=M
e
modn
Dekripsi:
𝑀
=
𝐶
𝑑
m
o
d
𝑛
M=C
d
modn
Dengan begitu, hanya pemilik kunci privat yang bisa membuka pesan tersebut.
d. Kelebihan RSA
Tidak perlu bertukar kunci rahasia secara langsung.
Sangat kuat karena bergantung pada sulitnya faktorisasi bilangan prima besar (misalnya 2048-bit).
Cocok untuk digital signature, autentikasi, dan enkripsi kunci AES


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
