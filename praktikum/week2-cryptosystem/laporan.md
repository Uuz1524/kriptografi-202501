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
- Pertanyaan 1:Komponen utama kriptosistem meliputi plaintext (data asli), ciphertext (data terenkripsi), kunci (nilai rahasia untuk enkripsi/dekripsi), dan algoritma (metode untuk enkripsi dan dekripsi). Kriptosistem juga dapat merujuk pada tiga algoritma: satu untuk pembangkitan kunci, satu untuk enkripsi, dan satu untuk dekripsi
Komponen utama
Plaintext: Data atau pesan asli yang ingin dilindungi, yang dapat dibaca oleh manusia sebelum dienkripsi.
Ciphertext: Bentuk pesan yang telah dienkripsi sehingga tidak dapat dibaca tanpa kunci yang benar.
Kunci (Key): Informasi rahasia (bisa berupa angka atau string) yang digunakan oleh algoritma untuk mengubah plaintext menjadi ciphertext (enkripsi) dan sebaliknya (dekripsi).
Algoritma: Metode atau fungsi matematika yang digunakan untuk melakukan enkripsi dan dekripsi. Algoritma ini menerima plaintext dan kunci sebagai masukan untuk menghasilkan ciphertext, dan menerima ciphertext dan kunci untuk menghasilkan plaintext kembali. 
Komponen tambahan
Algoritma Pembangkit Kunci: Algoritma yang menghasilkan pasangan kunci (kunci publik dan kunci privat) yang digunakan dalam enkripsi dan dekripsi.    Kunci Enkripsi: Kunci yang digunakan pengirim untuk mengenkripsi pesan.
Kunci Dekripsi: Kunci yang digunakan penerima untuk mendekripsi pesan

- Pertanyaan 2:Perbandingan antara sistem simetris dan asimetris, khususnya dalam konteks kriptografi (yang merupakan penerapan paling umum dari kedua sistem ini), dapat diringkas berdasarkan kelebihan dan kelemahannya masing-masing
Sistem Simetris (Kriptografi Kunci Rahasia)
Sistem simetris menggunakan satu kunci rahasia yang sama baik untuk mengenkripsi maupun mendekripsi data. 
Kelebihan:
Kecepatan dan Efisiensi: Proses enkripsi dan dekripsi jauh lebih cepat dan efisien, sehingga ideal untuk mengenkripsi data dalam jumlah besar (enkripsi massal).
Penggunaan Sumber Daya Rendah: Membutuhkan lebih sedikit daya komputasi (CPU dan memori).
Algoritma Sederhana: Algoritma yang digunakan umumnya lebih sederhana. 
Kelemahan:
Manajemen Kunci yang Rumit: Kunci rahasia harus dibagikan antara pengirim dan penerima melalui saluran yang aman, yang merupakan titik kerentanan utama dalam keamanan.
Masalah Otentikasi: Sulit untuk memverifikasi identitas pengirim secara pasti, karena kunci yang sama digunakan oleh kedua belah pihak.
Skalabilitas: Membutuhkan banyak kunci jika ingin berkomunikasi dengan banyak pihak secara rahasia (misalnya, A membutuhkan kunci unik untuk B, C, D, dst.). 
Sistem Asimetris (Kriptografi Kunci Publik)
Sistem asimetris menggunakan sepasang kunci yang saling terkait: satu kunci publik (dibagikan secara terbuka) untuk enkripsi, dan satu kunci pribadi (dirahasiakan oleh pemilik) untuk dekripsi. 
Kelebihan:
Tidak Perlu Pertukaran Kunci Aman: Kunci publik dapat dibagikan secara terbuka tanpa mengorbankan keamanan, menghilangkan kerentanan utama sistem simetris.
Otentikasi dan Tanda Tangan Digital: Memungkinkan verifikasi identitas (melalui tanda tangan digital), karena hanya pemilik kunci pribadi yang dapat membuat tanda tangan yang sesuai dengan kunci publiknya.
Kerahasiaan yang Lebih Kuat: Bahkan jika kunci publik jatuh ke tangan yang salah, data tetap aman karena kunci pribadi diperlukan untuk mendekripsi. 
Kelemahan:
Kecepatan Lambat: Proses enkripsi dan dekripsi jauh lebih lambat dan memakan waktu dibandingkan simetris karena algoritmanya yang lebih rumit.
Penggunaan Sumber Daya Tinggi: Mengonsumsi lebih banyak sumber daya komputasi, membuatnya tidak efisien untuk enkripsi data dalam jumlah besar.
Kompleksitas Manajemen Kunci: Meskipun pertukaran kunci lebih aman, manajemen pasangan kunci (publik dan pribadi) itu sendiri bisa rumit. 
kesimpulannya 
 jadi Secara umum, sistem simetris digunakan untuk kecepatan (enkripsi data massal), sedangkan sistem asimetris digunakan untuk keamanan dalam pertukaran kunci awal dan otentikasi (seperti pada sertifikat SSL/TLS dan VPN). Dalam praktiknya, kedua sistem ini sering digunakan bersama-sama: asimetris digunakan untuk bertukar kunci simetris secara aman, dan simetris kemudian digunakan untuk komunikasi data yang cepat dan efisien

