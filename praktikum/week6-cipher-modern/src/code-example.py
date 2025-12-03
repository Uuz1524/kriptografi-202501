from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad  # opsional, jika butuh mode CBC/ECB
import binascii

def hex_to_bytes(h):
    try:
        return binascii.unhexlify(h.replace(' ', ''))
    except Exception as e:
        raise ValueError(f"Format hex tidak valid: {e}")

def bytes_to_hex(b):
    return binascii.hexlify(b).decode().lower()

print("=== AES-EAX Manual Mode ===")
print("Pilih mode:")
print("1. Enkripsi (masukkan pesan & dapatkan key/nonce/ciphertext/tag)")
print("2. Dekripsi (masukkan key, nonce, ciphertext, tag → dapatkan pesan)")
print("-" * 60)

mode = input("Masukkan pilihan (1/2): ").strip()

if mode == "1":
    print("\n[Mode Enkripsi]")
    plaintext = input("Masukkan pesan (plaintext): ").encode('utf-8')
    
    # Generate key & nonce
    key = AES.new(b"", AES.MODE_EAX).key  # cara cepat generate 16-byte key
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    nonce = cipher.nonce

    print("\n--- Output Enkripsi ---")
    print("Key (hex)   :", bytes_to_hex(key))
    print("Nonce (hex) :", bytes_to_hex(nonce))
    print("Ciphertext  :", bytes_to_hex(ciphertext))
    print("Tag (hex)   :", bytes_to_hex(tag))

elif mode == "2":
    print("\n[Mode Dekripsi]")
    try:
        key_hex   = input("Masukkan key (hex): ").strip()
        nonce_hex = input("Masukkan nonce (hex): ").strip()
        ct_hex    = input("Masukkan ciphertext (hex): ").strip()
        tag_hex   = input("Masukkan tag (hex): ").strip()

        key   = hex_to_bytes(key_hex)
        nonce = hex_to_bytes(nonce_hex)
        ct    = hex_to_bytes(ct_hex)
        tag   = hex_to_bytes(tag_hex)

        # Validasi panjang
        if len(key) not in (16, 24, 32):
            raise ValueError("Panjang key harus 16/24/32 byte (128/192/256 bit).")
        if len(nonce) == 0:
            raise ValueError("Nonce tidak boleh kosong.")

        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        decrypted = cipher.decrypt_and_verify(ct, tag)
        plaintext = decrypted.decode('utf-8', errors='replace')

        print("\nDekripsi BERHASIL!")
        print("Pesan asli:", plaintext)

    except (ValueError, KeyError) as e:
        print("\n GAGAL! Error:", e)
        print("Penyebab umum:")
        print("- Hex tidak valid")
        print("- Key/nonce/ciphertext/tag salah/tidak cocok")
        print("- Tag tidak sesuai → data dimodifikasi")

else:
    print("Pilihan tidak valid. Jalankan ulang dan pilih 1 atau 2.")
