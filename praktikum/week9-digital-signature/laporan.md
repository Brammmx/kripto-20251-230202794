# Laporan Praktikum Kriptografi
Minggu ke-: 9
Topik: [Digital Signature (RSA/DSA)]  
Nama: [Bramby Dida Baskara]  
NIM: [230202794]  
Kelas: [5IKRA]  

---

## 1. Tujuan
Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.
Memverifikasi keaslian tanda tangan digital.
Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data



## 2. Dasar Teori
Tanda tangan digital adalah mekanisme kriptografis yang digunakan untuk memverifikasi keaslian dan integritas suatu pesan atau dokumen elektronik. Berbeda dengan skema enkripsi yang bertujuan merahasiakan data, tanda tangan digital bertujuan untuk otentikasi (memastikan identitas pengirim) dan integritas (memastikan data belum diubah).

Algoritma seperti RSA atau DSA digunakan untuk membuat tanda tangan digital. Dalam prosesnya, pengirim (Signer) menggunakan fungsi hash (seperti SHA256) untuk menghasilkan message digest dari pesan, lalu mengenkripsi digest tersebut menggunakan kunci privat miliknya. Hasil enkripsi inilah yang menjadi tanda tangan digital. Penerima (Verifier) akan menggunakan kunci publik pengirim untuk mendekripsi tanda tangan, mendapatkan kembali message digest asli. Penerima juga membuat message digest sendiri dari pesan yang diterima, lalu membandingkan keduanya. Jika kedua digest cocok, maka verifikasi berhasil, menandakan pesan tidak diubah (integritas) dan berasal dari pemilik kunci privat yang sah (otentikasi).
## 3. Alat dan Bahan
- Visual Studio Code / editor lain  
- Git dan akun GitHub
- pyhton


## 4. Langkah Percobaan
Langkah-langkah yang dilakukan:

Membuat struktur folder praktikum/week9-digital-signature/ yang berisi src/, screenshots/, dan laporan.md.

Menginstal library pycryptodome dengan perintah pip install pycryptodome.

Membuat file src/signature.py untuk mengimplementasikan tiga langkah: Generate Key dan Sign, Verify Signature, dan Test Message Modification.

Menjalankan program dengan perintah python src/signature.py.

Mengambil screenshot hasil eksekusi program.

## 5. Source Code
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
## 6. Hasil dan Pembahasan
Uji Coba,Pesan yang Diverifikasi,Tanda Tangan,Ekspektasi Hasil,Hasil Program,Analisis
Uji 1,Asli,Asli,Berhasil,Berhasil,"Pesan dan tanda tangan cocok, otentikasi dan integritas terjamin."
Uji 2,Dimodifikasi/Palsu,Asli,Gagal,Gagal,"Digest pesan baru (SHA256(fake_message)) tidak cocok dengan digest yang diekstrak dari tanda tangan asli, menunjukkan integritas pesan terlanggar."
Uji 3,Asli,Dimodifikasi,Gagal,Gagal,"Tanda tangan diubah, sehingga hasil dekripsi kunci publik menghasilkan digest yang berbeda dari SHA256(original_message), menunjukkan keaslian/otentikasi terlanggar."
## 7. Jawaban Pertanyaan
1. Apa perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA?

Perbedaan utama terletak pada tujuan dan penggunaan kunci:

Enkripsi RSA (Kerahasiaan): Tujuannya adalah menjamin kerahasiaan (confidentiality) data. Data dienkripsi menggunakan kunci publik penerima dan hanya dapat didekripsi menggunakan kunci privat penerima.

Tanda Tangan Digital RSA (Otentikasi & Integritas): Tujuannya adalah menjamin otentikasi dan integritas data. Tanda tangan dibuat dengan mengenkripsi message digest menggunakan kunci privat pengirim, dan diverifikasi menggunakan kunci publik pengirim.

2. Mengapa tanda tangan digital menjamin integritas dan otentikasi pesan?

Integritas (Integrity): Dijamin karena tanda tangan dibuat berdasarkan message digest (hash) dari pesan. Jika pesan diubah (bahkan 1 bit), hash akan berubah total. Saat verifikasi, hash yang diekstrak dari tanda tangan (menggunakan kunci publik) akan dibandingkan dengan hash pesan yang diterima. Ketidakcocokan membuktikan pesan telah dimodifikasi.

Otentikasi (Authentication): Dijamin karena hanya pemilik kunci privat yang sah (dan rahasia) yang dapat membuat tanda tangan yang valid. Jika verifikasi menggunakan kunci publik pengirim berhasil, maka penerima yakin bahwa pesan tersebut benar-benar berasal dari pemilik kunci privat tersebut.

3. Bagaimana peran Certificate Authority (CA) dalam sistem tanda tangan digital modern?

Certificate Authority (CA) adalah pihak ketiga tepercaya (TTP - Trusted Third Party) yang tugas utamanya adalah mengikat identitas seseorang atau entitas dengan kunci publik mereka melalui penerbitan Sertifikat Digital (Digital Certificate).

Peran CA: CA mencegah serangan man-in-the-middle dan masalah peniruan identitas. Ketika seseorang menerima kunci publik, mereka harus yakin bahwa kunci publik tersebut benar-benar milik orang yang diklaim. CA meninjau identitas, kemudian menandatangani kunci publik tersebut. Tanda tangan CA ini menjamin bahwa kunci publik tersebut adalah asli.

Dengan kata lain, CA memverifikasi bahwa kunci publik yang Anda gunakan untuk verifikasi benar-benar milik pengirim yang Anda yakini, sehingga memperkuat jaminan otentikasi.

## 8. Kesimpulan
Praktikum ini berhasil mengimplementasikan dan memverifikasi tanda tangan digital menggunakan algoritma RSA dan fungsi hash SHA256. Hasil uji coba menunjukkan bahwa tanda tangan digital berhasil menjamin integritas pesan dengan mendeteksi perubahan pada isi pesan, serta menjamin otentikasi dengan memvalidasi kepemilikan kunci. Penggunaan pasangan kunci privat dan publik secara terbalik dari enkripsi, yaitu signing dengan kunci privat dan verification dengan kunci publik, merupakan fondasi penting dalam skema tanda tangan digital.
## 9. Daftar Pustaka
Stinson, D. R. (2019). Cryptography: Theory and Practice (4th ed.). CRC Press. (Materi Rujukan Bab 5)

Modul Praktikum 09 Digital Signature (RSA/DSA).

Stallings, W. (2020). Cryptography and Network Security: Principles and Practice (8th ed.). Pearson.
## 10. Commit Log
commit [hash_commit_terakhir]
Author: Bramby Dida Baskara <[brambybaskara8@gmail.com>
Date:   2025-12-11

    week9-digital-signature
