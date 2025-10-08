# Laporan Praktikum Kriptografi
Minggu ke-: 1
Topik: [Pengenalan Kriptografi]  
Nama: [Uswatun Khasanah]  
NIM: [230202782]  
Kelas: [5IKKA]  

---

## 1. Tujuan
Kriptografi merupakan ilmu dan seni untuk menjaga kerahasiaan serta keamanan informasi agar tidak dapat dibaca atau dimanipulasi oleh pihak yang tidak berwenang. Perkembangan kriptografi dapat dibagi menjadi tiga era utama: kriptografi klasik, kriptografi modern, dan kriptografi kontemporer.

Era Kriptografi Klasik
Pada masa ini, kriptografi berfokus pada manipulasi huruf dalam pesan teks (plaintext) menjadi bentuk yang tidak bermakna (ciphertext) dengan menggunakan teknik substitusi dan transposisi sederhana.

Caesar Cipher adalah salah satu metode tertua, ditemukan oleh Julius Caesar. Algoritma ini menggantikan setiap huruf dengan huruf lain yang berjarak tetap dalam alfabet. Misalnya, pergeseran 3 huruf akan mengubah “A” menjadi “D”.

Vigenère Cipher menyempurnakan Caesar Cipher dengan menggunakan kunci berupa kata, sehingga pergeseran huruf berbeda-beda tergantung posisi karakter pada kunci. Vigenère dianggap lebih kuat karena membuat pola enkripsi lebih sulit ditebak.
Kelemahan utama kriptografi klasik adalah ketergantungannya pada kerahasiaan algoritma dan mudah diserang menggunakan analisis frekuensi.

Perkembangan Kriptografi Modern
Era modern dimulai sekitar pertengahan abad ke-20, dipengaruhi oleh karya Claude Shannon, yang dikenal sebagai bapak kriptografi modern. Prinsip yang diperkenalkan Shannon menekankan bahwa keamanan sistem harus bergantung pada kerahasiaan kunci, bukan algoritma.

RSA (Rivest–Shamir–Adleman) adalah algoritma kunci publik yang memanfaatkan konsep matematika bilangan prima besar untuk menghasilkan pasangan kunci (publik dan privat). RSA banyak digunakan dalam komunikasi aman di internet.

AES (Advanced Encryption Standard) adalah algoritma simetris yang digunakan secara luas untuk enkripsi data digital, menggantikan DES. AES terkenal karena efisien dan sangat aman terhadap serangan kriptanalisis modern.
Evolusi Menuju Kriptografi Kontemporer
Perkembangan teknologi digital mendorong munculnya kriptografi kontemporer, yang berperan penting dalam sistem keamanan berbasis jaringan dan ekonomi digital.
Blockchain menggunakan konsep kriptografi hash dan tanda tangan digital untuk memastikan integritas dan keaslian data dalam jaringan terdistribusi tanpa otoritas pusat.

Cryptocurrency seperti Bitcoin mengandalkan blockchain serta algoritma kriptografi seperti SHA-256 dan ECDSA (Elliptic Curve Digital Signature Algorithm) untuk menjaga keamanan transaksi dan kepemilikan aset digital.

