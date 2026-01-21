# Laporan Praktikum Kriptografi
Minggu ke-: 12
Topik: [Aplikasi TLS & E-commerce]  
Nama: [Uswatun Khasanah]  
NIM: [230202782]  
Kelas: [5IKKA]  

---

## 1. Tujuan
(
    Menganalisis penggunaan kriptografi pada email dan SSL/TLS.
    Menjelaskan enkripsi dalam transaksi e-commerce.
    Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.
.)

---

## 2. Dasar Teori
(Informasi Sertifikat SSL/TLS Shopee
Issuer CA (Certificate Authority)
Sertifikat .shopee.co.id diterbitkan oleh GlobalSign GCC R6 AlphaSSL CA 2023, yang merupakan otoritas sertifikat dari GlobalSign nv-sa — sebuah Certificate Authority yang tepercaya dan dikenal luas.
Masa Berlaku Sertifikat
Berdasarkan pemeriksaan SSL:
Valid from: 24 Mar 2025
Valid until: 25 Apr 2026
Ini berarti sertifikat tersebut aktif kurang lebih 13 bulan, sesuai praktik masa berlaku sertifikat TLS saat ini.
Catatan: Industri SSL/TLS memang menurunkan masa berlaku sertifikat demi keamanan — sekarang umumnya kurang dari 398 hari (≈13 bulan).
Algoritma Enkripsi yang Digunakan
Signature Algorithm: sha256WithRSAEncryption
Key Size (kunci publik): RSA 2048 bit
Ini menunjukkan sertifikatnya menggunakan RSA 2048 untuk tanda tangan dan enkripsi awal.
Selain itu, koneksi HTTPS menggunakan cipher suite TLS modern yang secara umum melibatkan:
AES untuk enkripsi data simetris selama sesi.
ECDHE untuk pertukaran kunci cepat dan aman (tergantung setelan server/browser).
Detail cipher suite lengkap dapat dilihat di konsol browser (Developer Tools) → Security.

2. Bandingkan Website dengan HTTPS vs tanpa HTTPS
Website dengan HTTPS (aman)
Contoh: Shopee Indonesia (https://www.shopee.co.id)
Data komunikasi antara browser dan server terenkripsi sehingga tidak mudah dibaca oleh pihak ketiga.
Sertifikat yang valid diverifikasi oleh CA tepercaya (GlobalSign).
Browser menampilkan ikon gembok di address bar sebagai indikator koneksi aman.
Melindungi informasi sensitif seperti password, nomor kartu, alamat pengguna.
Keuntungan HTTPS:
Melindungi data dari penyadapan (eavesdropping).
Mencegah modifikasi data (integrity).
Menunjukkan identitas server yang sah.
Semua ini penting terutama untuk situs e-commerce yang memproses data pribadi dan transaksi keuangan.
Website tanpa HTTPS (tidak aman)
Contoh: Situs yang hanya menggunakan http:// tanpa S (secure).
Data ditransmisikan dalam teks biasa (plaintext) sehingga bisa disadap oleh siapa pun di jaringan yang sama.
Tidak ada verifikasi identitas server, sehingga rentan terhadap serangan man-in-the-middle (MITM).
Browser modern biasanya memberi peringatan “Not Secure” atau ikon peringatan.
Risiko tanpa HTTPS:
Password dan data login mudah dicuri.
No sertifikat digital → identitas server tidak terverifikasi.
Tidak ada enkripsi → semua data dapat dibaca.
Ringkasan Shopee SSL/TLS
Informasi	Detail
Domain	*.shopee.co.id
Issuer CA	GlobalSign GCC R6 AlphaSSL CA 2023 (GlobalSign nv-sa)
Valid From
24 Mar 2025
Valid Until
25 Apr 2026
Algoritma Kriptografi
RSA 2048 + SHA-256 (Signature)
Status HTTPS
Aktif & aman  )

    2.Isu privasi dalam Penggunaan Email Terenkripsi (PGP & S/MIME)
Walaupun PGP dan S/MIME melindungi isi email, masih ada beberapa isu privasi penting:
a. Metadata Masih Terbaca
Yang terenkripsi hanya isi pesan, bukan:
Alamat pengirim & penerima
Subjek email
Waktu pengiriman
Ukuran pesan
Artinya pola komunikasi tetap bisa dianalisis (siapa kirim ke siapa, seberapa sering, kapan).
b. Manajemen Kunci yang Rentan
Masalah umum:
Private key disimpan tidak aman (misalnya tanpa password kuat).
Kunci bocor → seluruh email lama bisa dibaca.
Pengguna awam sering salah mengelola key.
c. Ketergantungan pada Infrastruktur Pihak Ketiga (S/MIME)
S/MIME bergantung pada Certificate Authority (CA).
Jika CA diretas atau salah menerbitkan sertifikat → orang lain bisa menyamar sebagai pengguna sah.
d. Konflik antara Keamanan & Akses Organisasi
Email terenkripsi bisa membuat perusahaan tidak bisa memantau isi email karyawan, sehingga berpotensi menghambat audit atau investigasi internal.
Dilema Etika
Apakah perusahaan boleh mendekripsi email karyawan untuk audit?
Sudut Pandang Perusahaan	Sudut Pandang Privasi
Perusahaan perlu melindungi aset & data rahasia	Email adalah komunikasi pribadi
Untuk mencegah kebocoran data & kejahatan internal	Dekripsi tanpa izin melanggar privasi
Audit penting untuk kepatuhan hukum	Bisa disalahgunakan untuk memata-matai
Kesimpulan etika:
Perusahaan boleh mengaudit email hanya jika:
Sudah tertulis jelas dalam kebijakan internal.
Karyawan diberi tahu sejak awal.
Dekripsi dilakukan secara terbatas, terkontrol, dan untuk tujuan resmi (misalnya investigasi pelanggaran).
Tanpa persetujuan dan transparansi → tidak etis dan melanggar hak privasi.
Bagaimana kebijakan pemerintah terhadap komunikasi terenkripsi?
Kepentingan Pemerintah	Risiko terhadap Hak Warga
Mencegah terorisme & kejahatan siber	Pelanggaran kebebasan berekspresi
Perlu akses bukti digital	Potensi penyalahgunaan kekuasaan
Menjaga keamanan nasional	Muncul praktik mass surveillance
Dilema utama:
Pemerintah ingin memiliki backdoor untuk mengakses komunikasi.
Tapi backdoor ini melemahkan keamanan seluruh sistem, dan bisa dimanfaatkan pihak jahat.
Prinsip etis yang disepakati secara global:
Pengawasan hanya boleh:
Dengan dasar hukum yang jelas.
Melalui izin pengadilan.
Bersifat spesifik, terbatas, dan proporsional, bukan pengawasan massal.
3. Kesimpulan
Email terenkripsi (PGP & S/MIME) memang melindungi privasi pengguna, tetapi menimbulkan dilema:
Perusahaan ingin mengamankan data → berbenturan dengan privasi karyawan.
Pemerintah ingin menegakkan hukum → berisiko menggerus kebebasan sipil.)
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
Sertifikat
Masa Berlaku Sertifikat

    Not Before: 15 Januari 2024  
    Not After: 19 Januari 2025  

        → Masa berlaku: 1 tahun (standar industri untuk sertifikat OV/EV).
