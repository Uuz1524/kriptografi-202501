# Laporan Praktikum Kriptografi
Minggu ke-: 7
Topik: [Diffie-Hellman Key Exchange]  
Nama: [uswatun khasanah]  
NIM: [230202782]  
Kelas: [5 IKKA]  

---

## 1. Tujuan
(Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).
.)

## 2. Dasar Teori
(Diffie-Hellman Key Exchange (DHKE)adalah protokol kriptografi yang memungkinkan dua pihak (misalnya Alice dan Bob) untuk menghasilkan kunci rahasia bersama (shared secret key) melalui saluran komunikasi yang tidak aman—tanpa pernah mengirimkan kunci tersebut secara eksplisit. Protokol ini diperkenalkan oleh Whitfield Diffie dan Martin Hellman pada tahun 1976, dan menjadi fondasi penting bagi kriptografi kunci publik. Intinya, DHKE memanfaatkan sifat matematis dari modular exponentiation (perpangkatan modular), khususnya kesulitan memecahkan *Discrete Logarithm Problem (DLP): meskipun pihak ketiga (Eve) bisa melihat semua nilai yang dikirim (seperti basis g, modulus prima p, dan nilai publik gᵃ mod p dan gᵇ mod p), ia tidak dapat dengan mudah menghitung kunci bersama gᵃᵇ mod ptanpa mengetahui a atau b.

Prosesnya dimulai dengan kesepakatan dua parameter publik: bilangan prima besar p dan generator g (biasanya kecil, seperti 2 atau 5). Alice memilih kunci privat rahasia a, lalu menghitung dan mengirim A = gᵃ mod p ke Bob. Secara paralel, Bob memilih kunci privat bdan mengirim B = gᵇ mod p ke Alice. Keduanya kemudian menghitung kunci bersama: Alice menghitung s = Bᵃ mod p, sedangkan Bob menghitung s = Aᵇ mod p. Karena Bᵃ ≡ (gᵇ)ᵃ ≡ gᵃᵇ ≡ (gᵃ)ᵇ ≡ Aᵇ (mod p), keduanya mendapatkan nilai s yang identik—yang kemudian bisa digunakan sebagai kunci enkripsi simetris (misalnya untuk AES). Keamanan DHKE bergantung pada asumsi bahwa komputasi a dari g dan gᵃ mod p (atau b dari gᵇ mod p) secara komputasional tidak layak (infeasible) saat p cukup besar (misalnya 2048-bit atau lebih), meskipun protokol ini rentan terhadap serangan man-in-the-middle jika tidak dipadukan dengan mekanisme autentikasi (seperti digital signature)
Definisi Diffie-Hellman Key Exchange (DHKE) adalah sebuah protokol kriptografi yang memungkinkan dua pihak yang belum pernah berkomunikasi sebelumnya untuk secara aman menyepakati sebuah kunci rahasia bersama melalui saluran komunikasi yang tidak aman (misalnya internet), tanpa perlu membagikan kunci tersebut secara langsung. 
Protokol ini bukan metode enkripsi data, melainkan metode key agreement (persetujuan kunci). Keamanannya didasarkan pada kesulitan komputasi dalam memecahkan Discrete Logarithm Problem (DLP) dalam aritmetika modular—yaitu, sulitnya menentukan eksponen rahasia (a atau b) dari hasil perpangkatan modular (gᵃ mod p), meskipun nilai g, p, dan hasilnya diketahui publik. DHKE menjadi landasan penting bagi banyak protokol keamanan modern seperti TLS/SSL, SSH, dan IPsec, meskipun biasanya dikombinasikan dengan mekanisme autentikasi untuk mencegah serangan man-in-the-middle.).  
cara kerjanya 
Langkah-Langkah Cara Kerja DHKE 
Persetujuan Parameter Publik
Alice dan Bob terlebih dahulu menyepakati dua bilangan publik (boleh diketahui siapa saja): 
Bilangan prima besar p (misal: 23)
Generator g, di mana 1 < g < p (misal: 5)
(Nilai p dan g bisa distandarkan, seperti dalam grup RFC 3526)
Pemilihan Kunci Privat Rahasia  
Alice memilih kunci privat rahasia a (misal: a = 6)  
Bob memilih kunci privat rahasia b (misal: b = 15)
(Nilai ini tidak pernah dikirim dan hanya diketahui masing-masing pihak.)
 Pertukaran Nilai Publik   
