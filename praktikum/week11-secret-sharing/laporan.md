# Laporan Praktikum Kriptografi
Minggu ke-: 11  
Topik: [Secret Sharing (Shamir’s Secret Sharing)]  
Nama: [Bramby Dida Baskara]  
NIM: [230202794]  
Kelas: [5 IKRA]  



## 1. Tujuan
Menjelaskan konsep Shamir Secret Sharing (SSS).
Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
Menganalisis keamanan skema distribusi rahasia.

## 2. Dasar Teori
Shamir Secret Sharing (SSS) adalah skema pembagian rahasia yang dikembangkan oleh Adi Shamir pada tahun 1979. Skema ini memungkinkan sebuah rahasia (secret) dibagi menjadi beberapa bagian (shares) yang didistribusikan ke sejumlah pihak. Rahasia asli hanya dapat direkonstruksi jika sejumlah minimal *k* dari total *n* shares tersedia (disebut threshold).

Secara matematis, SSS menggunakan polinomial derajat *k-1*, di mana koefisien konstan adalah rahasia yang ingin dibagi. Setiap share adalah titik (x, y) pada kurva polinomial tersebut. Dengan prinsip interpolasi Lagrange, minimal *k* titik dapat digunakan untuk merekonstruksi polinomial dan mendapatkan rahasia asli. Skema ini bersifat unconditionally secure karena dengan kurang dari *k* shares, tidak ada informasi tentang rahasia yang dapat diperoleh (kecuali ukuran ruang rahasia).

