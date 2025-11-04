# Laporan Praktikum Kriptografi
Minggu ke-: 4 
Topik: [Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)]  
Nama: [Bramby Dida Baskara]  
NIM: [230202794]  
Kelas: [5 IKRA]  

---

## 1. Tujuan
1. Menyelesaikan perhitungan sederhana terkait entropi kunci.
2. Menggunakan teorema Euler pada contoh perhitungan modular & invers.
3. Menghitung unicity distance untuk ciphertext tertentu.
4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.

---

## 2. Dasar Teori
Entropi (Entropy) dalam kriptografi menggambarkan tingkat ketidakpastian atau acak dari sebuah kunci. Semakin besar nilai entropi suatu ruang kunci (𝐻(𝐾)H(K)), semakin sulit bagi penyerang untuk menebak kunci tersebut secara acak. Entropi dihitung menggunakan rumus:
                 H(K)=log2​∣K∣
di mana 
∣K∣ adalah jumlah total kemungkinan kunci. Misalnya, Caesar Cipher memiliki 26 kemungkinan kunci sehingga 
H(K)=log2 26≈4.7 bit, sedangkan AES-128 memiliki ruang kunci 
2 pangkat (128) yang berarti entropinya 128 bit — sangat besar dan hampir mustahil ditebak dengan brute force.
Unicity Distance (U) adalah ukuran jumlah minimal ciphertext yang diperlukan untuk dapat secara unik menentukan plaintext dan kunci yang digunakan. Nilai ini dihitung dengan rumus:
         U=H(K) / R⋅log2​∣A∣​
dengan 𝑅 adalah redundansi bahasa dan ∣A∣ ukuran alfabet. Semakin besar unicity distance, semakin sulit untuk memecahkan ciphertext hanya dari hasil observasi.
 
 Brute Force Attack adalah metode serangan paling sederhana, di mana penyerang mencoba semua kemungkinan kunci hingga menemukan yang benar. Waktu serangan bergantung pada ukuran ruang kunci dan kecepatan komputasi. Meskipun sederhana, metode ini tetap relevan, terutama terhadap sistem dengan ruang kunci kecil seperti cipher klasik.
 
## 3. Alat dan Bahan
Git dan akun GitHub

---

## 4. Langkah Percobaan
1. Membuat folder:
   praktikum/week4-entropy-unicity/
├─ src/
├─ screenshots/
└─ laporan.md
2. Membuat file entropy_unicity.py di folder src/.

3. Menuliskan kode program untuk menghitung entropi, unicity distance, dan estimasi waktu brute force.

4. Menjalankan program dengan perintah:
   python entropy_unicity.py
5. Menyimpan hasil eksekusi ke dalam folder screenshots/.

6. Melakukan commit ke GitHub dengan pesan week4-entropy-unicity.


## 5. Source Code
  import math

# Menghitung entropi kunci
def entropy(keyspace_size):
    return math.log2(keyspace_size)

# Menghitung unicity distance
def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

# Estimasi waktu brute force
def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600 * 24)
    return days

# Contoh perhitungan
HK_caesar = entropy(26)
HK_aes = entropy(2**128)

print("Entropy ruang kunci Caesar Cipher =", HK_caesar, "bit")
print("Entropy ruang kunci AES-128 =", HK_aes, "bit")

print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK_caesar))
print("Unicity Distance untuk AES-128 =", unicity_distance(HK_aes))

print("Waktu brute force Caesar Cipher =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")

## 6. Hasil dan Pembahasan
| Cipher        | Entropy (bit) | Unicity Distance | Estimasi Brute Force (hari) |
| ------------- | ------------- | ---------------- | --------------------------- |
| Caesar Cipher | 4.7           | ~0.41            | 0.0000003                   |
| AES-128       | 128           | ~11.22           | 3.4 × 10³⁰                  |

1. Analisis:
Caesar Cipher memiliki entropi yang sangat rendah, artinya ruang kunci sangat kecil dan mudah dipecahkan dengan brute force. Sebaliknya, AES-128 memiliki entropi 128 bit, menjadikannya hampir mustahil dipecahkan dengan cara brute force bahkan dengan komputer tercepat sekalipun.

2. Error Handling: Tidak ditemukan error dalam eksekusi program.

hasil eksekusi entropy:
https://github.com/Brammmx/kripto-20251-230202794/blob/f082b19fd741499eeb3964bf5c570595697d39d5/praktikum/week4-entropy-unicity/hasil%20vs%20code.png
https://github.com/Brammmx/kripto-20251-230202794/blob/f082b19fd741499eeb3964bf5c570595697d39d5/praktikum/week4-entropy-unicity/entropy.png

## 7. Jawaban Pertanyaan
1. Apa arti dari nilai entropy dalam konteks kekuatan kunci?
Entropy menggambarkan ukuran ketidakpastian dari kunci. Semakin besar nilai entropi, semakin kuat dan acak kunci tersebut.

2. Mengapa unicity distance penting dalam menentukan keamanan suatu cipher?
Karena unicity distance menunjukkan seberapa banyak ciphertext yang diperlukan agar serangan analisis kriptografi dapat menemukan kunci secara pasti. Nilai unicity distance tinggi berarti cipher lebih aman.

3. Mengapa brute force masih menjadi ancaman meskipun algoritma sudah kuat?
Karena brute force adalah metode universal yang selalu bisa dilakukan, hanya saja efektivitasnya bergantung pada ruang kunci dan kekuatan komputasi.

## 8. Kesimpulan
Dari percobaan ini dapat disimpulkan bahwa semakin besar entropi ruang kunci, semakin tinggi pula keamanan cipher. Nilai unicity distance membantu memperkirakan seberapa besar data yang diperlukan untuk memecahkan cipher secara unik. Cipher modern seperti AES memiliki entropi yang sangat besar sehingga serangan brute force menjadi tidak praktis dilakukan.

## 9. Daftar Pustaka
1. Stallings, W. (2017). Cryptography and Network Security: Principles and Practice.

2. Katz, J., & Lindell, Y. (2015). Introduction to Modern Cryptography.

3. Modul Praktikum Kriptografi Minggu ke-4: Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force).

## 10. Commit Log
commit 8f32a7b
Author: Bramby Dida Baskara <brambydida@github.com>
Date:   2025-11-03

    week4-entropy-unicity: implementasi perhitungan entropi, unicity distance, dan simulasi brute force
