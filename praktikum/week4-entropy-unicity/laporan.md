# Laporan Praktikum Kriptografi
Minggu ke-: 4
Topik: [Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)]  
Nama: [uswtun khasanah]  
NIM: [230202782]  
Kelas: [5 IKKA]  

---

## 1. Tujuan
( Menyelesaikan perhitungan sederhana terkait entropi kunci.
Menggunakan teorema Euler pada contoh perhitungan modular & invers.
Menghitung unicity distance untuk ciphertext tertentu.
Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.
.)

---

## 2. Dasar Teori
(Entropy (Entropi) 
Definisi Informal 
Entropi mengukur jumlah ketidakpastian atau kerandoman dalam sebuah sumber informasi — khususnya, dalam konteks kriptografi: seberapa sulit menebak kunci. 
Definisi Formal (Shannon Entropy) 
Untuk variabel acak X  yang dapat mengambil nilai x1​,x2​,...,xn​  dengan probabilitas p(xi​) , entropi didefinisikan sebagai: 
H(X)=−i=1∑n​p(xi​)log2​p(xi​)(dalam satuan *bit*) 
Contoh: Entropi Kunci 
Kunci 1 bit,
adil
(0/1 sama mungkin)
{0, 1}
p(0)=p(1)=0.5
H=−2⋅0.5log2​0.5=1 bit
Kunci 1 bit,
bias
(0 muncul 90%)
{0, 1}
p(0)=0.9,p(1)=0.1
H=−[0.9log2​0.9+0.1log2​0.1]≈0.469 bit
Kunci 128-bit,
seragam & acak
2128 kemungkinan
Semua p=1/2128
H=128 bit 
Entropi maksimum terjadi ketika semua kunci sama mungkin (uniform) → inilah yang diinginkan dalam desain kriptografi. 
 Masalah Nyata: Effective Key Length 
 Jika generator kunci buruk (misal: seed 32-bit untuk PRNG yang menghasilkan 256-bit key), maka entropi efektif hanya 32 bit — meskipun kuncinya 256 bit!
    Contoh nyata: Android Bitcoin wallets (2013) gagal karena entropi rendah → kunci bisa ditebak.
2. Unicity Distance (Jarak Unisitas) 
Apa itu? 
    Unicity distance adalah panjang ciphertext minimum yang diperlukan agar hanya ada satu kunci yang masuk akal (yaitu: menghasilkan plaintext dalam bahasa alami) — sehingga serangan brute-force bisa mengidentifikasi kunci yang benar secara unik. 
Diperkenalkan oleh Claude Shannon (1949) dalam teori keamanan informasi. 
Rumus Unicity Distance (U ) 
U=DH(K)​ 
di mana: 
    H(K)  = entropi kunci (dalam bit)  
    D  = redundansi bahasa (dalam bit per karakter)
Redundansi Bahasa (D ) 
D=R0​−R 
R0​=log2​∣Σ∣  = kapasitas maksimum (untuk alfabet bahasa Inggris: ∣Σ∣=26  → R0​≈4.7  bit/char)
 R  = laju entropi aktual bahasa (untuk Inggris: ~1.0–1.5 bit/char)
Jadi redundansi bahasa Inggris:  
D≈4.7−1.3=3.4 bit per karakter 
Contoh Hitung Unicity Distance 
Kasus: Substitusi Caesar (kunci = pergeseran 0–25) 
 Jumlah kunci = 26 → H(K)=log2​26≈4.7  bit
D≈3.4  bit/char (bahasa Inggris)
U=3.44.7​≈1.38 karakter 
Artinya: dengan hanya 2 karakter ciphertext, serangan brute-force sudah bisa menentukan kunci yang benar secara unik karena hanya satu hasil dekripsi yang "bermakna". 
Kasus: DES (56-bit key) 
H(K)=56  bit  
D=3.4  bit/char
U=3.456​≈16.5 karakter≈132 bit ciphertext 
Ciphertext sepanjang ~17 karakter cukup untuk memastikan hanya satu kunci menghasilkan plaintext Bahasa Inggris yang valid. 
Kasus: AES-128 
H(K)=128  bit  
U=3.4128​≈37.6  karakter
Masih kecil? Tidak masalah — karena brute-force 2¹²⁸ tetap mustahil, meski ciphertext-nya panjang. 
Inti: Unicity distance tidak mengukur kepraktisan serangan, tapi kapan serangan menjadi teoretis unik. 
Perbandingan: Entropi vs Unicity Distance 
Fokus
Kekuatan
kunci
(kerandoman, panjang efektif)
Kekuatan
sistem
(kapan ciphertext cukup untuk identifikasi unik)
Satuan
bit
karakter (atau bit)
Tergantung pada
Distribusi kunci
- Entropi kunci
- Redundansi bahasa plaintext
Serangan relevan
Brute-force, side-channel
Ciphertext-only attack, exhaustive key search
Tujuan desain
Maksimalkan H(K) → gunakan kunci acak penuh
Jika U kecil, sistem rentan
secara teoretis
tapi keamanan praktis tetap tergantung pada H(K) 
Implikasi untuk Desain Kriptosistem 
Gunakan kunci dengan entropi tinggi
Hindari pola, gunakan CSPRNG (Cryptographically Secure PRNG). 
Hindari redundansi berlebihan di plaintext
Kompresi sebelum enkripsi mengurangi redundansi → meningkatkan U  → lebih aman secara teoretis. 
Jangan percaya pada "security through obscurity"
Entropi rendah (misal: password lemah) membuat U  kecil → mudah di-brute-force. 
Unicity distance kecil ≠ sistem lemahContoh: AES-128 punya U≈38  karakter, tapi brute-force-nya tetap butuh ~10³⁶ tahun — aman secara praktis.  
Ringkasan (Untuk Laporan/Slide) 
Entropi Kunci
H(K)=−∑p(k)log2​p(k)
Ukuran kerandoman kunci; maksimal = panjang kunci (bit)
Redundansi
( D = \log_2
\Sigma
Unicity Distance
U=DH(K)​
Panjang ciphertext minimal agar hanya 1 kunci menghasilkan plaintext bermakna
profile
Qwen3-Max 12:26 am

Entropy mengukur tingkat ketidakpastian atau kerandoman dalam kunci kriptografi, dinyatakan dalam bit. Semakin tinggi entropi (mendekati panjang kunci ideal), semakin sulit kunci tersebut ditebak melalui brute-force. Misalnya, kunci 128-bit yang benar-benar acak memiliki entropi 128 bit—artinya diperlukan rata-rata 2127  percobaan untuk menemukannya. Namun, jika kunci dihasilkan dari sumber dengan entropi rendah (misalnya password manusia), entropi efektif bisa jauh lebih kecil, sehingga keamanan sistem menurun drastis meskipun panjang kuncinya besar. 
Unicity distance adalah panjang ciphertext minimum yang diperlukan agar hanya satu kunci menghasilkan plaintext yang bermakna (misalnya, dalam bahasa alami). Rumusnya U=H(K)/D , dengan H(K)  sebagai entropi kunci dan D  sebagai redundansi bahasa (≈3.4 bit/karakter untuk Bahasa Inggris). Contohnya, untuk DES (56-bit), U≈17  karakter—artinya dengan ciphertext sependek itu, serangan brute-force teoretis sudah bisa mengidentifikasi kunci yang benar secara unik. Namun, unicity distance kecil tidak serta-merta membuat sistem lemah secara praktis; keamanan tetap ditentukan oleh besarnya entropi kunci dan kelayakan komputasi mengeksekusi brute-force. Kesimpulan:   
Entropi tinggi → brute-force sulit.  
Unicity distance besar → serangan teoretis lebih lama konvergen.  
Keduanya penting untuk analisis keamanan komprehensif
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
import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](<img width="1366" height="727" alt="image" src="https://github.com/user-attachments/assets/36cb26e4-c1df-4e01-9e6c-a03aed74f151" />
)
![Hasil Output](<img width="722" height="246" alt="image" src="https://github.com/user-attachments/assets/2cb78f94-ff92-49c9-b6e9-0bca99fe06ec" />
)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: jadi Dalam konteks kekuatan kunci, nilai entropy menyatakan jumlah informasi (dalam bit) yang benar-benar acak dan tidak dapat diprediksi dalam kunci tersebut. Semakin tinggi entropy, semakin besar ruang pencarian yang harus dilalui penyerang dalam serangan brute-force, sehingga kunci semakin kuat. Misalnya, kunci 128-bit dengan entropy 128 bit berarti semua 2128  kemungkinan kunci sama mungkin muncul—menjadikannya sangat kuat. Sebaliknya, jika entropy hanya 40 bit (misalnya karena pola atau sumber acak lemah), maka meskipun kuncinya panjang, ruang pencarian efektif hanya 240 , yang bisa dipecahkan dengan komputasi modern. Jadi, entropy mengukur kekuatan nyata kunci, bukan sekadar panjangnya.
- 
- Pertanyaan 2:Unicity distance penting karena memberikan batas teoretis tentang seberapa banyak ciphertext yang dibutuhkan agar hanya ada satu kunci yang menghasilkan plaintext bermakna—artinya, di bawah panjang ini, banyak kunci bisa menghasilkan teks yang tampak valid (ambigu), sehingga serangan ciphertext-only tidak bisa menentukan kunci yang benar secara unik. Jika unicity distance sangat kecil (misalnya 2–3 karakter untuk sandi Caesar), maka sistem rentan secara teoretis: cukup dengan ciphertext pendek, penyerang dapat mengidentifikasi kunci yang benar hanya dengan mencari hasil dekripsi yang masuk akal. Sebaliknya, cipher yang baik memiliki unicity distance besar, memaksa penyerang memerlukan ciphertext sangat panjang untuk mempersempit kandidat kunci—meskipun dalam praktik, keamanan tetap tergantung pada besarnya entropi kunci dan ketidaklayakan brute-force

- pertanyaan 3:Brute force tetap menjadi ancaman meskipun algoritma kriptografi (seperti AES atau RSA) secara matematis kuat, karena keamanan praktis sistem tidak hanya bergantung pada algoritma, tetapi juga pada implementasi dan manajemen kunci. Jika kunci yang digunakan memiliki entropi rendah—misalnya password lemah, pola prediktabel, atau generator acak yang cacat—maka ruang pencarian efektif jauh lebih kecil daripada yang dirancang algoritma, sehingga brute force menjadi layak dilakukan (contoh: serangan terhadap kunci 6-digit PIN hanya butuh maksimal 1 juta percobaan). Selain itu, kemajuan teknologi (GPU, FPGA, ASIC, komputasi awan) serta teknik optimasi (rainbow tables, dictionary attack, parallelisasi) terus menurunkan biaya dan waktu serangan brute force. Dengan demikian, algoritma yang kuat bisa “dikalahkan” bukan karena kelemahan matematisnya, tetapi karena kelemahan di lapisan pengguna atau sistem, menjadikan brute force ancaman yang terus relevan selama kunci tidak dikelola dengan baik 
)
---