Alice menghitung:
A = gᵃ mod p = 5⁶ mod 23 = 15625 mod 23 = 8
Lalu mengirim A = 8 ke Bob.  
Bob menghitung:
B = gᵇ mod p = 5¹⁵ mod 23 = 30517578125 mod 23 = 19
Lalu mengirim B = 19 ke Alice.
(Nilai A dan B boleh diketahui publik — tidak membahayakan kunci rahasia.)
Perhitungan Kunci Bersama (Shared Secret)   
Alice menerima B = 19, lalu menghitung:
s = Bᵃ mod p = 19⁶ mod 23 = 47045881 mod 23 = 2  
Bob menerima A = 8, lalu menghitung:
s = Aᵇ mod p = 8¹⁵ mod 23 = 35184372088832 mod 23 = 2        
Keduanya mendapatkan kunci bersama s = 2, meski hanya bertukar data publik!
Mengapa Aman? 
Penyerang (Eve) hanya melihat: p = 23, g = 5, A = 8, B = 19.  
Untuk mencari s = 2, Eve harus mengetahui a atau b, yaitu:  
a dari 5ᵃ ≡ 8 mod 23 → discrete log: a = log₅(8) mod 23 = 6  
b dari 5ᵇ ≡ 19 mod 23 → b = 15
Saat p sangat besar (misal: 2048-bit), menghitung a atau b secara komputasional sangat sulit (butuh waktu ribuan tahun dengan teknologi saat ini).
     

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
- Pertanyaan 1: Karena Diffie-Hellman memungkinkan pertukaran kunci di saluran publik karena tidak ada kunci rahasia yang dikirimkan secara langsung—yang ditransmisikan hanyalah nilai-nilai publik, sedangkan kunci bersama (shared secret) dihitung secara independen oleh masing-masing pihak menggunakan kunci privat mereka yang tetap dirahasiakan. 
Keamanannya bersandar pada asimetri komputasi matematis:   
Operasi forward (menghitung nilai publik dari kunci privat) mudah:
Misalnya, menghitung A=gamodp  cepat, bahkan untuk bilangan sangat besar.  
Namun operasi inverse-nya—yaitu menentukan eksponen rahasia a  dari A,g,  dan p  (dikenal sebagai Discrete Logarithm Problem / DLP)—sangat sulit secara komputasional ketika p  cukup besar (misalnya 2048-bit atau lebih).
Dengan kata lain, meskipun penyerang melihat semua data yang lewat di saluran publik (p,g,A,B ), ia tidak bisa secara praktis menghitung kunci bersama s=gabmodp  tanpa menyelesaikan DLP—yang sampai saat ini belum ada algoritma klasik (non-kuantum) yang efisien untuk melakukannya.
Dengan demikian, Diffie-Hellman menciptakan "rahasia bersama dari informasi publik", memungkinkan dua pihak membangun kunci simetris untuk enkripsi (misalnya AES) tanpa pernah bertemu atau berbagi rahasia sebelumnya—sebuah terobosan yang menjadi dasar keamanan komunikasi modern di internet


- Pertanyaan 2: dalah tidak adanya autentikasi pihak yang terlibat, sehingga sangat rentan terhadap serangan man-in-the-middle (MitM). 
Penjelasan Serangan MitM pada DH Murni: 
Alice ingin berkomunikasi dengan Bob dan memulai protokol DH.
Penyerang (Eve) menyisipkan diri di tengah:
Saat Alice mengirim nilai publiknya A=gamodp , Eve mencegat dan menggantinya dengan nilai publik miliknya sendiri, E1​=ge1​modp , lalu meneruskannya ke Bob.
Saat Bob membalas dengan B=gbmodp , Eve kembali mencegat dan menggantinya dengan E2​=ge2​modp , lalu mengirim ke Alice.         
kibatnya:
Alice berpikir dia berbagi kunci dengan Bob, padahal dia berbagi kunci dengan Eve: s1​=E2a​modp 
Bob berpikir dia berbagi kunci dengan Alice, padahal dia berbagi kunci dengan Eve: s2​=E1b​modp 
Eve kini mengetahui kedua kunci rahasia dan bisa membaca, memodifikasi, atau menyisipkan pesan—tanpa diketahui Alice maupun Bob.