## 2. Dasar Teori
1. Kerahasiaan (Confidentiality)
Penjelasan:
Kerahasiaan berarti menjaga agar data atau informasi hanya dapat diakses oleh pihak yang berwenang. Tujuannya adalah melindungi data dari akses atau pengungkapan yang tidak sah.
Contoh nyata:
Sistem perbankan menggunakan enkripsi data (misalnya SSL/TLS) untuk melindungi informasi pribadi nasabah seperti nomor rekening atau kata sandi saat transaksi online.
2. Integritas (Integrity)**
Penjelasan:
Integritas berkaitan dengan menjaga keaslian dan keutuhan data agar tidak diubah, dihapus, atau dimanipulasi oleh pihak yang tidak berwenang — baik secara sengaja maupun tidak sengaja.
Contoh nyata:
Dalam pengiriman file melalui internet, digunakan checksum atau hash function (misalnya SHA-256)untuk memastikan bahwa file tidak mengalami perubahan selama proses transmisi.
3. Ketersediaan (Availability)
Penjelasan:
Ketersediaan memastikan bahwa sistem, data, dan layanan selalu dapat diakses oleh pengguna yang berwenang kapan pun diperlukan.
Contoh nyata:
Layanan website e-commerce menggunakan server cadangan (backup server)dan sistem load balancing untuk memastikan situs tetap dapat diakses meskipun terjadi gangguan pada salah satu server utama.

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
- Pertanyaan 1:Siapa tokoh yang dianggap sebagai bapak kriptografi modern?
- 1.	Claude E. Shannon dikenal sebagai “Bapak Kriptografi Modern” dan juga “Bapak Teori Informasi”.
Pada tahun 1949, ia menerbitkan makalah berjudul “Communication Theory of Secrecy Systems”, yang menjelaskan dasar ilmiah dari keamanan kriptografi.
Kontribusi penting Shannon:
Mendefinisikan konsep “confusion” dan “diffusion” — dua prinsip utama desain cipher modern.
Membedakan keamanan absolut (perfect secrecy) dari keamanan berdasarkan kesulitan komputasi.
- Pertanyaan 2:Sebutkan algoritma kunci publik yang populer digunakan saat ini.
- 2.	Menggabungkan teori informasi dan matematika ke dalam kriptografi, menjadikannya bidang ilmiah, bukan sekadar seni.Algoritma kunci publik yang populer digunakan saat ini antara lain RSA, ElGamal, dan Kriptografi Kurva Eliptik (ECC). Algoritma-algoritma ini mengandalkan masalah matematika yang sulit dipecahkan, seperti faktorisasi bilangan prima besar untuk RSA, logaritma diskrit untuk ElGamal, dan sifat kurva eliptik untuk ECC, yang memungkinkan pembuatan pasangan kunci publik dan pribadi untuk enkripsi dan dekripsi data. 
a.RSA (Rivest Shamir Adleman)
Prinsip Keamanan: Keamanan RSA didasarkan pada kesulitan memfaktorkan bilangan besar menjadi faktor-faktor primanya. 
Fungsi: Dapat digunakan untuk enkripsi, dekripsi, dan penandatanganan digital. 
Penggunaan: Algoritma ini sangat populer dan banyak digunakan untuk melindungi data sensitif. 
b. ElGamal 
Prinsip Keamanan: Keamanan ElGamal terletak pada sulitnya menghitung logaritma diskrit.
Fungsi: Awalnya untuk tanda tangan digital, tetapi juga dapat digunakan untuk enkripsi dan dekripsi data.
c. Kriptografi Kurva Eliptik (ECC - Elliptic Curve Cryptography)
Prinsip Keamanan: 
Keamanan ECC didasarkan pada sulitnya memecahkan masalah logaritma diskrit pada kurva eliptik. 
Keunggulan: 
Keunggulan utamanya adalah ukuran kunci yang lebih kecil dibandingkan dengan RSA dan ElGamal, sehingga lebih efisien untuk perangkat dengan sumber daya terbatas. 
Penggunaan: 
Digunakan untuk aplikasi yang memerlukan efisiensi komputasi yang lebih tinggi, seperti pada perangkat seluler. 
-pertanyaan 3:Apa perbedaan utama antara kriptografi klasik dan kriptografi modern?
 Aspek 
Dari Teknik dasar 
Kriptografi klasik
Berdasarkan penggantian (substitution) dan pergeseran (transposition) huruf
Kriptografi modern
Berdasarkan matematika dan teori informasi yang kompleks
Aspek dari data yang di olah
Kriptografi klasik
Jenis Data yang Diolah	Biasanya hanya untuk teks alfabet (huruf)
Kriptografi modern
Dapat digunakan untuk semua jenis data digital (teks, gambar, suara, video).
Aspek dari jenis kunci 
Kriptografi klasik
Hanya cocok untuk teks alfabeth
Kriptografi modern
Dapat di gunakan untuk jenis semua jenis data digital


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
