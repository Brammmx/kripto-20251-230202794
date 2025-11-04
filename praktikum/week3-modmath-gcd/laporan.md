# Laporan Praktikum Kriptografi
Minggu ke-: 3 
Topik: [Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)]  
Nama: [Bramby Dida Baskara]  
NIM: [230202794]  
Kelas: [5 IKRA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Menyelesaikan operasi aritmetika modular.
Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.

---

## 2. Dasar Teori
Modular arithmetic adalah sistem perhitungan yang bekerja berdasarkan sisa hasil bagi suatu bilangan terhadap bilangan modulus tertentu. Dua bilangan dikatakan kongruen jika memiliki sisa pembagian yang sama terhadap modulus yang digunakan, ditulis sebagai 𝑎≡𝑏 (mod 𝑛) a≡b (modn). Konsep ini banyak digunakan dalam kriptografi karena memungkinkan operasi pada bilangan besar tetap efisien dan aman, serta menjadi dasar dari algoritma seperti RSA dan Diffie-Hellman. Greatest Common Divisor (GCD) atau Faktor Persekutuan Terbesar adalah bilangan terbesar yang dapat membagi dua bilangan tanpa sisa. Perhitungannya umumnya dilakukan dengan Algoritma Euclidean yang cepat dan sederhana. Dalam kriptografi, GCD digunakan untuk memastikan dua bilangan bersifat relatif prima, sehingga memungkinkan perhitungan invers modular yang penting dalam pembentukan kunci publik dan privat pada sistem seperti RSA.
## 3. Alat dan Bahan  
- Git dan akun GitHub  
- Visual Studio Code

## 4. Langkah Percobaan
1. Membuat folder praktikum/week3-modmath-gcd/.

2. Membuat file modular_math.py di dalam folder src/.

3. Menuliskan fungsi aritmetika modular, GCD, invers modular, dan logaritma diskrit.

4.  Menjalankan program dengan perintah: python src/modular_math.py
5. Menyimpan hasil eksekusi ke dalam folder

---

## 5. Source Code
# Aritmetika Modular
def mod_add(a, b, n): return (a + b) % n
def mod_sub(a, b, n): return (a - b) % n
def mod_mul(a, b, n): return (a * b) % n
def mod_exp(base, exp, n): return pow(base, exp, n)

print("7 + 5 mod 12 =", mod_add(7, 5, 12))
print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
print("7^128 mod 13 =", mod_exp(7, 128, 13))

# GCD (Algoritma Euclidean)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("gcd(54, 24) =", gcd(54, 24))

# Extended Euclidean Algorithm & Invers Modular
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n

print("Invers 3 mod 11 =", modinv(3, 11))

# Logaritma Diskrit
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))


## 6. Hasil dan Pembahasan
7 + 5 mod 12 = 0
7 * 5 mod 12 = 11
7^128 mod 13 = 3
gcd(54, 24) = 6
Invers 3 mod 11 = 4
3^x ≡ 4 (mod 7), x = 4

| Operasi               | Input           | Output |
| --------------------- | --------------- | ------ |
| Penjumlahan modular   | 7 + 5 mod 12    | 0      |
| Perkalian modular     | 7 × 5 mod 12    | 11     |
| Eksponensiasi modular | 7¹²⁸ mod 13     | 3      |
| GCD                   | (54, 24)        | 6      |
| Invers modular        | 3 mod 11        | 4      |
| Logaritma diskrit     | 3^x ≡ 4 (mod 7) | x = 4  |

Pembahasan:
Semua hasil sesuai dengan teori aritmetika modular. Nilai invers modular diperoleh menggunakan algoritma Euclidean, sedangkan logaritma diskrit berhasil ditemukan dengan metode brute-force. Tidak ditemukan error selama eksekusi.
# Aritmetika Modular
https://github.com/Brammmx/kripto-20251-230202794/blob/62d8644a93abcb1ffc04cdab7964b13312182109/praktikum/week3-modmath-gcd/aritmatika%20modular.png
# GCD (Algoritma Euclidean)
https://github.com/Brammmx/kripto-20251-230202794/blob/abc02cb18c6e8e5c577a0d54d7b2324494a54e25/praktikum/week3-modmath-gcd/GCD.png

# Extended Euclidean Algorithm & Invers Modular
https://github.com/Brammmx/kripto-20251-230202794/blob/8d65b16fadb3b60115c4941f43a08aceec28c8f7/praktikum/week3-modmath-gcd/Extended%20Euclidean%20Algorithm%20%26%20Invers%20Modular.png
# Logaritma Diskrit
https://github.com/Brammmx/kripto-20251-230202794/blob/f96e2e7b45b03e3f04ca302d8ba17db4d4a037df/praktikum/week3-modmath-gcd/Logaritma%20Diskrit.png

## 7. Jawaban Pertanyaan
Peran aritmetika modular dalam kriptografi:
Menjadi dasar operasi pada sistem kunci publik seperti RSA dan Diffie-Hellman, karena menjamin operasi dilakukan dalam ruang terbatas (finite field).

Pentingnya invers modular:
Digunakan dalam perhitungan kunci privat pada algoritma RSA dan untuk proses dekripsi.

Tantangan logaritma diskrit:
Sulit diselesaikan untuk bilangan besar, karena tidak ada algoritma efisien yang dapat menemukan 
𝑥
x dengan cepat tanpa brute-force.
---

## 8. Kesimpulan
Melalui praktikum ini, mahasiswa dapat memahami konsep dasar aritmetika modular, GCD, invers modular, dan logaritma diskrit.
Konsep-konsep ini merupakan pondasi utama dalam berbagai sistem kriptografi modern seperti RSA dan Diffie-Hellman.
---

## 9. Daftar Pustaka
Katz, J., & Lindell, Y. Introduction to Modern Cryptography.

Stallings, W. Cryptography and Network Security.

Modul Praktikum Kriptografi Minggu 3 – “Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)”.

---

## 10. Commit Log
commit 9a8b1f2
Author: Bramby Dida Baskara <brambydida@example.com>
Date:   2025-11-03

    week3-modmath-gcd: implementasi modular arithmetic, GCD, dan logaritma diskrit

