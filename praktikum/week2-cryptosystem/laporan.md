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
(Plaintext (Teks Asli)
Pesan awal yang masih bisa dibaca manusia/mesin.
Algoritma + Kunci (Proses Enkripsi & Dekripsi
Algoritma: aturan atau metode matematis yang digunakan untuk mengubah plaintext menjadi ciphertext.
Contoh algoritma: Caesar Cipher, AES, RSA, DES, ChaCha20.
Kunci (Key)
Nilai rahasia yang membuat enkripsi/dekripsi unik.
Tanpa kunci yang benar, ciphertext tidak bisa dibuka.
Misalnya pada Caesar Cipher: jika plaintext = HELLO, kunci = 3, maka hasilnya KHOOR.
Kunci adalah inti dari keamanan: semakin panjang/rumit kunci, semakin sulit ditembus.variabel rahasia yang dipakai oleh algoritma.
Tanpa kunci, pesan tidak bisa dibuka.
Pada algoritma simetris, kunci enkripsi = kunci dekripsi.
Pada algoritma asimetris, kunci enkripsi (public key) ≠ kunci dekripsi (private key).
Ciphertext (Teks Terenkripsi)
Hasil dari enkripsi plaintext menggunakan algoritma + kunci.
Bentuknya tidak bisa dipahami langsung tanpa proses dekripsi.
Contoh (dari Caesar Cipher dengan shift 3):
Plaintext: HELLO
Ciphertext: KHOOR
Proses Enkripsi (Encryption)
Mengubah plaintext → ciphertext dengan algoritma + kunci.
Tujuan: menjaga kerahasiaan data.
Proses Dekripsi (Decryption)
Kebalikan enkripsi. Ciphertext → plaintext menggunakan algoritma + kunci.
Jika kunci salah, hasilnya tidak akan sesuai. 
Proses Dekripsi
Proses kebalikan enkripsi, yaitu mengubah ciphertext → plaintext.
Dilakukan oleh penerima pesan dengan kunci yang sesuai.
Jika kunci salah → hasil dekripsi kacau, tidak sesuai.
Ciphertext: WFMDXN
Kunci: 5
Plaintext hasil dekripsi: RAHASIA
Alur Komunikasi Kriptografi
Pengirim: menulis pesan (plaintext) → dienkripsi dengan algoritma + kunci → ciphertext dikirim.
Penerima: menerima ciphertext → didekripsi dengan algoritma + kunci → kembali menjadi plaintext asli.
Pihak ketiga yang menyadap hanya melihat ciphertext (acak) tanpa bisa membuka isinya.)
---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(<img width="1341" height="694" alt="asli week2" src="https://github.com/user-attachments/assets/dc78961e-5511-4636-ad6e-c9fe2ba6a959" />
)

---

## 5. Source Code
# file: praktikum/week2-cryptosystem/src/simple_crypto.py

def encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - key) % 26 + shift)
        else:
            result += char
    return result

