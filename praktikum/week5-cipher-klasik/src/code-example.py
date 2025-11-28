1.def vigenere_encrypt(plaintext, key, verbose=False):
    """
    Enkripsi teks menggunakan sandi Vigenère.
    
    Parameters:
        plaintext (str): Teks asli yang akan dienkripsi.
        key (str): Kunci berupa huruf (A-Z/a-z). Non-alfabet diabaikan.
        verbose (bool): Jika True, tampilkan langkah per karakter.
    
    Returns:
        str: Ciphertext hasil enkripsi.
    """
    # Filter hanya huruf dari kunci, konversi ke lowercase
    key = ''.join(filter(str.isalpha, key)).lower()
    if not key:
        raise ValueError("Kunci harus mengandung minimal satu huruf.")
    
    result = []
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            # Ambil huruf kunci yang sesuai (ulang jika perlu)
            k = key[key_index % len(key)]
            shift = ord(k) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            
            # Enkripsi: (P + K) mod 26
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(encrypted_char)
            
            if verbose:
                print(f"[E] '{char}' + '{k}' (shift={shift:2}) → '{encrypted_char}'")
            key_index += 1
        else:
            # Biarkan karakter non-alfabet (spasi, tanda baca, angka) tidak berubah
            result.append(char)
    
    return "".join(result)


def vigenere_decrypt(ciphertext, key, verbose=False):
    """
    Dekripsi teks menggunakan sandi Vigenère.
    
    Parameters:
        ciphertext (str): Teks terenkripsi.
        key (str): Kunci (harus sama dengan saat enkripsi).
        verbose (bool): Jika True, tampilkan langkah per karakter.
    
    Returns:
        str: Plaintext hasil dekripsi.
    """
    # Filter hanya huruf dari kunci, konversi ke lowercase
    key = ''.join(filter(str.isalpha, key)).lower()
    if not key:
        raise ValueError("Kunci harus mengandung minimal satu huruf.")
    
    result = []
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            k = key[key_index % len(key)]
            shift = ord(k) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            
            # Dekripsi: (C - K) mod 26
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            result.append(decrypted_char)
            
            if verbose:
                print(f"[D] '{char}' - '{k}' (shift={shift:2}) → '{decrypted_char}'")
            key_index += 1
        else:
            result.append(char)
    
    return "".join(result)



# Contoh Penggunaan & Pengujian

if __name__ == "__main__":
    msg = "KRIPTOGRAFI"
    key = "KEY"
    
    print("="*50)
    print(" VIGENÈRE CIPHER")
    print("="*50)
    print(f"Plaintext : '{msg}'")
    print(f"Key       : '{key}'")
    print("-"*50)
    
    # Enkripsi
    enc = vigenere_encrypt(msg, key, verbose=True)
    print(f"\nCiphertext: '{enc}'")
    
    # Dekripsi
    dec = vigenere_decrypt(enc, key, verbose=True)
    print(f"\n Decrypted : '{dec}'")
    
    print("-"*50)
    print(f" Verifikasi: {'BERHASIL' if dec == msg else 'GAGAL'}")
    print("="*50)
    
    # Contoh tambahan dengan spasi & simbol
    print("\n Contoh dengan spasi dan tanda baca:")
    msg2 = "Hello, World! 123"
    key2 = "SECRET"
    enc2 = vigenere_encrypt(msg2, key2)
    dec2 = vigenere_decrypt(enc2, key2)
    print(f"Plaintext : '{msg2}'")
    print(f"Ciphertext: '{enc2}'")
    print(f"Decrypted : '{dec2}'")
    print(f" ifikasi: {'BERHASIL' if dec2 == msg2 else 'GAGAL'}")





