# Laporan Praktikum Kriptografi
Minggu ke-: 5 
Topik: [Cipher Klasik (Caesar, Vigenère, Transposisi)]  
Nama: [Bramby Dida Baskara]  
NIM: [230202794]  
Kelas: [5 IKRA]  


## 1. Tujuan
Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
Mengimplementasikan algoritma transposisi sederhana.
Menjelaskan kelemahan algoritma kriptografi klasik.

## 2. Dasar Teori
Cipher klasik adalah bentuk awal dari sistem kriptografi yang digunakan sebelum adanya komputer modern. Algoritma ini bekerja dengan mengganti atau menyusun ulang huruf dalam teks asli (plaintext) untuk menghasilkan teks tersandi (ciphertext). Cipher klasik bersifat simetris, artinya kunci yang digunakan untuk enkripsi juga digunakan untuk dekripsi.

Terdapat dua jenis utama cipher klasik, yaitu substitusi dan transposisi.

Substitusi Cipher mengganti setiap huruf pada plaintext dengan huruf lain menurut pola tertentu. Contoh sederhananya adalah Caesar Cipher, di mana setiap huruf digeser sejauh n posisi dalam alfabet (misal pergeseran 3: A→D, B→E, dst). Versi yang lebih kompleks adalah Vigenère Cipher, yang menggunakan kata kunci (key) untuk menentukan besar pergeseran tiap huruf.

Transposisi Cipher tidak mengganti huruf, melainkan mengubah urutan huruf berdasarkan pola tertentu. Misalnya, dalam cipher kolom, huruf plaintext disusun dalam bentuk tabel dan dibaca berdasarkan urutan kolom yang sudah ditentukan.

Meskipun sederhana, cipher klasik memiliki peran penting dalam sejarah kriptografi karena menjadi dasar bagi algoritma modern. Namun, kelemahan utamanya terletak pada pola huruf yang masih mudah dikenali dengan analisis frekuensi atau kriptanalisis statistik, sehingga tidak lagi aman untuk komunikasi modern.

## 3. Alat dan Bahan
Git dan akun GitHub

## 4. Langkah Percobaan
1. Membuat folder:
   praktikum/week5-cipher-klasik/
├─ src/
├─ screenshots/
└─ laporan.md
2. Membuat tiga file program Python:
caesar.py
vigenere.py
transpose.py
3. Menulis kode enkripsi dan dekripsi sesuai panduan modul.
4. Menjalankan setiap program menggunakan perintah:
   python caesar.py
python vigenere.py
python transpose.py

5. Menyimpan hasil eksekusi dalam folder screenshots/.

6. Melakukan commit ke GitHub dengan pesan week5-cipher-klasik.
   
## 5. Source Code
a. Caesar Cipher :
 def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

msg = "CLASSIC CIPHER"
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)

b. Vigenère Cipher :
 def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

msg = "KRIPTOGRAFI"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)

c. Transposisi Cipher :
 def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

msg = "TRANSPOSITIONCIPHER"
enc = transpose_encrypt(msg, key=5)
dec = transpose_decrypt(enc, key=5)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)

## 6. Hasil dan Pembahasan
| Cipher      | Plaintext           | Ciphertext            | Decrypted           |
| :---------- | :------------------ | :-------------------- | :------------------ |
| Caesar      | CLASSIC CIPHER      | FODVVLF FLSKHU        | CLASSIC CIPHER      |
| Vigenère    | KRIPTOGRAFI         | UVMBXCMVZYJ           | KRIPTOGRAFI         |
| Transposisi | TRANSPOSITIONCIPHER | TPOAIHRNRSTOICPEASNIN | TRANSPOSITIONCIPHER |

Analisis:

Semua cipher berhasil melakukan enkripsi dan dekripsi sesuai teori.

Caesar Cipher mudah dipecahkan karena hanya memiliki 25 kemungkinan kunci.
https://github.com/Brammmx/kripto-20251-230202794/blob/212c3fea67bdd6c5910763a8158156491faa2dfe/praktikum/week5-cipher-klasik/caesar%20chiper.png

Vigenère Cipher lebih kuat karena menggunakan kunci kata, tetapi masih dapat diserang dengan analisis pola (misal Kasiski test).
https://github.com/Brammmx/kripto-20251-230202794/blob/212c3fea67bdd6c5910763a8158156491faa2dfe/praktikum/week5-cipher-klasik/Vigen%C3%A8re%20Cipher.png

Transposisi Cipher tidak mengubah karakter plaintext, hanya urutannya — kombinasi substitusi dan transposisi menghasilkan cipher yang lebih kuat.
https://github.com/Brammmx/kripto-20251-230202794/blob/212c3fea67bdd6c5910763a8158156491faa2dfe/praktikum/week5-cipher-klasik/transposisi%20cipher.png

## 7. Jawaban Pertanyaan
1. Apa kelemahan utama algoritma Caesar dan Vigenère Cipher?
Keduanya rentan terhadap analisis frekuensi karena pola huruf tetap terlihat dalam ciphertext.

2. Mengapa cipher klasik mudah diserang dengan analisis frekuensi?
Karena distribusi huruf dalam ciphertext mirip dengan bahasa alami, sehingga pola huruf sering muncul secara berulang.

3. Bandingkan substitusi vs transposisi.

Substitusi: mengganti huruf dengan huruf lain, pola urutan tetap.
Transposisi: mempertahankan huruf tetapi mengubah urutannya.
Kombinasi keduanya membentuk cipher modern yang lebih kuat.

## 8. Kesimpulan
 Cipher klasik seperti Caesar, Vigenère, dan Transposisi menjadi dasar penting dalam pembelajaran kriptografi. Meskipun lemah terhadap serangan modern, algoritma ini memperkenalkan konsep dasar enkripsi, dekripsi, dan penggunaan kunci simetris yang menjadi pondasi bagi sistem kriptografi modern.
## 9. Daftar Pustaka
 1.  Stallings, W. (2017). Cryptography and Network Security: Principles and Practice.

 2. Katz, J., & Lindell, Y. (2015). Introduction to Modern Cryptography.

 3. Modul Praktikum Kriptografi Minggu ke-5: Cipher Klasik (Caesar, Vigenère, Transposisi).

## 10. Commit Log
 commit 9d4e31f
Author: Bramby Dida Baskara <brambydida@github.com>
Date:   2025-11-04

    week5-cipher-klasik: implementasi Caesar, Vigenère, dan Transposisi Cipher beserta laporan