Solusi Umum biasanya untuk mengatasi kelemahan ini, DH harus dikombinasikan dengan mekanisme autentikasi, misalnya: 
Digital signature (misal: DSA, ECDSA): Alice dan Bob menandatangani nilai publik mereka sebelum mengirim.
Sertifikat digital (dalam TLS): Nilai publik DH disertakan dalam sertifikat yang ditandatangani oleh otoritas tepercaya (CA).
Pre-shared key (PSK) atau password-authenticated DH (misal: SRP).
Protokol seperti TLS, SSH, dan Signal Protocol menggunakan Authenticated Diffie-Hellman (misal: ECDHE dengan signature) — bukan DH murni — demi keamanan end-to-end

_pertanyaan 3: Untuk mencegah serangan man-in-the-middle (MITM) pada protokol Diffie-Hellman, kunci utamanya adalah menambahkan mekanisme autentikasi — sehingga pihak-pihak yang berkomunikasi dapat memverifikasi identitas satu sama lain sebelum atau selama pertukaran kunci. Berikut cara-cara utama yang digunakan dalam praktik: 
 1. Menggunakan Digital Signature (Authenticated DH) 
Setiap pihak menandatangani nilai publik DH-nya dengan kunci privat dari pasangan kunci asimetris (misalnya RSA atau ECDSA), lalu mengirim tanda tangan tersebut bersama nilai publik. 
Contoh alur:
Alice menghitung nilai publik DH-nya: A=gamodp 
Alice membuat tanda tangan: σA​=SignprivA​​(A) 
Alice mengirim (A,σA​,sertifikatA​)  ke Bob
Bob memverifikasi tanda tangan menggunakan kunci publik Alice (dari sertifikat yang diverifikasi oleh CA tepercaya)
Jika valid → Bob yakin bahwa A  benar-benar berasal dari Alice
Digunakan di TLS (ECDHE-RSA / ECDHE-ECDSA), SSH (host key verification), dan Signal Protocol.  
2. Menggunakan Sertifikat Digital (Public Key Infrastructure / PKI) 
Nilai kunci publik (baik untuk DH maupun signature) dibundel dalam sertifikat X.509 yang ditandatangani oleh Certificate Authority (CA) tepercaya. 
Saat klien (misal browser) terhubung ke server:
Server mengirim sertifikatnya yang berisi kunci publiknya (dan sering kali juga parameter DH/ECDH)
Klien memverifikasi rantai kepercayaan sertifikat hingga ke root CA yang dikenal
Jika lolos klien yakin berkomunikasi dengan domain yang benar, bukan penir
Ini yang membuat gembok muncul di browser saat membuka https://.  
3. Pre-Shared Key (PSK) atau Password-Authenticated DH 
Jika dua pihak sudah memiliki rahasia bersama sebelumnya (misalnya password atau kunci simetris), rahasia itu bisa dipakai untuk mengautentikasi pertukaran DH. 
Contoh protokol:
SRP (Secure Remote Password): Memungkinkan autentikasi berbasis password tanpa mengirim password itu sendiri.
Dragonfly (IEEE 802.11s): Digunakan di Wi-Fi Protected Setup (WPA3-SAE).
Keuntungan: tidak butuh infrastruktur PKI, cocok untuk IoT atau perangkat embedded. 
4. Key Confirmation & Binding 
Setelah kunci bersama dihasilkan, kedua pihak mengirim pesan terautentikasi (misalnya HMAC atau enkripsi) menggunakan kunci tersebut untuk membuktikan bahwa mereka benar-benar memiliki kunci yang sama — ini mencegah "pengalihan kunci" oleh penyerang. 
Contoh dalam TLS:   
Finished message di akhir handshake berisi hash dari semua data handshake, dienkripsi/HMAC dengan kunci sesi — jika tidak cocok, koneksi dibatalkan. 
     
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

Author: uswatun kasanah <khasanah@gmail.com>
Date:   2025-11-16

    week7-cryptosystem: diffie-hellman )
```