Pertanyaan 3:karena kedua belah pihak harus memiliki kunci rahasia yang sama untuk enkripsi dan dekripsi. Masalah muncul karena kunci ini harus dibagikan melalui saluran yang aman, yang sulit atau tidak mungkin dilakukan dalam skala besar, sehingga ada risiko kunci tersebut dapat dicegat oleh pihak ketiga.
Masalah utama distribusi kunci
Kebutuhan saluran aman: Kunci rahasia harus dibagikan secara aman antara pengirim dan penerima sebelum komunikasi dimulai. Jika kunci dikirim melalui saluran yang tidak aman, kunci tersebut bisa disadap dan membahayakan seluruh data yang dienkripsi.
Skalabilitas: Dalam lingkungan yang melibatkan banyak pengguna, setiap pasangan komunikasi membutuhkan kunci yang berbeda. Ini membuat manajemen kunci menjadi sangat rumit dan tidak praktis untuk jumlah pengguna yang besar.
Kerentanan saat kunci terkompromi: Jika kunci rahasia jatuh ke tangan yang salah, semua komunikasi terenkripsi dengan kunci tersebut dapat dengan mudah dibobol.  
---

## 8. Kesimpulan
(Kode Python di atas mengimplementasikan sistem kriptografi sederhana berupa Caesar Cipher, yaitu algoritma enkripsi klasik yang melakukan pergeseran (shift) setiap huruf alfabet sebanyak nilai kunci (key) tertentu. 
Ringkasan dan Kesimpulan: 
1. Fungsi encrypt(plaintext, key) 
Menerima teks biasa (plaintext) dan kunci (key).
Untuk setiap karakter:
Jika karakter adalah huruf (baik besar maupun kecil), ia digeser ke kanan sebanyak key posisi dalam alfabet (dengan pembungkusan modulus 26 agar tetap dalam rentang A–Z atau a–z).
Karakter non-alfabet (seperti angka, spasi, tanda baca) tidak diubah.         
Mengembalikan teks terenkripsi (ciphertext).     
2. Fungsi decrypt(ciphertext, key) 
Menerima teks terenkripsi (ciphertext) dan kunci (key).
Melakukan kebalikan dari enkripsi: menggeser setiap huruf ke kiri sebanyak key posisi.
Juga melewatkan karakter non-alfabet tanpa perubahan.
Mengembalikan teks asli (plaintext).     
4. Bagian if __name__ == "__main__" 
Digunakan sebagai contoh penggunaan fungsi enkripsi dan dekripsi.
message = "<nim><nama>" seharusnya diisi dengan NIM dan nama mahasiswa sesuai instruksi praktikum (placeholder).
Menggunakan kunci tetap key = 5.
Menampilkan:
Plaintext asli,
Ciphertext hasil enkripsi,
Hasil dekripsi (yang seharusnya sama persis dengan plaintext awal).        
6. Jenis Algoritma 
Ini adalah Caesar Cipher dengan pergeseran tetap, termasuk dalam kategori symmetric-key cryptography (karena enkripsi dan dekripsi menggunakan kunci yang sama).
Tidak aman untuk penggunaan dunia nyata karena mudah dipecahkan dengan brute-force (hanya ada 25 kemungkinan kunci untuk alfabet Inggris)     
7. Karakteristik Implementasi 
Case-sensitive: mempertahankan huruf besar/kecil.
Non-alphabetic characters tetap utuh (tidak dienkripsi).
Menggunakan representasi ASCII dengan ord() dan chr().     
Kesimpulan Akhir:
jadi  implementasi Caesar Cipher sederhana untuk tujuan edukasi (misalnya, tugas praktikum kriptografi dasar). Ia menunjukkan prinsip dasar enkripsi substitusi alfabetik, serta bagaimana operasi modulus digunakan untuk "melingkarkan" alfabet. Namun, tidak cocok untuk keamanan nyata karena sangat rentan terhadap serangan analisis frekuensi atau brute-force.  )

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
Date:   2025-11-15

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