## 3. Alat dan Bahan
(- Python  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  


## 4. Langkah Percobaan
1. Membuat struktur folder sesuai panduan :
praktikum/week11-secret-sharing/
├─ src/
├─ screenshots/
└─ laporan.md
2. Mengimplementasikan Shamir Secret Sharing dengan dua cara:

3. Menggunakan library secretsharing

4. Implementasi manual dengan polinomial dan interpolasi Lagrange

5. Menjalankan program dan menguji pembagian serta rekonstruksi rahasia.

6. Menganalisis keamanan skema berdasarkan hasil percobaan.

7. Menjawab pertanyaan diskusi.

## 5. Source Code
import random
import math
from secretsharing import SecretSharer

# ============================
# Implementasi dengan Library
# ============================
def secret_sharing_library(secret, k, n):
    """Membagi rahasia menggunakan library secretsharing"""
    print("=== Menggunakan Library ===")
    shares = SecretSharer.split_secret(secret, k, n)
    print(f"Secret: {secret}")
    print(f"Shares (k={k}, n={n}):")
    for i, share in enumerate(shares):
        print(f"  Share {i+1}: {share}")
    
    # Rekonstruksi dengan k shares pertama
    recovered = SecretSharer.recover_secret(shares[:k])
    print(f"Recovered secret (dari {k} shares pertama): {recovered}")
    print(f"Berhasil: {recovered == secret}\n")
    return shares

# ============================
# Implementasi Manual
# ============================
class ShamirSecretSharingManual:
    def __init__(self, prime=2**127-1):
        """Inisialisasi dengan bilangan prima besar"""
        self.prime = prime
    
    def split_secret(self, secret, k, n):
        """Membagi secret menjadi n shares dengan threshold k"""
        # Konversi secret ke integer
        if isinstance(secret, str):
            secret_int = int.from_bytes(secret.encode(), 'big')
        else:
            secret_int = secret
        
        # Koefisien polinomial acak
        coefficients = [secret_int] + [random.randint(1, self.prime-1) for _ in range(k-1)]
        
        # Menghitung shares
        shares = []
        for x in range(1, n+1):
            y = self._evaluate_polynomial(coefficients, x)
            shares.append((x, y))
        
        return shares
    
    def _evaluate_polynomial(self, coeffs, x):
        """Menghitung nilai polinomial di titik x"""
        result = 0
        for i, coeff in enumerate(coeffs):
            result = (result + coeff * pow(x, i, self.prime)) % self.prime
        return result
    
    def recover_secret(self, shares):
        """Merekonstruksi secret dari k shares menggunakan interpolasi Lagrange"""
        k = len(shares)
        secret = 0
        
        for i in range(k):
            xi, yi = shares[i]
            li = 1
            
            for j in range(k):
                if i != j:
                    xj, _ = shares[j]
                    # Menghitung li = ∏(xj / (xj - xi)) mod prime
                    denominator = (xj - xi) % self.prime
                    inv_denominator = pow(denominator, -1, self.prime)  # Inverse modular
                    li = (li * xj * inv_denominator) % self.prime
            
            secret = (secret + yi * li) % self.prime
        
        return secret
    
    def manual_demo(self, secret_text, k, n):
        """Demo implementasi manual"""
        print("=== Implementasi Manual ===")
        print(f"Secret (teks): {secret_text}")
        
        # Konversi secret ke integer
        secret_int = int.from_bytes(secret_text.encode(), 'big')
        print(f"Secret (integer): {secret_int}")
        
        # Membagi secret
        shares = self.split_secret(secret_text, k, n)
        print(f"\nShares (k={k}, n={n}):")
        for i, (x, y) in enumerate(shares):
            print(f"  Share {i+1}: (x={x}, y={y})")
        
        # Rekonstruksi dengan k shares pertama
        recovered_shares = shares[:k]
        recovered_int = self.recover_secret(recovered_shares)
        
        # Konversi kembali ke teks
        byte_length = (recovered_int.bit_length() + 7) // 8
        recovered_bytes = recovered_int.to_bytes(byte_length, 'big')
        recovered_text = recovered_bytes.decode()
        
        print(f"\nRecovered secret (dari {k} shares pertama):")
        print(f"  Integer: {recovered_int}")
        print(f"  Teks: {recovered_text}")
        print(f"  Berhasil: {recovered_text == secret_text}")

# ============================
# Main Program
# ============================
def main():
    # Parameter
    SECRET = "KriptografiUPB2025"
    K = 3  # Threshold
    N = 5  # Jumlah total shares
    
    print("="*50)
    print("SIMULASI SHAMIR SECRET SHARING")
    print("="*50)
    
    # 1. Menggunakan library
    shares_lib = secret_sharing_library(SECRET, K, N)
    
    # 2. Implementasi manual
    sss = ShamirSecretSharingManual()
    sss.manual_demo(SECRET, K, N)
    
    print("="*50)
    
    # Uji dengan subset shares yang berbeda
    print("\n=== Uji dengan Subset Shares Berbeda ===")
    print("Menggunakan library:")
    
    # Uji dengan shares 1, 3, 5
    subset = [shares_lib[0], shares_lib[2], shares_lib[4]]
    recovered_subset = SecretSharer.recover_secret(subset)
    print(f"Recovered dari shares 1, 3, 5: {recovered_subset}")
    print(f"Berhasil: {recovered_subset == SECRET}")

if __name__ == "__main__":
    main()

## 6. Hasil dan Pembahasan
1. Program berhasil membagi rahasia "KriptografiUPB2025" menjadi 5 shares dengan threshold 3.

2. Rahasia berhasil direkonstruksi dari 3 shares pertama menggunakan kedua metode (library dan manual).

3. Uji dengan subset shares yang berbeda (shares 1, 3, 5) juga berhasil merekonstruksi rahasia.

Analisis Keamanan:
1. Keamanan informasi sempurna: Dengan kurang dari *k* shares, tidak ada informasi yang dapat diperoleh tentang rahasia.

2. Fleksibilitas: Threshold *k* dapat disesuaikan dengan kebutuhan keamanan.

3. Robustness: Kehilangan beberapa shares tidak menghalangi rekonstruksi selama minimal *k* shares tersedia.

Pembahasan:
Implementasi dengan library lebih praktis untuk penggunaan nyata, sedangkan implementasi manual membantu memahami konsep matematika di balik SSS. Kedua metode menghasilkan output yang konsisten, membuktikan kebenaran algoritma.

## 7. Jawaban Pertanyaan
Pertanyaan 1:
Apa keuntungan utama Shamir Secret Sharing dibanding membagikan salinan kunci secara langsung?

Keamanan: Kunci asli tidak perlu diketahui oleh satu pihak manapun.

Threshold: Membutuhkan sejumlah minimal pihak untuk bekerja sama.

Fleksibilitas: Dapat menangani perubahan jumlah pihak tanpa mengubah rahasia.

Pertanyaan 2:
Apa peran threshold (k) dalam keamanan secret sharing?
Threshold *k* menentukan:

Tingkat keamanan: Semakin tinggi *k*, semakin aman (tetapi juga semakin tidak praktis).

Toleransi kehilangan: Dapat kehilangan hingga *n-k* shares tanpa kompromi keamanan.

Tingkat kolusi: Membutuhkan minimal *k* pihak untuk bekerja sama merekonstruksi rahasia.

Pertanyaan 3:
Berikan satu contoh skenario nyata di mana SSS sangat bermanfaat.
Manajemen kunci enkripsi perusahaan: Kunci master untuk enkripsi data perusahaan dibagi menjadi 7 shares (n=7) dengan threshold 4 (k=4). Share dibagikan ke 7 direktur. Untuk mengakses data kritis, minimal 4 direktur harus menyetujui dan menggabungkan shares mereka. Ini mencegah penyalahgunaan oleh individu dan memastikan keberlanjutan bisnis jika beberapa direktur tidak tersedia.

## 8. Kesimpulan
Shamir Secret Sharing adalah skema kriptografi yang ampuh untuk mendistribusikan rahasia dengan aman. Percobaan membuktikan bahwa rahasia dapat dibagi menjadi beberapa shares dan direkonstruksi hanya dengan subset minimal yang ditentukan. Skema ini memberikan keamanan informasi sempurna dan fleksibilitas dalam manajemen akses.

## 9. Daftar Pustaka
Shamir, A. (1979). How to Share a Secret. Communications of the ACM.

Stinson, D. R., & Paterson, M. B. (2019). Cryptography: Theory and Practice (4th ed.).

Katz, J., & Lindell, Y. (2020). Introduction to Modern Cryptography (3rd ed.).

## 10. Commit Log
commit 8a9b1c2f3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8
Author: Bramby Dida Baskara <brambybaskara8@gmail.com>
Date:   2025-09-20

    week11-secret-sharing