2.def transpose_encrypt(plaintext, key=5, verbose=False):
    """ {Z
    Enkripsi teks menggunakan Columnar Transposition Cipher.
    
    Parameters:
        plaintext (str): Teks asli.
        key (int): Jumlah kolom (lebar matriks). Harus ≥ 1.
        verbose (bool): Jika True, tampilkan matriks dan proses.
    
    Returns:
        str: Ciphertext hasil enkripsi.
    """
    if not isinstance(key, int) or key < 1:
        raise ValueError("Key harus bilangan bulat positif (≥1).")
    

    # plaintext = ''.join(plaintext.split())  # aktifkan jika ingin *tanpa spasi*
    
    # Buat matriks: isi baris demi baris
    grid = []
    for i in range(0, len(plaintext), key):
        row =plaintext[i:i+key].ljust(key, '')  # tidak padding — biarkan baris terakhir pendek
        grid.append(list(row))
    
    if verbose:
        print(" Matriks Enkripsi (baris diisi kiri→kanan):")
        for r in grid:
            print(' '.join(c if c else '␣' for c in r))
        print(" Baca kolom demi kolom (atas→bawah)")

    # Baca kolom demi kolom
    ciphertext = ''
    for col in range(key):
        for row in grid:
            if col < len(row) and row[col]:
                ciphertext += row[col]
                if verbose:
                    print(f"  Kolom {col+1}, baris → '{row[col]}'")
    
    if verbose:
        print(f" Ciphertext: '{ciphertext}'")
    return ciphertext


def transpose_decrypt(ciphertext, key=5, verbose=False):
    """
    Dekripsi teks menggunakan Columnar Transposition Cipher.
    
    Parameters:
        ciphertext (str): Teks terenkripsi.
        key (int): Jumlah kolom (harus sama dengan saat enkripsi).
        verbose (bool): Jika True, tampilkan proses rekonstruksi matriks.
    
    Returns:
        str: Plaintext hasil dekripsi.
    """
    if not isinstance(key, int) or key < 1:
        raise ValueError("Key harus bilangan bulat positif (≥1).")
    
    n = len(ciphertext)
    num_cols = key
    num_rows = (n + key - 1) // key  # ceil(n / key)
    num_full_cols = n % key
    if num_full_cols == 0:
        num_full_cols = key  # semua kolom penuh
    
    # Hitung panjang tiap kolom
    col_lengths = [num_rows if i < num_full_cols else num_rows - 1 for i in range(key)]
    
    if verbose:
        print(f" Panjang kolom: {col_lengths}")
        print(" Membagi ciphertext ke kolom-kolom...")
    
    # Pisahkan ciphertext ke kolom-kolom
    columns = []
    start = 0
    for length in col_lengths:
        columns.append(ciphertext[start:start+length])
        if verbose:
            print(f"  Kolom {len(columns)}: '{columns[-1]}'")
        start += length
    
    # Rekonstruksi baris
    plaintext = ''
    for row in range(num_rows):
        for col in range(key):
            if row < len(columns[col]):
                plaintext += columns[col][row]
    
    if verbose:
        print(f" Plaintext: '{plaintext}'")
    return plaintext


# Contoh Penggunaan & Pengujian

if __name__ == "__main__":
    msg = "TRANSPOSITIONCIPHER"
    key = 5
    
    print("="*60)
    print(" COLUMNAR TRANSPOSITION CIPHER")
    print("="*60)
    print(f"Plaintext : '{msg}'")
    print(f"Key (kolom): {key}")
    print("-"*60)
    
    # Enkripsi
    enc = transpose_encrypt(msg, key=key, verbose=True)
    print(f"\n Ciphertext: '{enc}'\n")
    
    # Dekripsi
    dec = transpose_decrypt(enc, key=key, verbose=True)
    print(f"\n Decrypted : '{dec}'")
    
    print("-"*60)
    print(f" Verifikasi: {'BERHASIL' if dec == msg else 'GAGAL'}")
    print("="*60)
    
    # Contoh dengan spasi & simbol (lebih realistis)
    print("\n Contoh dengan spasi dan tanda baca:")
    msg2 = "HELLO WORLD! 123"
    key2 = 4
    enc2 = transpose_encrypt(msg2, key2)
    dec2 = transpose_decrypt(enc2, key2)
    print(f"Plaintext : '{msg2}'")
    print(f"Ciphertext: '{enc2}'")
    print(f"Decrypted : '{dec2}'")
    print(f"Verifikasi: {'BERHASIL' if dec2 == msg2 else 'GAGAL'}")
