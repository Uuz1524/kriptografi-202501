# Laporan Praktikum Kriptografi
Minggu ke-: 14
Topik: [Analisis Serangan Kriptografi]  
Nama: [Uswatun Khasanah]  
NIM: [230202782]  
Kelas: [5 IKKA]  

---

## 1. Tujuan
(Mengidentifikasi jenis serangan pada sistem informasi nyata.
Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.)

---

## 2. Dasar Teori
Identifikasi Serangan
(Pada tahun 2012, database LinkedIn bocor berisi sekitar 117 juta password pengguna.
Masalah utamanya: LinkedIn saat itu masih menggunakan hash MD5 tanpa salt.
MD5 adalah algoritma hash lama yang sangat cepat → cocok untuk penyerang melakukan brute force.
Serangannya Terjadi karena Hacker mendapatkan file database berisi hash MD5.
Karena:MD5 cepat dihitung Tidak memakai saltHacker menggunakan: Rainbow tableDictionary attackGPU untuk brute force
Dalam waktu singkat, jutaan password berhasil dikembalikan ke bentuk aslinya.
dampaknya:Akun LinkedIn diambil alih
Password yang sama dipakai di email, bank, media sosial → banyak akun lain ikut dibobol
Kerugian reputasi besar bagi LinkedIn

Evaluasi Kelemahan Sistem
Penggunaan algoritma hash yang sudah usang
LinkedIn masih menggunakan MD5, padahal saat itu MD5 sudah dikenal lemah dan mudah di-brute force menggunakan GPU.
Tidak menggunakan salt
Password yang sama menghasilkan hash yang sama. Ini memudahkan penyerang memakai rainbow table dan dictionary attack.
Kecepatan hash terlalu tinggiMD5 sangat cepat dihitung sehingga jutaan kombinasi password bisa dicoba hanya dalam hitungan detik.
Tidak ada perlindungan lanjutan setelah kebocoran
Sistem tidak mampu mendeteksi bahwa hash database telah bocor sebelum digunakan penyerang
Ketergantungan pada sistem lama (legacy system)
Tidak dilakukan migrasi cepat ke standar keamanan terbaru.
Kelemahan pada algoritma kriptografi
Ya, ada kelemahan.
LinkedIn menggunakan MD5, yaitu algoritma hash yang sudah terbukti tidak aman dan sangat cepat di-brute force.
Kelemahan pada implementasi
Ada juga Walaupun MD5 sudah lemah, kesalahan makin fatal karena:
Tidak menggunakan saltTidak memakai password hashing khusus seperti bcrypt atau Argon2Ini menunjukkan cara penerapan kriptografi sangat buruk.
Kelemahan pada konfigurasi sistem
Juga ada Sistem tidak memiliki:Deteksi kebocoran database Kebijakan keamanan seperti pemantauan akses mencurigakan dan perlindungan ekstra setelah insiden.

Jelaskan alasan pemilihan algoritma dan dampaknya terhadap keamanan sistem.
LinkedIn memilih MD5 karena:Cepat diproses → tidak membebani serverMudah diimplementasikanPopuler pada masanya → dulu dianggap cukup aman Cocok untuk sistem besar dengan jutaan penggunaNamun, seiring berkembangnya teknologi, alasan ini justru menjadi sumber kelemahan.

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
Kronologi Insiden

Timeline:

Juni 2012:
  - 5 Juni: File berisi 6.5 juta LinkedIn password hashes muncul di forum hacker Rusia
  - Hash dalam format SHA-1 (tanpa salt)
  - Sebagian hash sudah di-crack dan diganti dengan "00000"
  
  - 6 Juni: LinkedIn mengonfirmasi breach
  - Notifikasi ke affected users
  - Force password reset untuk compromised accounts
  
2016 (Update):
  - Mei 2016: Hacker menjual 167 juta LinkedIn credentials di dark web
  - Terungkap bahwa breach 2012 lebih besar dari yang dilaporkan
  - Data mencakup email addresses dan hashed passwords
  
  - Harga: 5 Bitcoin (~$2,200 saat itu)

Dampak:

    Immediate: 6.5 juta accounts compromised
    Total (2016 revelation): 167 juta credentials exposed
    User trust damaged
    Legal consequences dan class-action lawsuit
    Reputasi LinkedIn terdampak

5.2 Vektor Serangan

Metode Breach:

Tahap 1: Initial Compromise
  Attacker mendapat akses ke LinkedIn database
  Metode: SQL Injection atau compromised credentials (tidak dikonfirmasi)
  
Tahap 2: Data Exfiltration
  Download database berisi:
    - User emails
    - Password hashes (SHA-1)
    - Profile information
  
Tahap 3: Hash Cracking
  Attacker menggunakan:
    - GPU-accelerated cracking (HashCat, John the Ripper)
    - Dictionary attacks
    - Brute force untuk short passwords
  
Tahap 4: Distribution
  2012: Publish 6.5M hashes di forum (free)
  2016: Sell 167M credentials di dark web

Kelemahan yang Dieksploitasi:

    SHA-1 tanpa Salt

    Password: "password123"
    SHA-1 Hash: 482c811da5d5b4bc6d497ffa98491e38

    Problem:
      - Semua user dengan "password123" memiliki hash yang sama
      - Rainbow tables efektif
      - Parallel cracking efficient

    Tidak Ada Key Stretching

    SHA-1 sangat cepat:
      - Modern GPU: 8-10 billion SHA-1/second
      - Dapat try semua 8-character passwords dalam minutes

    Weak Passwords

    Top cracked passwords:
      1. password
      2. 123456
      3. linkedin
      4. 123456789
      5. password1

    Millions of users menggunakan passwords ini

5.3 Analisis Kelemahan Kriptografi

Problem 1: SHA-1 sebagai Password Hash

SHA-1 dirancang untuk kecepatan, bukan keamanan password:

Karakteristik SHA-1:
  - Purpose: Data integrity, digital signatures
  - Speed: 500+ MB/s pada CPU modern
  - Cost: Constant time (tidak adjustable)
  
Untuk password hashing:
  Kecepatan = BURUK
  Attacker dapat try billions kombinasi per detik

Simulasi Cracking Speed:

import hashlib
import time

def sha1_hash(password):
    return hashlib.sha1(password.encode()).hexdigest()

# Benchmark cracking speed
start = time.time()
attempts = 0
target_hash = sha1_hash("password123")

# Dictionary attack simulation
common_passwords = ["password", "123456", "password123", "linkedin"]

for pwd in common_passwords:
    attempts += 1
    if sha1_hash(pwd) == target_hash:
        print(f"Password found: {pwd}")
        print(f"Attempts: {attempts}")
        break

end = time.time()
print(f"Time: {end - start} seconds")

Output:

Password found: password123
Attempts: 3
Time: 0.0001 seconds

Analisis:

Single CPU core: 1 million SHA-1/second
Modern GPU (RTX 4090): 10 billion SHA-1/second

8-character lowercase password:
  Keyspace: 26^8 = 208 billion
  GPU time: 208B / 10B = 20.8 seconds
  
8-character alphanumeric:
  Keyspace: 62^8 = 218 trillion
  GPU time: 218T / 10B = 6 hours
  
Reality: Most users use weak passwords
Dictionary attack cracks 50%+ dalam minutes

Problem 2: Tidak Ada Salt

Scenario tanpa salt:

Database:
  user1@email.com: 482c811da5d5b4bc6d497ffa98491e38
  user2@email.com: 482c811da5d5b4bc6d497ffa98491e38
  user3@email.com: 5f4dcc3b5aa765d61d8327deb882cf99
  user4@email.com: 482c811da5d5b4bc6d497ffa98491e38

Observation:
  - user1, user2, user4 memiliki hash sama
  - Berarti password sama
  - Crack satu = crack semua
  
Attacker strategy:
  1. Identifikasi hash yang paling sering
  2. Fokus cracking pada hash tersebut
  3. Satu crack = thousands accounts

Rainbow Table Attack:

Rainbow Table: Pre-computed hash → password mapping

Example (simplified):
  SHA1("password")  = 5baa61e4c...
  SHA1("123456")    = 7c4a8d09c...
  SHA1("linkedin")  = 9d4e1e23b...
  
Storage: 100GB untuk 1 billion passwords
Lookup: Instant (hash table)

LinkedIn hashes:
  Load 6.5M hashes ke memory
  Lookup di rainbow table
  Crack rate: 90%+ dalam minutes
  
Defense: Salt makes rainbow tables useless
(Setiap salt memerlukan rainbow table terpisah)

Problem 3: Tidak Ada Iterasi (Key Stretching)

Single SHA-1 iteration:
  Password → SHA1() → Hash
  Time: 0.000001 seconds
  
Key stretching (bcrypt example):
  Password → bcrypt(cost=12) → Hash
  Time: 0.3 seconds (300,000x slower)
  
Impact:
  Attacker speed: 10B hashes/s → 33,000 hashes/s
  Reduction: 300,000x
  
  8-char alphanumeric:
    SHA-1: 6 hours
    bcrypt: 20,000 years

5.4 Simulasi Serangan

Source Code: LinkedIn Hash Cracking Simulation

import hashlib
import time
from typing import List, Tuple

def sha1_hash(password: str) -> str:
    """
    Simulasi hashing LinkedIn (SHA-1 tanpa salt)
    """
    return hashlib.sha1(password.encode()).hexdigest()

def load_common_passwords(filename: str = "common_passwords.txt") -> List[str]:
    """
    Load common passwords untuk dictionary attack
    """
    # Simulasi common passwords (dalam real attack, gunakan rockyou.txt)
    common_passwords = [
        "password", "123456", "123456789", "password123",
        "linkedin", "welcome", "qwerty", "abc123",
        "monkey", "1234567890", "princess", "letmein",
        "dragon", "iloveyou", "sunshine", "master",
        "admin", "login", "solo", "trustno1"
    ]
    return common_passwords

def dictionary_attack(target_hashes: List[str], 
                     dictionary: List[str]) -> Tuple[dict, int, float]:
    """
    Simulasi dictionary attack terhadap LinkedIn hashes
    
    Returns:
        (cracked_passwords, total_attempts, time_elapsed)
    """
    cracked = {}
    attempts = 0
    start_time = time.time()
    
    for password in dictionary:
        hash_value = sha1_hash(password)
        attempts += 1
        
        if hash_value in target_hashes:
            cracked[hash_value] = password
            print(f"Cracked: {password} → {hash_value}")
    
    elapsed = time.time() - start_time
    return cracked, attempts, elapsed

def brute_force_numeric(target_hashes: List[str], 
                       max_length: int = 6) -> Tuple[dict, int, float]:
    """
    Simulasi brute force untuk numeric passwords
    """
    cracked = {}
    attempts = 0
    start_time = time.time()
    
    # Brute force 6-digit numbers (000000-999999)
    for num in range(10 ** max_length):
        password = str(num).zfill(max_length)
        hash_value = sha1_hash(password)
        attempts += 1
        
        if hash_value in target_hashes:
            cracked[hash_value] = password
            print(f"Cracked: {password} → {hash_value}")
        
        # Progress indicator
        if attempts % 100000 == 0:
            print(f"Progress: {attempts:,} attempts")
    
    elapsed = time.time() - start_time
    return cracked, attempts, elapsed

def analyze_hash_distribution(hashes: List[str]) -> dict:
    """
    Analisis distribusi hash untuk identifikasi password umum
    """
    distribution = {}
    for hash_value in hashes:
        distribution[hash_value] = distribution.get(hash_value, 0) + 1
    
    # Sort by frequency
    sorted_dist = sorted(distribution.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_dist)

# Simulasi LinkedIn Breach
if __name__ == "__main__":
    print("=" * 70)
    print("SIMULASI LINKEDIN PASSWORD BREACH (2012)")
    print("=" * 70)
    # Simulasi LinkedIn database (sample hashes)
    print("\n[1] Generating simulated LinkedIn hashes...")
    linkedin_passwords = [
        "password", "123456", "linkedin", "password123",
        "welcome", "123456", "password", "admin",
        "123456789", "qwerty", "password", "login"
    ]
    linkedin_hashes = [sha1_hash(pwd) for pwd in linkedin_passwords]
    print(f"Total hashes in database: {len(linkedin_hashes)}")
    print(f"Unique hashes: {len(set(linkedin_hashes))}")
    # Analisis distribusi
    print("\n[2] Analyzing hash distribution...")
    distribution = analyze_hash_distribution(linkedin_hashes)
    print("\nTop 5 most common hashes:")
    for i, (hash_val, count) in enumerate(list(distribution.items())[:5], 1):
        print(f"  {i}. {hash_val[:16]}... (appears {count} times)")
    # Dictionary attack
    print("\n[3] Launching dictionary attack...")
    common_passwords = load_common_passwords()
    cracked_dict, dict_attempts, dict_time = dictionary_attack(
        linkedin_hashes, common_passwords
    )
    print(f"\nDictionary Attack Results:")
    print(f"  Passwords cracked: {len(cracked_dict)}")
    print(f"  Total attempts: {dict_attempts:,}")
    print(f"  Time elapsed: {dict_time:.4f} seconds")
    print(f"  Speed: {dict_attempts/dict_time:,.0f} hashes/second")
    # Brute force numeric
    print("\n[4] Launching brute force (numeric 6-digit)...")
    print("(This will try 1,000,000 combinations)")
    user_input = input("Continue? (y/n): ")
    if user_input.lower() == 'y':
        cracked_brute, brute_attempts, brute_time = brute_force_numeric(
            linkedin_hashes, max_length=6
        )
        print(f"\nBrute Force Results:")
        print(f"  Passwords cracked: {len(cracked_brute)}")
        print(f"  Total attempts: {brute_attempts:,}")
        print(f"  Time elapsed: {brute_time:.4f} seconds")
        print(f"  Speed: {brute_attempts/brute_time:,.0f} hashes/second")
    # Summary
    print("\n" + "=" * 70)
    print("ATTACK SUMMARY")
    print("=" * 70)
    total_cracked = len(set(list(cracked_dict.keys())))
    total_hashes = len(set(linkedin_hashes))
    crack_rate = (total_cracked / total_hashes) * 100
    print(f"Total unique hashes: {total_hashes}")
    print(f"Successfully cracked: {total_cracked} ({crack_rate:.1f}%)")
    print(f"\nCracked passwords:")
    for hash_val, password in cracked_dict.items():
        count = distribution.get(hash_val, 0)
        print(f"  {password:15} → affects {count} accounts")
    print("\n" + "=" * 70)
    print("VULNERABILITY ANALYSIS")
    print("=" * 70)
    print("\nIdentified Weaknesses:")
    print("  1. SHA-1 hashing (fast, designed for speed)")
    print("  2. No salt (identical passwords = identical hashes)")
    print("  3. No key stretching (single iteration)")
    print("  4. Weak password policy (common passwords allowed)")
    print("\nReal-world Impact:")
    print("  - With modern GPU: 10 billion SHA-1/second")
    print("  - Dictionary of 1 billion passwords: < 1 second")
    print("  - 8-character brute force: minutes to hours")
    print("  - Rainbow tables: instant lookup")

## 6. Hasil dan Pembahasan

<img width="958" height="591" alt="image" src="https://github.com/user-attachments/assets/ff102125-a4fb-4e62-9da4-2c07a255276f" />



<img width="837" height="578" alt="image" src="https://github.com/user-attachments/assets/b21c8e23-4ff6-4354-b1a5-3666560e6631" />


## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Karena pada saat sistem itu dibuat, standar keamanannya masih rendah dibandingkan kondisi sekarang.
Penyebab utamanya: Penyebab	Penjelasan
Panjang password pendek	Dulu password 6–8 karakter sudah dianggap aman
Tidak ada pembatasan login	Bisa mencoba ribuan kali tanpa diblokir
Hash lama (MD5, SHA-1)	Hash ini cepat dihitung → mudah di-crack
Tidak menggunakan salt	Password sama menghasilkan hash sama
Perangkat lama	Server lama tidak mendukung algoritma modern
Akibatnya,
satu file database bocor saja bisa dipecahkan hanya dalam hitungan menit.
- Pertanyaan 2: Kelemahan algoritma terjadi jika algoritma kriptografinya sendiri sudah tidak aman. Walaupun dipakai dengan benar, tetap bisa dibobol. Contohnya MD5 atau DES. Solusinya: ganti algoritmanya.
Kelemahan implementasi terjadi jika algoritma sebenarnya aman, tetapi cara penggunaannya salah. Contohnya AES tapi password lemah, kunci disimpan di kode, atau tidak ada batas percobaan login. Solusinya: perbaiki cara penerapannya.
Pertanyaan 3: Selalu memperbarui algoritma dan standar keamanan
Gunakan algoritma yang masih direkomendasikan seperti AES-256, RSA minimal 2048 bit, atau ECC. Untuk password gunakan hashing modern seperti bcrypt, scrypt, atau Argon2.
Melakukan audit dan pengujian keamanan secara berkala
Sistem harus dicek rutin melalui penetration testing dan vulnerability scanning untuk menemukan celah sejak dini.
Mengamankan proses autentikasi pengguna
Terapkan password kuat, batasi percobaan login, dan aktifkan multi-factor authentication (MFA).
Melatih pengembang dan pengguna
Pengembang harus paham cara implementasi kriptografi yang benar, dan pengguna diedukasi agar tidak memakai password lemah.
Pertanyaan 1: Mengapa banyak sistem lama masih rentan terhadap brute force atau dictionary attack?

Banyak sistem lama masih rentan karena beberapa faktor:

1. Legacy Systems dan Technical Debt

Skenario:
  System dikembangkan 10-15 tahun lalu
  Password hashing: MD5 atau SHA-1
  
Challenges mengupgrade:
  - Breaking changes (format hash berbeda)
  - Database migration kompleks
  - Millions of existing user records
  - Downtime tidak acceptable
  - Cost vs benefit analysis
  
Example: LinkedIn (founded 2003)
  2003-2012: SHA-1 tanpa salt
  2012: Breach terjadi
  2012-2016: Migration ke bcrypt
  Impact: 9 years dengan vulnerable system

2. Backward Compatibility

Problem:
  Changing password hash algorithm = breaking change
  
  Old system:
    Login: SHA-1(input) == stored_SHA1_hash
  
  New system:
    Login: bcrypt.verify(input, stored_bcrypt_hash)
  
  Migration requires:
    - User re-enter password (tidak ada plaintext)
    - Force password reset (bad UX)
    - Gradual migration (dual hash storage)
    
  Companies prioritize:
    User experience > security (unfortunately)
    Availability > security updates

3. Lack of Security Awareness

Common misconceptions:

"SHA-256 is secure, right?"
  - SHA-256 aman untuk digital signatures
  - TIDAK aman untuk passwords (terlalu cepat)
  - Speed = vulnerability untuk password hashing
  
"We have firewall, database won't be breached"
  - Defense in depth ignored
  - Single point of failure
  - Breach still happens (SQL injection, insider threat)
  
"Nobody will attack us, we're small"
  - Automated attacks tidak diskriminasi
  - Credential stuffing attacks target everyone
  - Dark web marketplaces untuk stolen credentials

4. Cost Considerations

Migration Cost Analysis:

Direct Costs:
  - Developer time (design + implement + test)
  - Database migration scripts
  - Server downtime
  - User support (password reset helpdesk)
  
Indirect Costs:
  - User frustration (force reset)
  - Potential user loss
  - Training untuk support staff
  
Estimated: $100K - $500K untuk large platform

Management decision:
  "We haven't been breached yet, why spend now?"
  
Reality:
  Cost of breach: $3.86 million average (IBM 2020)
  Prevention >>> Remediation

5. Password Reuse Across Services

User behavior:
  - 59% reuse passwords (Google 2019)
  - Breach pada one service → credentials tried on others
  
Credential Stuffing:
  1. Attacker obtains LinkedIn breach credentials
  2. Try same email+password on:
     - Banks
     - Email providers
     - E-commerce sites
     - Social media
  3. 0.1% - 2% success rate (still millions of accounts)
  
Defense:
  - Cannot control user behavior
  - Can only make our hashes harder to crack
  - Slows down attacker progress

6. Weak Password Policies

Old policies (ineffective):
  - Minimum 6 characters
  - No complexity requirements
  - Allow common passwords ("password", "123456")
  - No breach database check
  
Result:
  40% users choose passwords from top 10,000 most common
  
Modern policies (effective):
  - Minimum 12 characters (15+ recommended)
  - Check against breach databases (Have I Been Pwned)
  - No common passwords
  - Password strength meter
  - Encourage passphrases

7. Regulatory and Compliance Lag

Regulations often lag behind threats:

GDPR (2018): Strong data protection
  - But tidak specify password hashing algorithms
  - "Appropriate security measures" (vague)
  
PCI DSS (Payment Card Industry):
  - Requires salted hashes
  - Tidak specify algorithm (bcrypt vs SHA-256)
  
NIST (US):
  - 2017: Deprecated password complexity rules
  - Recommended: Length > complexity
  - Recommended: Check breach databases
  
Industry moves slow:
  - Guidelines take years to update
  - Companies wait untuk compliance mandate
  - Proactive security rare

8. False Sense of Security

"We encrypt passwords"
  - Encryption ≠ Hashing
  - Encryption reversible (with key)
  - Hashing one-way (proper approach)
  
"We use SHA-256"
  - SHA-256 lebih baik dari MD5
  - Tapi still tidak untuk passwords (too fast)
  - bcrypt/Argon2 specifically designed untuk passwords
  
"We have SSL/TLS"
  - Transport security ≠ storage security
  - TLS protects in transit
  - Hashing protects at rest
  - Both needed (defense in depth)

Solutions:

1. Gradual Migration:
   - Implement bcrypt untuk new accounts
   - Rehash existing pada login (opportunistic)
   - After 6-12 months: force reset untuk remaining
   
2. Dual Hash Storage (transition):
   db.users:
     - password_hash_sha1 (deprecated)
     - password_hash_bcrypt (new)
     - migration_status (pending/completed)
   
   Login flow:
     if user.migration_status == 'pending':
       if verify_sha1(input, user.password_hash_sha1):
         # Rehash dengan bcrypt
         user.password_hash_bcrypt = bcrypt.hash(input)
         user.migration_status = 'completed'
         return success
   
3. Security Awareness:
   - Developer training (secure coding)
   - Management buy-in (cost-benefit)
   - Regular security audits
   - Penetration testing
   
4. Proactive Security:
   - Don't wait untuk breach
   - Implement defense in depth
   - Stay updated dengan best practices
   - Monitor security advisories

Kesimpulan:

Sistem lama rentan karena kombinasi technical debt, backward compatibility concerns, cost considerations, dan lack of security awareness. Solusi memerlukan gradual migration strategy, management support, dan proactive security mindset. Breach seperti LinkedIn membuktikan bahwa cost of prevention << cost of remediation.

Pertanyaan 2: Apa bedanya kelemahan algoritma dengan kelemahan implementasi?

Perbedaan fundamental antara algorithm weakness vs implementation weakness:

1. Kelemahan Algoritma (Cryptographic Weakness)

Definisi:

Kelemahan intrinsik dalam desain algoritma kriptografi
Tidak peduli seberapa baik implementasi, kelemahan tetap ada
Fundamental flaw yang tidak dapat diperbaiki tanpa mengganti algoritma

Contoh: MD5 Hash Function

Algoritma: MD5 (Message Digest 5)
Designed: 1991 by Ron Rivest
Purpose: Cryptographic hash function

Kelemahan Algoritma:
  1. Collision vulnerability
     - Menemukan dua input berbeda dengan hash sama
     - First collision: 2004 (researchers)
     - Practical collision: 2008 (dapat dilakukan < 1 menit)
     
  2. Preimage attack
     - Complexity: 2^123 operations (theoretically)
     - Below 2^128 (MD5 output size)
     - Tidak practical tapi better than brute force
     
  3. Mathematical weakness
     - Flaws dalam internal structure
     - Differential cryptanalysis efektif

Demonstration:

import hashlib

def md5_collision_demo():
    """
    Demonstrasi kelemahan MD5
    (menggunakan known collision dari penelitian)
    """
    # Two different inputs dengan MD5 hash sama (collision)
    input1 = bytes.fromhex("d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f89...")
    input2 = bytes.fromhex("d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f89...")
    
    hash1 = hashlib.md5(input1).hexdigest()
    hash2 = hashlib.md5(input2).hexdigest()
    
    print(f"Input 1 hash: {hash1}")
    print(f"Input 2 hash: {hash2}")
    print(f"Collision: {hash1 == hash2}")
    print(f"Inputs same: {input1 == input2}")
    
    # Result: Same hash, different inputs
    # Algorithm weakness: collision possible

Impact:

Digital Signatures:
  - Attacker dapat create malicious document dengan hash sama
  - Valid signature dari legitimate document dapat transferred
  - Fraud/forgery possible
  
Certificate Authorities:
  - 2008: Rogue CA certificate created (MD5 collision)
  - Could issue fake SSL certificates
  - MITM attacks pada HTTPS
  
Conclusion:
  MD5 fundamentally broken
  No amount of good implementation dapat fix
  Must use different algorithm (SHA-256, SHA-3)

Contoh Lain: DES (Data Encryption Standard)

Algoritma: DES
Key size: 56 bits

Kelemahan Algoritma:
  1. Key space too small
     - 2^56 = 72 quadrillion keys
     - 1998: DES cracked dalam 56 hours (EFF DES Cracker)
     - 2008: COPACOBANA cracked dalam < 1 day
     - Modern: dapat cracked dalam hours
  
  2. Linear cryptanalysis
     - Theoretical attack requiring 2^43 known plaintexts
     - Practical dalam certain scenarios
  
  3. Differential cryptanalysis
     - Dapat find key dengan 2^47 chosen plaintexts

Solution:
  - Triple-DES (3DES) - band-aid fix
  - AES - modern replacement (128/192/256 bit keys)

2. Kelemahan Implementasi (Implementation Vulnerability)

Definisi:

Algoritma secara kriptografis aman
Tetapi implementasi software/hardware memiliki flaws
Dapat diperbaiki tanpa mengganti algoritma

Contoh 1: Heartbleed (OpenSSL)

Algoritma: TLS/SSL (aman)
Implementation: OpenSSL library
Bug: CVE-2014-0160 (Heartbleed)

Vulnerability:
  TLS Heartbeat extension
  Missing bounds check pada memcpy()
  
Code (simplified):
  void process_heartbeat(char *request) {
    int payload_length = *(int*)request;  // attacker-controlled
    char *payload = request + 4;
    
    // BUG: tidak validate payload_length
    char *response = malloc(payload_length);
    memcpy(response, payload, payload_length);  // buffer over-read
    
    send_heartbeat_response(response);
  }

Attack:
  Attacker sends: payload_length = 64KB, actual payload = 1 byte
  Server reads beyond buffer
  Returns 64KB of memory (including secrets):
    - Private keys
    - Session tokens
    - Passwords
    - Other user data

Impact:
  - Millions of servers vulnerable
  - Private key theft possible
  - HTTPS compromised
  
Fix:
  Add bounds check:
  if (payload_length > actual_payload_size)
    return error;
  
Algorithm: Still secure (TLS/SSL)
Implementation: Fixed dalam OpenSSL 1.0.1g

Contoh 2: Debian OpenSSL Weak Key Generation

Algoritma: RSA (aman)
Implementation: Debian/Ubuntu OpenSSL package (2006-2008)

Bug:
  Developer commented out crucial entropy source
  Untuk fix Valgrind warning (uninitialized memory)
  
Original code:
  MD_Update(&m, buf, j);  // buf contains random data
  
Modified code (buggy):
  // MD_Update(&m, buf, j);  // commented out
  MD_Update(&m, buf, 0);      // zero randomness!

Impact:
  Random number generator only uses:
    - Process ID (PID): 15 bits entropy
  
  Total entropy: 15 bits instead of 128+ bits
  Keyspace: 2^15 = 32,768 possible keys
  
  All SSH/TLS keys generated 2006-2008 predictable:
    - Can enumerate all possible keys
    - Can crack dalam minutes
    
Fix:
  Restore original code
  Regenerate all affected keys
  
Algorithm: RSA still secure
Implementation: Human error dalam code modification

Contoh 3: Timing Attacks

Algoritma: AES (aman)
Implementation: Naive comparison function

Vulnerable code:
  def verify_password(stored_hash, input_hash):
    if len(stored_hash) != len(input_hash):
      return False
    
    for i in range(len(stored_hash)):
      if stored_hash[i] != input_hash[i]:
        return False  # EARLY RETURN
    
    return True

Attack:
  Measure response time
  
  Input "A" vs "XXXXXXX":
    - First byte wrong
    - Returns immediately (fast)
  
  Input "H" vs "HXXXXXX":
    - First byte correct, second wrong
    - Takes longer (slower)
  
  Attacker learns:
    - First byte is "H"
    - Repeat untuk setiap posisi
    - Leak entire hash character-by-character

Fix (constant-time comparison):
  def verify_password_safe(stored_hash, input_hash):
    if len(stored_hash) != len(input_hash):
      return False
    
    result = 0
    for i in range(len(stored_hash)):
      result |= ord(stored_hash[i]) ^ ord(input_hash[i])
    
    return result == 0  # Always checks all bytes

Algorithm: Still secure
Implementation: Fixed timing leak

3. Perbandingan Kelemahan
Aspect 	Kelemahan Algoritma 	Kelemahan Implementasi
Root Cause 	Cryptographic design flaw 	Programming/configuration error
Scope 	All implementations affected 	Specific software/version
Fix 	Replace algorithm 	Patch/update software
Examples 	MD5 collision, DES small keysize 	Heartbleed, Debian weak keys
Detection 	Cryptanalysis research 	Penetration testing, code audit
Severity 	Fundamental, permanent 	Fixable, temporary
Timeline 	Often discovered years after release 	Can be introduced anytime

4. LinkedIn Case Analysis

Kelemahan Algoritma:

SHA-1 untuk password hashing:
  - Algoritma designed untuk speed
  - 10 billion hashes/second pada GPU
  - Collision found (2017 SHAttered attack)
  
Not technically broken untuk password hashing
But inappropriate choice (too fast)

Recommendation:
  Use algorithm designed untuk password hashing:
    - bcrypt
    - scrypt
    - Argon2

Kelemahan Implementasi:

LinkedIn SHA-1 implementation:
  1. No salt
     - Implementation decision, bukan algoritma limitation
     - SHA-1 dapat use salt (proper implementation)
     
  2. No key stretching
     - Single iteration
     - Could have implemented multiple iterations
     
  3. Weak password policy
     - Allowed common passwords
     - Implementation/policy issue

These are IMPLEMENTATION failures
Same algorithm (SHA-1) dapat implemented lebih baik:
  - Add unique salt per user
  - Multiple iterations (10,000+)
  - Still suboptimal, tapi significantly better

5. Real-world Implications

Algoritma Weakness:

Once algorithm broken:
  - ALL implementations vulnerable
  - Cannot patch/update
  - Must migrate to new algorithm
  
Example: MD5
  - 2004: Collision found
  - 2025: Still broken
  - No future fixes possible
  - Migration to SHA-256/SHA-3 only solution

Implementation Weakness:

Can be fixed dengan updates:
  - Patch release
  - Configuration change
  - Code fix
  
Example: Heartbleed
  - 2014: Discovered
  - 2014: Fixed dalam OpenSSL 1.0.1g
  - Servers update → vulnerability gone
  - Algorithm (TLS) remains secure

6. Detection Methods

Algorithm Weakness:

Methods:
  - Cryptanalysis (mathematical analysis)
  - Academic research
  - Collision finding
  - Complexity analysis
  
Timeline:
  - Often takes years to discover
  - Peer review process
  - Published papers
  
Examples:
  - MD5: 13 years (1991 release → 2004 collision)
  - SHA-1: 16 years (2001 → 2017 practical collision)

Implementation Weakness:

Methods:
  - Code review
  - Penetration testing
  - Fuzzing
  - Static analysis tools
  - Runtime monitoring
  
Timeline:
  - Can be found immediately or years later
  - Depends on testing thoroughness
  
Examples:
  - Heartbleed: 2 years (2012 introduced → 2014 discovered)
  - Debian weak keys: 2 years in production

Kesimpulan:

Kelemahan Algoritma:

    Fundamental flaw dalam cryptographic design
    Affects semua implementations
    Requires algorithm replacement
    Cannot be patched
    Example: MD5 collision, DES small keysize

Kelemahan Implementasi:

    Programming atau configuration error
    Affects specific software/version
    Can be fixed dengan patch/update
    Algorithm remains secure
    Example: Heartbleed, timing attacks, missing salt

LinkedIn menggunakan SHA-1 (inappropriate algorithm) tanpa salt (implementation failure). Kombinasi algorithm choice + implementation flaws = critical vulnerability. Fix requires both: migrate to proper algorithm (bcrypt/Argon2) AND implement correctly (with salt, proper cost factor).

Pertanyaan 3: Bagaimana organisasi dapat memastikan sistem kriptografi mereka tetap aman di masa depan?

Organisasi perlu mengadopsi strategi comprehensive dan proactive untuk menjaga keamanan kriptografi di masa depan:

1. Crypto Agility (Kesiapan Migrasi)

Konsep:

Kemampuan untuk mengganti algoritma kriptografi dengan cepat
Tanpa architectural overhaul

Design Principles:
  - Abstraksi: Separate crypto implementation dari business logic
  - Pluggable: Easy swap algorithms
  - Versioning: Support multiple algorithms simultaneously
  - Migration path: Gradual transition

Implementation:

# BAD: Hardcoded algorithm
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# GOOD: Crypto agility
class PasswordHasher:
    def __init__(self, algorithm='bcrypt', version='v2'):
        self.algorithm = algorithm
        self.version = version
    
    def hash(self, password):
        if self.algorithm == 'bcrypt':
            return self._hash_bcrypt(password)
        elif self.algorithm == 'argon2':
            return self._hash_argon2(password)
        else:
            raise ValueError(f"Unknown algorithm: {self.algorithm}")
    
    def verify(self, password, stored_hash):
        # Parse hash to determine algorithm
        algo, version, hash_value = self._parse_hash(stored_hash)
        
        # Verify dengan appropriate algorithm
        if algo == 'bcrypt':
            return self._verify_bcrypt(password, hash_value)
        elif algo == 'argon2':
            return self._verify_argon2(password, hash_value)
    
    def needs_rehash(self, hashed_password):
        # Check if current parameters masih aman
        # Return True if perlu rehash dengan parameters baru
        pass

2. Regular Security Audits

Audit berkala untuk:
  - Menemukan dan memperbaiki kelemahan
  - Memastikan compliance dengan best practices
  - Mengidentifikasi potensi risiko baru
  
Frekuensi:
  - Setiap 6 bulan sekali
  - Setelah setiap insiden keamanan
  - Setelah perubahan besar pada sistem
  
Tim audit:
  - Internal security team
  - External security consultant (annual)

3. Penetration Testing

Uji coba penetrasi rutin untuk:
  - Mensimulasikan serangan nyata
  - Mengidentifikasi dan mengeksploitasi kelemahan
  
Frekuensi:
  - Setiap tahun sekali
  - Setelah setiap insiden keamanan besar
  - Setelah perubahan arsitektur atau teknologi utama
  
Tim penetration testing:
  - Tim internal terlatih
  - Vendor eksternal (certified)

4. Keamanan Berlapis (Defense in Depth)

Implementasi beberapa lapisan keamanan:
  - Firewall dan IDS/IPS
  - Enkripsi data (in transit dan at rest)
  - Segmentasi jaringan
  - Least privilege access control
  - Regular patching dan updates
  
Tujuan:
  - Mengurangi risiko dan dampak dari serangan
  - Menyulitkan attacker untuk mendapatkan akses atau bergerak lateral

5. Kebijakan Password yang Kuat

Kebijakan password yang direkomendasikan:
  - Minimum 12 karakter, kombinasi huruf besar, huruf kecil, angka, simbol
  - Tidak ada penggunaan password umum atau yang mudah ditebak
  - Penggunaan password manager untuk menyimpan dan menghasilkan password yang kuat
  
Pendidikan pengguna:
  - Pentingnya password yang kuat dan unik
  - Bahaya dari password reuse
  - Cara menggunakan password manager

6. Multi-Factor Authentication (MFA)

Implementasi MFA di semua sistem yang mendukung:
  - Menggunakan aplikasi authenticator (Google Authenticator, Authy)
  - SMS atau email sebagai faktor kedua (jika perlu)
  
Pendidikan pengguna:
  - Pentingnya MFA untuk keamanan tambahan
  - Cara mengatur dan menggunakan MFA

7. Respons Insiden yang Efektif

Rencana respons insiden yang jelas:
  - Deteksi dan analisis insiden
  - Kontainment, eradication, dan recovery
  - Post-incident analysis dan reporting
  
Tim respons insiden:
  - Tim internal terlatih
  - Konsultan eksternal (jika perlu)

8. Pelatihan dan Kesadaran Keamanan

Program pelatihan keamanan untuk semua karyawan:
  - Dasar-dasar keamanan siber
  - Cara mengenali dan melaporkan insiden
  - Praktik terbaik untuk keamanan informasi
  
Frekuensi:
  - Pelatihan awal untuk karyawan baru
  - Pelatihan ulang tahunan untuk semua karyawan

9. Kebijakan dan Prosedur Keamanan yang Jelas

Dokumentasi kebijakan dan prosedur keamanan:
  - Kebijakan penggunaan kata sandi
  - Kebijakan akses dan otorisasi
  - Kebijakan enkripsi dan penyimpanan data
  - Prosedur respons insiden
  
Pemeriksaan dan pembaruan berkala:
  - Kebijakan dan prosedur ditinjau dan diperbarui setiap tahun
  - Setelah setiap insiden keamanan
  - Setelah perubahan besar pada sistem atau organisasi

10. Komitmen Manajemen dan Dukungan Anggaran

Manajemen puncak harus:
  - Memberikan dukungan dan sumber daya yang cukup untuk keamanan
  - Terlibat dalam peninjauan dan pembaruan kebijakan keamanan
  - Mendukung pelatihan dan kesadaran keamanan untuk semua karyawan
  
Anggaran yang memadai untuk:
  - Alat dan teknologi keamanan
  - Pelatihan dan pengembangan keterampilan
  - Audit dan penilaian keamanan eksternal

8. Jawaban Pertanyaan Diskusi

Pertanyaan 1: Mengapa banyak sistem lama masih rentan terhadap brute force atau dictionary attack?

Banyak sistem lama masih rentan karena beberapa faktor:

1. Legacy Systems dan Technical Debt

Skenario:
  System dikembangkan 10-15 tahun lalu
  Password hashing: MD5 atau SHA-1
  
Challenges mengupgrade:
  - Breaking changes (format hash berbeda)
  - Database migration kompleks
  - Millions of existing user records
  - Downtime tidak acceptable
  - Cost vs benefit analysis
  
Example: LinkedIn (founded 2003)
  2003-2012: SHA-1 tanpa salt
  2012: Breach terjadi
  2012-2016: Migration ke bcrypt
  Impact: 9 years dengan vulnerable system

2. Backward Compatibility

Problem:
  Changing password hash algorithm = breaking change
  
  Old system:
    Login: SHA-1(input) == stored_SHA1_hash
  
  New system:
    Login: bcrypt.verify(input, stored_bcrypt_hash)
  
  Migration requires:
    - User re-enter password (tidak ada plaintext)
    - Force password reset (bad UX)
    - Gradual migration (dual hash storage)
    
  Companies prioritize:
    User experience > security (unfortunately)
    Availability > security updates

3. Lack of Security Awareness

Common misconceptions:

"SHA-256 is secure, right?"
  - SHA-256 aman untuk digital signatures
  - TIDAK aman untuk passwords (terlalu cepat)
  - Speed = vulnerability untuk password hashing
  
"We have firewall, database won't be breached"
  - Defense in depth ignored
  - Single point of failure
  - Breach still happens (SQL injection, insider threat)
  
"Nobody will attack us, we're small"
  - Automated attacks tidak diskriminasi
  - Credential stuffing attacks target everyone
  - Dark web marketplaces untuk stolen credentials

4. Cost Considerations

Migration Cost Analysis:

Direct Costs:
  - Developer time (design + implement + test)
  - Database migration scripts
  - Server downtime
  - User support (password reset helpdesk)
  
Indirect Costs:
  - User frustration (force reset)
  - Potential user loss
  - Training untuk support staff
  
Estimated: $100K - $500K untuk large platform

Management decision:
  "We haven't been breached yet, why spend now?"
  
Reality:
  Cost of breach: $3.86 million average (IBM 2020)
  Prevention >>> Remediation

5. Password Reuse Across Services

User behavior:
  - 59% reuse passwords (Google 2019)
  - Breach pada one service → credentials tried on others
  
Credential Stuffing:
  1. Attacker obtains LinkedIn breach credentials
  2. Try same email+password on:
     - Banks
     - Email providers
     - E-commerce sites
     - Social media
  3. 0.1% - 2% success rate (still millions of accounts)
  
Defense:
  - Cannot control user behavior
  - Can only make our hashes harder to crack
  - Slows down attacker progress

6. Weak Password Policies

Old policies (ineffective):
  - Minimum 6 characters
  - No complexity requirements
  - Allow common passwords ("password", "123456")
  - No breach database check
  
Result:
  40% users choose passwords from top 10,000 most common
  
Modern policies (effective):
  - Minimum 12 characters (15+ recommended)
  - Check against breach databases (Have I Been Pwned)
  - No common passwords
  - Password strength meter
  - Encourage passphrases

7. Regulatory and Compliance Lag

Regulations often lag behind threats:

GDPR (2018): Strong data protection
  - But tidak specify password hashing algorithms
  - "Appropriate security measures" (vague)
  
PCI DSS (Payment Card Industry):
  - Requires salted hashes
  - Tidak specify algorithm (bcrypt vs SHA-256)
  
NIST (US):
  - 2017: Deprecated password complexity rules
  - Recommended: Length > complexity
  - Recommended: Check breach databases
  
Industry moves slow:
  - Guidelines take years to update
  - Companies wait untuk compliance mandate
  - Proactive security rare

8. False Sense of Security

"We encrypt passwords"
  - Encryption ≠ Hashing
  - Encryption reversible (with key)
  - Hashing one-way (proper approach)
  
"We use SHA-256"
  - SHA-256 lebih baik dari MD5
  - Tapi still tidak untuk passwords (too fast)
  - bcrypt/Argon2 specifically designed untuk passwords
  
"We have SSL/TLS"
  - Transport security ≠ storage security
  - TLS protects in transit
  - Hashing protects at rest
  - Both needed (defense in depth)

Solutions:

1. Gradual Migration:
   - Implement bcrypt untuk new accounts
   - Rehash existing pada login (opportunistic)
   - After 6-12 months: force reset untuk remaining
   
2. Dual Hash Storage (transition):
   db.users:
     - password_hash_sha1 (deprecated)
     - password_hash_bcrypt (new)
     - migration_status (pending/completed)
   
   Login flow:
     if user.migration_status == 'pending':
       if verify_sha1(input, user.password_hash_sha1):
         # Rehash dengan bcrypt
         user.password_hash_bcrypt = bcrypt.hash(input)
         user.migration_status = 'completed'
         return success
   
3. Security Awareness:
   - Developer training (secure coding)
   - Management buy-in (cost-benefit)
   - Regular security audits
   - Penetration testing
   
4. Proactive Security:
   - Don't wait untuk breach
   - Implement defense in depth
   - Stay updated dengan best practices
   - Monitor security advisories

Kesimpulan:

Sistem lama rentan karena kombinasi technical debt, backward compatibility concerns, cost considerations, dan lack of security awareness. Solusi memerlukan gradual migration strategy, management support, dan proactive security mindset. Breach seperti LinkedIn membuktikan bahwa cost of prevention << cost of remediation.

Pertanyaan 2: Apa bedanya kelemahan algoritma dengan kelemahan implementasi?

Perbedaan fundamental antara algorithm weakness vs implementation weakness:

1. Kelemahan Algoritma (Cryptographic Weakness)

Definisi:

Kelemahan intrinsik dalam desain algoritma kriptografi
Tidak peduli seberapa baik implementasi, kelemahan tetap ada
Fundamental flaw yang tidak dapat diperbaiki tanpa mengganti algoritma

Contoh: MD5 Hash Function

Algoritma: MD5 (Message Digest 5)
Designed: 1991 by Ron Rivest
Purpose: Cryptographic hash function

Kelemahan Algoritma:
  1. Collision vulnerability
     - Menemukan dua input berbeda dengan hash sama
     - First collision: 2004 (researchers)
     - Practical collision: 2008 (dapat dilakukan < 1 menit)
     
  2. Preimage attack
     - Complexity: 2^123 operations (theoretically)
     - Below 2^128 (MD5 output size)
     - Tidak practical tapi better than brute force
     
  3. Mathematical weakness
     - Flaws dalam internal structure
     - Differential cryptanalysis efektif

Demonstration:

import hashlib

def md5_collision_demo():
    """
    Demonstrasi kelemahan MD5
    (menggunakan known collision dari penelitian)
    """
    # Two different inputs dengan MD5 hash sama (collision)
    input1 = bytes.fromhex("d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f89...")
    input2 = bytes.fromhex("d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f89...")
    
    hash1 = hashlib.md5(input1).hexdigest()
    hash2 = hashlib.md5(input2).hexdigest()
    
    print(f"Input 1 hash: {hash1}")
    print(f"Input 2 hash: {hash2}")
    print(f"Collision: {hash1 == hash2}")
    print(f"Inputs same: {input1 == input2}")
    
    # Result: Same hash, different inputs
    # Algorithm weakness: collision possible

Impact:

Digital Signatures:
  - Attacker dapat create malicious document dengan hash sama
  - Valid signature dari legitimate document dapat transferred
  - Fraud/forgery possible
  
Certificate Authorities:
  - 2008: Rogue CA certificate created (MD5 collision)
  - Could issue fake SSL certificates
  - MITM attacks pada HTTPS
  
Conclusion:
  MD5 fundamentally broken
  No amount of good implementation dapat fix
  Must use different algorithm (SHA-256, SHA-3)

Contoh Lain: DES (Data Encryption Standard)

Algoritma: DES
Key size: 56 bits

Kelemahan Algoritma:
  1. Key space too small
     - 2^56 = 72 quadrillion keys
     - 1998: DES cracked dalam 56 hours (EFF DES Cracker)
     - 2008: COPACOBANA cracked dalam < 1 day
     - Modern: dapat cracked dalam hours
  
  2. Linear cryptanalysis
     - Theoretical attack requiring 2^43 known plaintexts
     - Practical dalam certain scenarios
  
  3. Differential cryptanalysis
     - Dapat find key dengan 2^47 chosen plaintexts

Solution:
  - Triple-DES (3DES) - band-aid fix
  - AES - modern replacement (128/192/256 bit keys)

2. Kelemahan Implementasi (Implementation Vulnerability)

Definisi:

Algoritma secara kriptografis aman
Tetapi implementasi software/hardware memiliki flaws
Dapat diperbaiki tanpa mengganti algoritma

Contoh 1: Heartbleed (OpenSSL)

Algoritma: TLS/SSL (aman)
Implementation: OpenSSL library
Bug: CVE-2014-0160 (Heartbleed)

Vulnerability:
  TLS Heartbeat extension
  Missing bounds check pada memcpy()
  
Code (simplified):
  void process_heartbeat(char *request) {
    int payload_length = *(int*)request;  // attacker-controlled
    char *payload = request + 4;
    
    // BUG: tidak validate payload_length
    char *response = malloc(payload_length);
    memcpy(response, payload, payload_length);  // buffer over-read
    
    send_heartbeat_response(response);
  }

Attack:
  Attacker sends: payload_length = 64KB, actual payload = 1 byte
  Server reads beyond buffer
  Returns 64KB of memory (including secrets):
    - Private keys
    - Session tokens
    - Passwords
    - Other user data

Impact:
  - Millions of servers vulnerable
  - Private key theft possible
  - HTTPS compromised
  
Fix:
  Add bounds check:
  if (payload_length > actual_payload_size)
    return error;
  
Algorithm: Still secure (TLS/SSL)
Implementation: Fixed dalam OpenSSL 1.0.1g

Contoh 2: Debian OpenSSL Weak Key Generation

Algoritma: RSA (aman)
Implementation: Debian/Ubuntu OpenSSL package (2006-2008)

Bug:
  Developer commented out crucial entropy source
  Untuk fix Valgrind warning (uninitialized memory)
  
Original code:
  MD_Update(&m, buf, j);  // buf contains random data
  
Modified code (buggy):
  // MD_Update(&m, buf, j);  // commented out
  MD_Update(&m, buf, 0);      // zero randomness!

Impact:
  Random number generator only uses:
    - Process ID (PID): 15 bits entropy
  
  Total entropy: 15 bits instead of 128+ bits
  Keyspace: 2^15 = 32,768 possible keys
  
  All SSH/TLS keys generated 2006-2008 predictable:
    - Can enumerate all possible keys
    - Can crack dalam minutes
    
Fix:
  Restore original code
  Regenerate all affected keys
  
Algorithm: RSA still secure
Implementation: Human error dalam code modification

Contoh 3: Timing Attacks

Algoritma: AES (aman)
Implementation: Naive comparison function

Vulnerable code:
  def verify_password(stored_hash, input_hash):
    if len(stored_hash) != len(input_hash):
      return False
    
    for i in range(len(stored_hash)):
      if stored_hash[i] != input_hash[i]:
        return False  # EARLY RETURN
    
    return True

Attack:
  Measure response time
  
  Input "A" vs "XXXXXXX":
    - First byte wrong
    - Returns immediately (fast)
  
  Input "H" vs "HXXXXXX":
    - First byte correct, second wrong
    - Takes longer (slower)
  
  Attacker learns:
    - First byte is "H"
    - Repeat untuk setiap posisi
    - Leak entire hash character-by-character

Fix (constant-time comparison):
  def verify_password_safe(stored_hash, input_hash):
    if len(stored_hash) != len(input_hash):
      return False
    
    result = 0
    for i in range(len(stored_hash)):
      result |= ord(stored_hash[i]) ^ ord(input_hash[i])
    
    return result == 0  # Always checks all bytes

Algorithm: Still secure
Implementation: Fixed timing leak

3. Perbandingan Kelemahan
Aspect 	Kelemahan Algoritma 	Kelemahan Implementasi
Root Cause 	Cryptographic design flaw 	Programming/configuration error
Scope 	All implementations affected 	Specific software/version
Fix 	Replace algorithm 	Patch/update software
Examples 	MD5 collision, DES small keysize 	Heartbleed, Debian weak keys
Detection 	Cryptanalysis research 	Penetration testing, code audit
Severity 	Fundamental, permanent 	Fixable, temporary
Timeline 	Often discovered years after release 	Can be introduced anytime

4. LinkedIn Case Analysis

Kelemahan Algoritma:

SHA-1 untuk password hashing:
  - Algoritma designed untuk speed
  - 10 billion hashes/second pada GPU
  - Collision found (2017 SHAttered attack)
  
Not technically broken untuk password hashing
But inappropriate choice (too fast)

Recommendation:
  Use algorithm designed untuk password hashing:
    - bcrypt
    - scrypt
    - Argon2

Kelemahan Implementasi:

LinkedIn SHA-1 implementation:
  1. No salt
     - Implementation decision, bukan algoritma limitation
     - SHA-1 dapat use salt (proper implementation)
     
  2. No key stretching
     - Single iteration
     - Could have implemented multiple iterations
     
  3. Weak password policy
     - Allowed common passwords
     - Implementation/policy issue

These are IMPLEMENTATION failures
Same algorithm (SHA-1) dapat implemented lebih baik:
  - Add unique salt per user
  - Multiple iterations (10,000+)
  - Still suboptimal, tapi significantly better

5. Real-world Implications

Algoritma Weakness:

Once algorithm broken:
  - ALL implementations vulnerable
  - Cannot patch/update
  - Must migrate to new algorithm
  
Example: MD5
  - 2004: Collision found
  - 2025: Still broken
  - No future fixes possible
  - Migration to SHA-256/SHA-3 only solution

Implementation Weakness:

Can be fixed dengan updates:
  - Patch release
  - Configuration change
  - Code fix
  
Example: Heartbleed
  - 2014: Discovered
  - 2014: Fixed dalam OpenSSL 1.0.1g
  - Servers update → vulnerability gone
  - Algorithm (TLS) remains secure

6. Detection Methods

Algorithm Weakness:

Methods:
  - Cryptanalysis (mathematical analysis)
  - Academic research
  - Collision finding
  - Complexity analysis
  
Timeline:
  - Often takes years to discover
  - Peer review process
  - Published papers
  
Examples:
  - MD5: 13 years (1991 release → 2004 collision)
  - SHA-1: 16 years (2001 → 2017 practical collision)

Implementation Weakness:

Methods:
  - Code review
  - Penetration testing
  - Fuzzing
  - Static analysis tools
  - Runtime monitoring
  
Timeline:
  - Can be found immediately or years later
  - Depends on testing thoroughness
  
Examples:
  - Heartbleed: 2 years (2012 introduced → 2014 discovered)
  - Debian weak keys: 2 years in production

Kesimpulan:

Kelemahan Algoritma:

    Fundamental flaw dalam cryptographic design
    Affects semua implementations
    Requires algorithm replacement
    Cannot be patched
    Example: MD5 collision, DES small keysize

Kelemahan Implementasi:

    Programming atau configuration error
    Affects specific software/version
    Can be fixed dengan patch/update
    Algorithm remains secure
    Example: Heartbleed, timing attacks, missing salt

LinkedIn menggunakan SHA-1 (inappropriate algorithm) tanpa salt (implementation failure). Kombinasi algorithm choice + implementation flaws = critical vulnerability. Fix requires both: migrate to proper algorithm (bcrypt/Argon2) AND implement correctly (with salt, proper cost factor).

Pertanyaan 3: Bagaimana organisasi dapat memastikan sistem kriptografi mereka tetap aman di masa depan?

Organisasi perlu mengadopsi strategi comprehensive dan proactive untuk menjaga keamanan kriptografi di masa depan:

1. Crypto Agility (Kesiapan Migrasi)

Konsep:

Kemampuan untuk mengganti algoritma kriptografi dengan cepat
Tanpa architectural overhaul

Design Principles:
  - Abstraksi: Separate crypto implementation dari business logic
  - Pluggable: Easy swap algorithms
  - Versioning: Support multiple algorithms simultaneously
  - Migration path: Gradual transition

Implementation:

# BAD: Hardcoded algorithm
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# GOOD: Crypto agility
class PasswordHasher:
    def __init__(self, algorithm='bcrypt', version='v2'):
        self.algorithm = algorithm
        self.version = version
    
    def hash(self, password):
        if self.algorithm == 'bcrypt':
            return self._hash_bcrypt(password)
        elif self.algorithm == 'argon2':
            return self._hash_argon2(password)
        else:
            raise ValueError(f"Unknown algorithm: {self.algorithm}")
    
    def verify(self, password, stored_hash):
        # Parse hash to determine algorithm
        algo, version, hash_value = self._parse_hash(stored_hash)
        
        # Verify dengan appropriate algorithm
        if algo == 'bcrypt':
            return self._verify_bcrypt(password, hash_value)
        elif algo == 'argon2':
            return self._verify_argon2(password, hash_value)
    
    def needs_rehash(self, hashed_password):
        # Check if current parameters masih aman
        # Return True if perlu rehash dengan parameters baru
        pass

2. Regular Security Audits

Audit berkala untuk:
  - Menemukan dan memperbaiki kelemahan
  - Memastikan compliance dengan best practices
  - Mengidentifikasi potensi risiko baru
  
Frekuensi:
  - Setiap 6 bulan sekali
  - Setelah setiap insiden keamanan
  - Setelah perubahan besar pada sistem
  
Tim audit:
  - Internal security team
  - External security consultant (annual)

3. Penetration Testing

Uji coba penetrasi rutin untuk:
  - Mensimulasikan serangan nyata
  - Mengidentifikasi dan mengeksploitasi kelemahan
  
Frekuensi:
  - Setiap tahun sekali
  - Setelah setiap insiden keamanan besar
  - Setelah perubahan arsitektur atau teknologi utama
  
Tim penetration testing:
  - Tim internal terlatih
  - Vendor eksternal (certified)

4. Keamanan Berlapis (Defense in Depth)

Implementasi beberapa lapisan keamanan:
  - Firewall dan IDS/IPS
  - Enkripsi data (in transit dan at rest)
  - Segmentasi jaringan
  - Least privilege access control
  - Regular patching dan updates
  
Tujuan:
  - Mengurangi risiko dan dampak dari serangan
  - Menyulitkan attacker untuk mendapatkan akses atau bergerak lateral

5. Kebijakan Password yang Kuat

Kebijakan password yang direkomendasikan:
  - Minimum 12 karakter, kombinasi huruf besar, huruf kecil, angka, simbol
  - Tidak ada penggunaan password umum atau yang mudah ditebak
  - Penggunaan password manager untuk menyimpan dan menghasilkan password yang kuat
  
Pendidikan pengguna:
  - Pentingnya password yang kuat dan unik
  - Bahaya dari password reuse
  - Cara menggunakan password manager

6. Multi-Factor Authentication (MFA)

Implementasi MFA di semua sistem yang mendukung:
  - Menggunakan aplikasi authenticator (Google Authenticator, Authy)
  - SMS atau email sebagai faktor kedua (jika perlu)
  
Pendidikan pengguna:
  - Pentingnya MFA untuk keamanan tambahan
  - Cara mengatur dan menggunakan MFA

7. Respons Insiden yang Efektif

Rencana respons insiden yang jelas:
  - Deteksi dan analisis insiden
  - Kontainment, eradication, dan recovery
  - Post-incident analysis dan reporting
  
Tim respons insiden:
  - Tim internal terlatih
  - Konsultan eksternal (jika perlu)

8. Pelatihan dan Kesadaran Keamanan

Program pelatihan keamanan untuk semua karyawan:
  - Dasar-dasar keamanan siber
  - Cara mengenali dan melaporkan insiden
  - Praktik terbaik untuk keamanan informasi
  
Frekuensi:
  - Pelatihan awal untuk karyawan baru
  - Pelatihan ulang tahunan untuk semua karyawan

9. Kebijakan dan Prosedur Keamanan yang Jelas

Dokumentasi kebijakan dan prosedur keamanan:
  - Kebijakan penggunaan kata sandi
  - Kebijakan akses dan otorisasi
  - Kebijakan enkripsi dan penyimpanan data
  - Prosedur respons insiden
  
Pemeriksaan dan pembaruan berkala:
  - Kebijakan dan prosedur ditinjau dan diperbarui setiap tahun
  - Setelah setiap insiden keamanan
  - Setelah perubahan besar pada sistem atau organisasi

10. Komitmen Manajemen dan Dukungan Anggaran

Manajemen puncak harus:
  - Memberikan dukungan dan sumber daya yang cukup untuk keamanan
  - Terlibat dalam peninjauan dan pembaruan kebijakan keamanan
  - Mendukung pelatihan dan kesadaran keamanan untuk semua karyawan
  
Anggaran yang memadai untuk:
  - Alat dan teknologi keamanan
  - Pelatihan dan pengembangan keterampilan
  - Audit dan penilaian keamanan eksternal

---

## 8. Kesimpulan
Praktikum ini memberikan pemahaman mendalam tentang serangan terhadap sistem kriptografi dengan menganalisis kasus nyata pelanggaran data LinkedIn tahun 2012. Beberapa kesimpulan penting yang dapat diambil:
    Kerentanan SHA-1 Tanpa Salt: Serangan LinkedIn menunjukkan bahwa penggunaan SHA-1 tanpa salt membuat password sangat rentan terhadap serangan dictionary dan rainbow table. Hash function yang cepat seperti SHA-1 memungkinkan attacker untuk melakukan brute force dengan kecepatan tinggi.
    Implementasi Password Hashing yang Benar: Dari analisis dan implementasi dalam praktikum ini, terbukti bahwa algoritma seperti bcrypt dan Argon2 memberikan perlindungan yang jauh lebih baik dibandingkan SHA-1. Kedua algoritma ini dirancang khusus untuk password hashing dengan fitur salt otomatis dan computational cost yang dapat disesuaikan.
    Perbandingan Performa:
        SHA-1: Sangat cepat (dapat melakukan jutaan hash per detik), cocok untuk data integrity tapi tidak untuk password
        bcrypt: Lebih lambat dengan work factor yang dapat disesuaikan, menyulitkan brute force attack
        Argon2: Modern, memory-hard algorithm yang resisten terhadap GPU dan ASIC attacks
    Best Practices untuk Keamanan Password:
        Menggunakan algoritma password hashing yang tepat (bcrypt, Argon2, scrypt)
        Implementasi salt yang unik untuk setiap password
        Menggunakan work factor/cost parameter yang sesuai dengan kebutuhan keamanan
        Mengimplementasikan password policy yang kuat
        Edukasi pengguna tentang pentingnya password yang kuat dan unik
    Dampak Pelanggaran Data: Analisis kasus LinkedIn menunjukkan bahwa pelanggaran data dapat memiliki dampak jangka panjang, termasuk:
        Kerugian kepercayaan pengguna
        Risiko keamanan akibat password reuse
        Implikasi hukum dan finansial
        Kerusakan reputasi perusahaan
    Defense in Depth: Keamanan sistem tidak boleh hanya bergantung pada satu lapisan. Diperlukan pendekatan berlapis yang mencakup:
        Enkripsi yang kuat
        Multi-factor authentication
        Monitoring dan auditing
        Pelatihan kesadaran keamanan
        Regular security updates
        Incident response planning
    Pembelajaran untuk Masa Depan: Organisasi harus secara proaktif mengevaluasi dan memperbarui sistem kriptografi mereka, mengadopsi standar industri terbaru, dan tidak menunggu hingga terjadi pelanggaran data untuk meningkatkan keamanan.

Praktikum ini mendemonstrasikan bahwa pemahaman tentang kriptografi bukan hanya tentang algoritma enkripsi, tetapi juga tentang implementasi yang benar, pemilihan algoritma yang tepat untuk use case yang tepat, dan pemahaman tentang threat landscape yang terus berkembang. Dengan menganalisis serangan nyata seperti kasus LinkedIn, kita dapat belajar dari kesalahan masa lalu dan menerapkan best practices untuk melindungi sistem di masa depan.

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
Author: Uswatun Khasanah <Khasanah8952@gmail.com>
Date:   2026-09-1

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
