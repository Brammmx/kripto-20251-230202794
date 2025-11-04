# Laporan Praktikum Kriptografi
Minggu ke-: 6 
Topik: [Cipher Modern (DES, AES, RSA)]  
Nama: [Bramby Dida Baskara]  
NIM: [230202794]  
Kelas: [5 IKRA]  


## 1. Tujuan
 1. Mengimplementasikan algoritma DES untuk blok data sederhana.
 2. Menerapkan algoritma AES dengan panjang kunci 128 bit.
 3. Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.
##  2. Dasar Teori
  Perkembangan cipher modern dimulai dengan munculnya sistem kriptografi berbasis komputer yang mampu mengolah data dalam bentuk blok-bit. Tidak seperti cipher klasik yang hanya bekerja pada huruf, cipher modern bekerja dengan operasi matematis dan bitwise untuk menjaga kerahasiaan data secara digital.

1. Data Encryption Standard (DES)
DES merupakan salah satu cipher blok pertama yang menjadi standar enkripsi pada tahun 1977. Algoritma ini bekerja dengan panjang blok 64 bit dan kunci 56 bit. DES menggunakan struktur Feistel Network, di mana setiap putaran (round) terdiri dari permutasi dan substitusi untuk meningkatkan difusi dan konfusi data. Namun, karena ukuran kuncinya terlalu pendek, DES kini dianggap tidak aman terhadap serangan brute force.

2. Advanced Encryption Standard (AES)
AES menggantikan DES sebagai standar enkripsi pada tahun 2001. AES menggunakan ukuran blok tetap 128 bit dengan variasi panjang kunci 128, 192, atau 256 bit. AES tidak menggunakan struktur Feistel, melainkan substitution–permutation network (SPN). Algoritma ini memiliki 10–14 ronde tergantung panjang kuncinya, dan dirancang agar efisien untuk perangkat keras maupun perangkat lunak.

3. Rivest–Shamir–Adleman (RSA)
RSA adalah algoritma kriptografi asimetris, artinya menggunakan dua kunci berbeda: kunci publik untuk enkripsi dan kunci privat untuk dekripsi. RSA didasarkan pada prinsip faktorisasi bilangan prima besar, di mana keamanan algoritma bergantung pada sulitnya memecahkan hasil perkalian dua bilangan prima besar. RSA banyak digunakan dalam sistem keamanan modern seperti SSL/TLS dan tanda tangan digital.

## 3. Alat dan Bahan

Git dan akun GitHub

## 4. Langkah Percobaan
1. Membuat struktur folder:
   praktikum/week6-cipher-modern/
├─ src/
├─ screenshots/
└─ laporan.md
2. Menginstal library yang dibutuhkan:
   pip install pycryptodome
3. Membuat tiga file program:
  - des.py
  - aes.py
  - rsa.py
4. Menulis kode untuk masing-masing algoritma (DES, AES, dan RSA).

5. Menjalankan program dan mencatat hasil eksekusinya.

6. Menyimpan screenshot hasil ke folder screenshots/.

7.Melakukan commit Git dengan pesan week6-cipher-modern.

## 5. Source Code
a. Implementasi DES (Simulasi)
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)  # 64-bit key
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b"ABCDEFGH"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)

b. Implementasi AES-128
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # 128-bit key
cipher = AES.new(key, AES.MODE_EAX)

plaintext = b"Modern Cipher AES Example"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

print("Ciphertext:", ciphertext)

# Dekripsi
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher_dec.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())

c. Implementasi RSA
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Enkripsi dengan public key
cipher_rsa = PKCS1_OAEP.new(public_key)
plaintext = b"RSA Example"
ciphertext = cipher_rsa.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Dekripsi dengan private key
decipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = decipher_rsa.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())


## 6. Hasil dan Pembahasan
 | Algoritma | Jenis Cipher       | Ukuran Kunci | Hasil Enkripsi       | Hasil Dekripsi              |
| --------- | ------------------ | ------------ | -------------------- | --------------------------- |
| DES       | Simetris (Feistel) | 56 bit       | `b'\xaf\x8c\x10...'` | `ABCDEFGH`                  |
| AES       | Simetris (SPN)     | 128 bit      | `b'\x1a\xcf\x9b...'` | `Modern Cipher AES Example` |
| RSA       | Asimetris          | 2048 bit     | `b'\x8f\xd2\xab...'` | `RSA Example`               |

Analisis:

- DES bekerja dengan blok 64-bit, namun tidak direkomendasikan karena mudah dipecahkan.

- AES memiliki keamanan tinggi dan efisiensi baik, serta merupakan standar global saat ini.

- RSA digunakan untuk pertukaran kunci dan tanda tangan digital, bukan untuk enkripsi data besar, karena prosesnya lebih lambat dibanding cipher simetris.


## 7. Jawaban Pertanyaan
1. Perbedaan mendasar antara DES, AES, dan RSA:
DES dan AES adalah cipher simetris (menggunakan kunci yang sama untuk enkripsi dan dekripsi), sedangkan RSA asimetris (menggunakan pasangan kunci publik dan privat).

2. Mengapa AES lebih banyak digunakan dibanding DES:
AES memiliki panjang kunci lebih besar (128/192/256 bit), lebih aman terhadap brute force, dan lebih efisien untuk implementasi perangkat keras maupun perangkat lunak.

3. Mengapa RSA disebut algoritma asimetris:
Karena RSA menggunakan dua kunci berbeda—publik untuk enkripsi dan privat untuk dekripsi. Kunci dibuat berdasarkan faktorisasi bilangan prima besar, yang sulit untuk dibalik tanpa mengetahui kunci privat.
## 8. Kesimpulan
 Pada praktikum ini, telah diimplementasikan tiga algoritma cipher modern yaitu DES, AES, dan RSA. DES menunjukkan konsep dasar cipher blok, AES menjadi standar modern dengan tingkat keamanan tinggi, dan RSA memperkenalkan kriptografi asimetris yang digunakan secara luas dalam sistem keamanan digital.

## 9. Daftar Pustaka
Stallings, W. (2017). Cryptography and Network Security: Principles and Practice.

Katz, J., & Lindell, Y. (2015). Introduction to Modern Cryptography.

Modul Praktikum Kriptografi Minggu ke-6: Cipher Modern (DES, AES, RSA).

## 10. Commit Log
commit a5c7f2d
Author: Bramby Dida Baskara <brambydida@github.com>
Date:   2025-11-04

    week6-cipher-modern: implementasi DES, AES, dan RSA beserta laporan hasil percobaan
