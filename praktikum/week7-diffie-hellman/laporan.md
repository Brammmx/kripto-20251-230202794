# Laporan Praktikum Kriptografi
Minggu ke-: 7 
Topik: [Diffie-Hellman Key Exchange]  
Nama: [Bramby Dida Baskara]  
NIM: [230202794]  
Kelas: [5 IKRA]  



## 1. Tujuan
1. Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).
## 2. Dasar Teori
Protokol Diffie-Hellman Key Exchange adalah metode untuk dua pihak (misalnya Alice dan Bob) agar dapat menyepakati sebuah kunci rahasia bersama melalui saluran komunikasi publik. Mekanisme ini didasarkan pada perhitungan eksponensial modular dan kesulitan menyelesaikan logaritma diskrit, sehingga secara praktis aman dari peretas yang hanya mengamati nilai publik.

Konsep utamanya: kedua pihak sepakat pada dua nilai publik — bilangan prima besar p dan generator g. Masing-masing pihak memiliki kunci privat rahasia (a dan b) lalu menghasilkan kunci publik (A = g^a mod p dan B = g^b mod p). Setelah saling bertukar kunci publik, keduanya menghitung kunci rahasia yang sama:
K = (B^a mod p) = (A^b mod p).

Keamanan Diffie-Hellman bergantung pada sulitnya menemukan nilai privat a atau b dari hasil eksponensial modular — inilah inti dari masalah logaritma diskrit. Namun, protokol dasar ini tidak menyediakan autentikasi, sehingga rentan terhadap serangan Man-in-the-Middle (MITM) jika tidak dikombinasikan dengan metode autentikasi tambahan seperti tanda tangan digital atau sertifikat.
## 3. Alat dan Bahan
- Visual Studio Code / editor lain  
- Git dan akun GitHub  

## 4. Langkah Percobaan
1. Membuat folder praktikum/week7-diffie-hellman/ dengan struktur:
 ├─ src/
├─ screenshots/
└─ laporan.md
2. Membuat file diffie_hellman.py di folder src/.

3. Menyalin kode simulasi dari panduan praktikum.

4. Menjalankan program dengan perintah:
   python src/diffie_hellman.py
5. Mencatat hasil eksekusi program (nilai kunci bersama).

6. Melakukan analisis serangan MITM dengan menambahkan pihak ketiga (Eve) yang memodifikasi kunci publik.
## 5. Source Code
Code:
import random

# parameter publik
p = 23  # bilangan prima
g = 5   # generator

# kunci privat masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# kunci publik
A = pow(g, a, p)
B = pow(g, b, p)

# pertukaran kunci publik dan pembentukan kunci bersama
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Nilai publik (p, g):", p, g)
print("Kunci publik Alice (A):", A)
print("Kunci publik Bob (B):", B)
print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)

Simulasi MITM (Opsional):
Code:
# Eve menyadap dan mengganti kunci publik
e = random.randint(1, p-1)
E = pow(g, e, p)

# Alice berpikir dia menerima B (padahal E)
shared_A = pow(E, a, p)
# Bob berpikir dia menerima A (padahal E)
shared_B = pow(E, b, p)

print("\n=== Simulasi MITM ===")
print("Kunci Alice - Eve:", shared_A)
print("Kunci Bob - Eve  :", shared_B)


## 6. Hasil dan Pembahasan
Hasil eksekusi contoh (acak setiap kali dijalankan):
Nilai publik (p, g): 23 5
Kunci publik Alice (A): 8
Kunci publik Bob (B): 19
Kunci bersama Alice : 2
Kunci bersama Bob   : 2

Hasil menunjukkan kunci bersama Alice dan Bob identik, sesuai teori Diffie-Hellman.
Pada simulasi MITM, terlihat bahwa kunci antara Alice-Eve dan Bob-Eve berbeda, namun Eve mengetahui keduanya — menandakan kebocoran kunci karena tidak adanya autentikasi.

hasil ekskusi code diffie_hellman
https://github.com/Brammmx/kripto-20251-230202794/blob/89e0da7497ee5b5a07ce385a329bb5c856a85694/praktikum/week7-diffie-hellman/Diffie_helman.png

Hasil Simulasi MITM (Opsional):
https://github.com/Brammmx/kripto-20251-230202794/blob/a58dd6b7025806b1562be462e643ba73c5d203e8/praktikum/week7-diffie-hellman/Simulasi%20MITM.png

## 7. Jawaban Pertanyaan
1. Mengapa Diffie-Hellman memungkinkan pertukaran kunci di saluran publik?
Karena keamanan didasarkan pada masalah logaritma diskrit, sehingga meskipun nilai publik diketahui, pihak luar tidak dapat menghitung kunci rahasia dengan mudah.

2. Apa kelemahan utama protokol Diffie-Hellman murni?
Tidak adanya mekanisme autentikasi, sehingga rentan terhadap serangan Man-in-the-Middle.

3. Bagaimana cara mencegah serangan MITM pada protokol ini?
Dengan menambahkan autentikasi digital seperti digital signature, certificate authority (CA), atau menggabungkan dengan protokol keamanan seperti TLS/SSL.

## 8. Kesimpulan
Dari percobaan, dapat disimpulkan bahwa algoritma Diffie-Hellman memungkinkan dua pihak untuk menyepakati kunci rahasia melalui saluran publik dengan aman secara matematis. Namun, tanpa autentikasi tambahan, protokol ini rentan terhadap serangan MITM. Penerapan praktis biasanya digabung dengan sertifikat digital untuk menjamin keaslian pihak yang berkomunikasi.

## 9. Daftar Pustaka
Stallings, W. (2017). Cryptography and Network Security: Principles and Practice. Pearson.

Katz, J., & Lindell, Y. (2020). Introduction to Modern Cryptography. CRC Press.

Diffie, W., & Hellman, M. (1976). New Directions in Cryptography. IEEE Transactions on Information Theory.

## 10. Commit Log
commit 8b3d9f2
Author: Bramby Dida Baskara <bramby@example.com>
Date:   2025-11-04

    week7-diffie-hellman: implementasi simulasi Diffie-Hellman dan analisis MITM

