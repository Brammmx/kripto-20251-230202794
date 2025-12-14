from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import binascii

# --- Inisialisasi Kunci dan Pesan ---
# Generate pasangan kunci RSA (2048 bit)
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()
print("Kunci RSA berhasil dibuat.")

# Pesan asli yang akan ditandatangani
original_message = b"Hello, ini pesan penting."
h_original = SHA256.new(original_message)

# --- Langkah 1: Buat Tanda Tangan ---
try:
    # Buat tanda tangan dengan private key
    signature = pkcs1_15.new(private_key).sign(h_original)
    print(f"\nMessage: {original_message.decode()}")
    # Tampilkan tanda tangan dalam format hex
    print("Signature (Hex):", signature.hex())
except Exception as e:
    print(f"Gagal membuat tanda tangan: {e}")

# --- Langkah 2: Verifikasi Tanda Tangan pada Pesan Asli ---
print("\n--- Uji 1: Verifikasi Pesan Asli ---")
try:
    pkcs1_15.new(public_key).verify(h_original, signature)
    print("✅ Verifikasi berhasil: Tanda tangan VALID (Integritas dan Otentikasi terjamin).")
except (ValueError, TypeError):
    print("❌ Verifikasi gagal: Tanda tangan TIDAK VALID.")

# --- Langkah 3: Uji Modifikasi Pesan ---
# Modifikasi pesan (seharusnya verifikasi gagal)
fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)

print("\n--- Uji 2: Verifikasi Pesan Palsu (Dimodifikasi) ---")
print(f"Fake Message: {fake_message.decode()}")
try:
    # Coba verifikasi tanda tangan ASLI dengan digest dari pesan PALSU
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("✅ Verifikasi berhasil (Seharusnya GAGAL karena pesan diubah!).")
except (ValueError, TypeError):
    print("❌ Verifikasi gagal: Tanda tangan TIDAK cocok dengan pesan (Integritas terlanggar).")

# --- Uji Tambahan: Tanda Tangan Palsu ---
print("\n--- Uji 3: Tanda Tangan Palsu (Ubah 1 byte signature) ---")
# Modifikasi 1 byte pada signature
modified_signature = bytearray(signature)
modified_signature[0] ^= 0xFF # Flip beberapa bit pada byte pertama
modified_signature = bytes(modified_signature)

try:
    # Coba verifikasi dengan signature yang diubah
    pkcs1_15.new(public_key).verify(h_original, modified_signature)
    print("✅ Verifikasi berhasil (Seharusnya GAGAL karena tanda tangan diubah!).")
except (ValueError, TypeError):
    print("❌ Verifikasi gagal: Tanda tangan TIDAK VALID (Tanda tangan telah diubah).")