<img width="894" height="717" alt="image" src="https://github.com/user-attachments/assets/23952b90-f028-4fa4-a583-0ed072a1b2cf" />



## 6. Hasil dan Pembahasan
Perbedaan HTTPS vs HTTP (Tanpa SSL/TLS)

Aspek	                       HTTPS (Shopee)                   HTTP (Situs Tanpa SSL)
Keamanan Data	    ✅ Terenkripsi end-to-end	                ❌ Data dikirim dalam bentuk plain text
Autentikasi         ✅ Identitas server diverifikasi oleh CA	❌ Tidak ada verifikasi — bisa jadi situs palsu
Integritas	        ✅ Data tidak bisa diubah di tengah jalan	❌ Rentan dimodifikasi (man-in-the-middle)
Peringatan Browser	✅ Tidak ada peringatan — "Secure"       	❌ Ditandai sebagai **“Not Secure”**
SEO & Kepercayaan	✅ Diutamakan Google, pengguna percaya    	❌ Pengguna ragu, tingkat bounce tinggi


Algoritma Enkripsi & Kriptografi
Komponen                                         Algoritma
Public Key                                       RSA 2048-bit        
Signature Hash                                   SHA256withRSA
Koneksi Aman (Cipher Suite)                      TLS_AES_128_GCM_SHA256 (TLS 1.3) atau  TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (TLS 1.2)
Protokol                                         TLS 1.2 dan TLS 1.3 (versi aman terbaru)