if __name__ == "__main__":
    message = "<nim><nama>"
    key = 5

    enc = encrypt(message, key)
    dec = decrypt(enc, key)

    print("Plaintext :", message)
    print("Ciphertext:", enc)
    print("Decrypted :", dec)

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
Program ini adalah implementasi Caesar Cipher dengan kunci pergeseran (shift).
Enkripsi berhasil mengubah plaintext menjadi ciphertext acak sehingga pesan asli tidak langsung terbaca.
Dekripsi dengan kunci yang sama bisa mengembalikan ciphertext menjadi plaintext.
Ini menunjukkan prinsip dasar kriptografi simetris:
Satu kunci dipakai untuk enkripsi dan dekripsi.
Jika kunci benar → pesan asli dapat dipulihkan dengan sempurna.
Jika kunci salah → hasil dekripsi tidak bermakna.
Hasil eksekusi program Caesar Cipher:
![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Komponen Utama Kriptosistem
Plaintext (Teks Asli)
Pesan atau data awal yang masih bisa dibaca manusia atau diproses komputer tanpa perlindungan.
Contoh: “Password123”, “Transfer Rp 1.000.000”.
Ciphertext (Teks Terenkripsi)
Hasil enkripsi dari plaintext.
Bentuknya acak/tidak bermakna, sehingga orang lain tidak bisa membaca tanpa kunci yang benar.
Contoh: “Xy9#kLm@2”.
Algoritma Kriptografi
Metode matematis yang digunakan untuk melakukan enkripsi dan dekripsi.
Ada dua jenis utama:
Algoritma Simetris (kunci enkripsi = kunci dekripsi) → Contoh: AES, DES.
Algoritma Asimetris (kunci enkripsi ≠ kunci dekripsi) → Contoh: RSA, ECC.
Kunci (Key)
Data rahasia yang dipakai oleh algoritma untuk mengubah plaintext ↔ ciphertext.
Kunci memastikan hasil enkripsi berbeda walaupun algoritmanya sama.
Panjang/kompleksitas kunci menentukan tingkat keamanan.
Proses Enkripsi
Transformasi plaintext menjadi ciphertext dengan algoritma + kunci.
Dilakukan oleh pengirim untuk menjaga kerahasiaan pesan.
Proses Dekripsi
Transformasi ciphertext kembali menjadi plaintext menggunakan algoritma + kunci.
Dilakukan oleh penerima agar pesan bisa dibaca kembali.
- Pertanyaan 2: Kriptografi Simetris

enkripsi dan dekripsi menggunakan kunci yang sama.
 Contoh algoritma: AES, DES, Blowfish.
 Kelebihan:
Lebih cepat & efisien → cocok untuk enkripsi data dalam jumlah besar (misalnya file, database).
Lebih sederhana → algoritma lebih ringan dan mudah diimplementasikan.
Lebih sedikit kebutuhan komputasi → tidak memerlukan operasi matematika yang berat seperti bilangan prima besar.
Kelemahan:
Distribusi kunci sulit → bagaimana cara mengirim kunci ke penerima secara aman tanpa disadap?
Kurang aman bila kunci bocor → siapa pun yang tahu kunci bisa enkripsi & dekripsi semua pesan.
Tidak cocok untuk komunikasi skala besar (misalnya internet global) karena harus membagikan kunci ke banyak pihak.
Kriptografi Asimetris
Ciri: menggunakan dua kunci berbeda:
Public key (untuk enkripsi, bisa dibagikan).
Private key (untuk dekripsi, rahasia).
Contoh algoritma: RSA, ECC, ElGamal.
Kelebihan:
Distribusi kunci lebih aman → public key bisa dibagikan bebas tanpa takut disadap.
Mendukung digital signature → bisa dipakai untuk otentikasi & integritas pesan.
Lebih cocok untuk sistem terbuka seperti internet.
 Kelemahan:

Lebih lambat → perhitungan matematis kompleks (eksponensial, bilangan prima besar).
Tidak efisien untuk data besar → biasanya hanya dipakai untuk enkripsi kunci (lalu kunci itu dipakai di simetris).
Lebih kompleks dalam implementasi.
pertanyaan 3.
Mengapa Distribusi Kunci Jadi Masalah Utama dalam Kriptografi Simetris?
Satu kunci dipakai untuk enkripsi dan dekripsi
Pada sistem simetris, pengirim dan penerima harus menggunakan kunci yang sama.
Artinya kunci tersebut harus dikirim/dibagikan terlebih dahulu agar komunikasi bisa berjalan.
Risiko penyadapan saat pengiriman kunci
Jika kunci dikirim lewat jaringan (misalnya internet), ada kemungkinan pihak ketiga menyadap kunci.
Jika kunci berhasil dicuri, maka semua pesan (lampau maupun masa depan) bisa dibaca oleh penyadap.
Kesulitan pada komunikasi banyak pihak
Untuk komunikasi antara banyak orang, jumlah kunci yang harus dikelola menjadi sangat besar.
Misalnya, jika ada 100 orang yang ingin saling bertukar pesan rahasia, dibutuhkan ratusan kunci berbeda.
Tidak ada cara aman bawaan untuk distribusi kunci
Algoritma simetris sendiri tidak menyediakan mekanisme aman untuk membagikan kunci.
Dibutuhkan metode tambahan, misalnya menggunakan kurir, saluran aman, atau bantuan kriptografi asimetris.
Contoh Nyata
Kamu ingin mengirim pesan rahasia ke teman dengan AES (simetris).
Kamu perlu memberikan kunci rahasia ke temanmu.
Pertanyaannya: bagaimana kamu mengirim kunci itu?
Kalau lewat WhatsApp/Email → bisa saja disadap.
Kalau lewat telepon → juga bisa disadap.
Jika penyadap berhasil dapat kuncinya → semua pesan bisa dibuka.

---

## 8. Kesimpulan
(Fungsi encrypt(plaintext, key)
Mengambil setiap karakter pada plaintext.
Jika huruf (isalpha()), maka dilakukan pergeseran dengan kunci (key) sesuai aturan Caesar Cipher.
shift = 65 untuk huruf kapital (A–Z), 97 untuk huruf kecil (a–z).
Operasi (ord(char) - shift + key) % 26 + shift membuat huruf bergeser sesuai kunci dalam alfabet.
Jika bukan huruf (angka, spasi, simbol), karakter tetap sama.
Fungsi decrypt(ciphertext, key)
Proses kebalikan enkripsi.
Menggeser huruf ke arah kiri dengan kunci yang sama.
Dengan cara ini ciphertext bisa kembali ke plaintext semula.
Main Program
message = "<nim><nama>" → ini adalah teks yang akan dienkripsi (nanti bisa diganti dengan nim & nama kamu).
key = 5 → kunci enkripsi/dekripsi.
enc = encrypt(message, key) → hasil enkripsi (ciphertext).
dec = decrypt(enc, key) → hasil dekripsi kembali jadi plaintext.
Program akan menampilkan:)
Plaintext : <nim><nama>
Ciphertext: <hasil enkripsi>
Decrypted : <nim><nama>

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