## 8. Kesimpulan
( Entropi Ruang Kunci 26
Menghitung entropi untuk ruang kunci berukuran 26 (misalnya: huruf alfabet A-Z).
Rumus: log₂(26) ≈ 4.7 bit
Artinya: Dibutuhkan sekitar 4.7 bit informasi untuk menggambarkan satu kemungkinan kunci dalam ruang 26 elemen.
Ini menunjukkan bahwa kekuatan kriptografi dengan hanya 26 kemungkinan kunci sangat lemah — bisa dipecahkan dengan mudah (brute force).
2. Entropi Ruang Kunci 2¹²⁸
Menghitung entropi untuk ruang kunci berukuran 2¹²⁸ (misalnya: kunci AES-128).
Rumus: log₂(2¹²⁸) = 128 bit
Artinya: Dibutuhkan tepat 128 bit informasi untuk menggambarkan satu kemungkinan kunci.
Ini menunjukkan tingkat keamanan yang sangat tinggi — hampir mustahil untuk dipecahkan secara brute force dengan teknologi saat ini.
Kesimpulan Utama:
Semakin besar ruang kunci, semakin tinggi entropinya — dan semakin kuat keamanan sistem kriptografinya.
uang kunci kecil (misal: 26) → Entropi rendah → Mudah ditembus.
Ruang kunci besar (misal: 2¹²⁸) → Entropi tinggi → Sangat aman.
Ini adalah dasar penting dalam kriptografi modern:
Kkuatan kunci tidak hanya tergantung pada panjangnya, tapi juga pada ukuran ruang kuncinya.
Entropi adalah ukuran matematis dari ketidakpastian atau keacakan — semakin tinggi, semakin sulit ditebak.
)

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
week4-entropy-unicity: Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force )
```