Artinya:

Identitas Shopee diverifikasi secara organisasi (OV – Organization Validation).
Data ditransmisikan dengan enkripsi AES-128-GCM (sangat aman).
Kunci pertukaran menggunakan ECDHE (Perfect Forward Secrecy).

Kesimpulan Analisis
Shopee menggunakan SSL/TLS modern dengan sertifikat dari CA tepercaya (DigiCert).
Mengimplementasikan enkripsi kuat (AES-128-GCM) dan Perfect Forward Secrecy.
HTTPS wajib untuk e-commerce karena menangani data sensitif (login, pembayaran, alamat).
Situs tanpa HTTPS tidak layak dipercaya untuk transaksi apa pun.

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1:| HTTP                                             | HTTPS                                          |
| ------------------------------------------------ | ---------------------------------------------- |
| Tidak menggunakan enkripsi                       | Menggunakan enkripsi dengan protokol TLS/SSL   |
| Data dikirim dalam bentuk teks biasa (plaintext) | Data dikirim dalam bentuk terenkripsi          |
| Mudah disadap dan dimodifikasi oleh pihak lain   | Data lebih aman dari penyadapan dan manipulasi |
| URL diawali dengan `http://`                     | URL diawali dengan `https://`                  |
| Tidak ada verifikasi identitas server            | Server diverifikasi melalui sertifikat digital |

- Pertanyaan 2:Mengapa sertifikat digital menjadi penting dalam komunikasi TLS?
Sertifikat digital berfungsi sebagai identitas resmi sebuah website/server.
Fungsi utama sertifikat digital dalam TLS:
Autentikasi Server
Memastikan bahwa server yang kita akses benar-benar server asli, bukan server palsu (phishing).
Mencegah Man-in-the-Middle Attack
Tanpa sertifikat, penyerang bisa berpura-pura menjadi server dan mencuri data.
Menyediakan Kunci Publik
Sertifikat membawa public key yang digunakan untuk proses enkripsi awal dalam TLS.
Diterbitkan oleh Certificate Authority (CA)
CA seperti DigiCert, Let's Encrypt, dll menjamin keaslian server.

- Pertanyaan 3:Kriptografi mendukung privasi
Melindungi pesan pribadi (WhatsApp, Email, E-Banking).
Menjaga kerahasiaan data penting (password, data kesehatan, data akademik).
Mencegah penyadapan oleh pihak yang tidak berwenang.
b. Tantangan hukum dan etika
Dampak Positif	Tantangan Hukum & Etika
Data pribadi terlindungi	Penjahat bisa menyembunyikan aktivitas ilegal
Kebebasan berekspresi terjamin	Sulit bagi aparat menelusuri kejahatan digital
Keamanan transaksi meningkat	Potensi konflik antara hak privasi dan penegakan hukum
)
---

## 8. Kesimpulan
(Shopee menerapkan SSL/TLS secara optimal dengan sertifikat digital dari Certificate Authority tepercaya (DigiCert), menggunakan enkripsi kuat (RSA 2048-bit + AES-128-GCM) dan protokol keamanan terbaru (TLS 1.2/1.3). Penerapan HTTPS ini menjamin kerahasiaan, integritas, dan autentikasi data pengguna — terutama saat login, bertransaksi, atau mengakses informasi pribadi.

Sebaliknya, situs tanpa HTTPS tidak aman, rentan penyadapan, dan tidak layak digunakan untuk aktivitas sensitif. Dengan demikian, SSL/TLS bukan lagi pilihan, melainkan keharusan mutlak bagi platform e-commerce modern seperti Shopee untuk melindungi privasi pengguna dan membangun kepercayaan digital.  )

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
Author: Uswatun Khasanah<khasanah8952@gmail.com>
Date:   2025-09-6

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
