# Laporan Praktikum Kriptografi
Minggu ke-: 2 
Topik: [Cryptosystem (Komponen, Enkripsi & Dekripsi, Simetris & Asimetris)]  
Nama: [Bramby Dida Baskara]  
NIM: [230202794]  
Kelas: [5 IKRA]  

---

## 1. Tujuan
Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).
Menjelaskan proses enkripsi dan dekripsi sederhana.
Mengklasifikasikan jenis kriptosistem menjadi simetris dan asimetris.
---

## 2. Dasar Teori
Kriptografi merupakan ilmu yang mempelajari cara melindungi pesan agar hanya pihak yang berwenang dapat membacanya. Pesan asli disebut plaintext, hasil enkripsi disebut ciphertext, sedangkan proses untuk mengubah plaintext menjadi ciphertext disebut enkripsi, dan kebalikannya disebut dekripsi.

Suatu kriptosistem terdiri atas beberapa komponen utama, yaitu algoritma enkripsi, algoritma dekripsi, kunci (key), plaintext, dan ciphertext. Kunci berperan penting dalam menentukan keamanan sistem, karena algoritma umumnya bersifat publik.

Terdapat dua jenis utama kriptografi:

Kriptografi Simetris, di mana kunci enkripsi dan dekripsi sama (contohnya Caesar Cipher, AES, DES).

Kriptografi Asimetris, yang menggunakan dua kunci berbeda, yaitu kunci publik dan kunci privat (contohnya RSA, ECC).

---

## 3. Alat dan Bahan
- Visual Studio Code / editor lain  
- Git dan akun GitHub  

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
Sebutkan komponen utama dalam sebuah kriptosistem.
Apa kelebihan dan kelemahan sistem simetris dibandingkan asimetris?
Mengapa distribusi kunci menjadi masalah utama dalam kriptografi simetris?

Komponen utama kriptosistem: plaintext (data asli), ciphertext (data terenkripsi), algoritma (prosedur enkripsi/dekripsi), dan kunci (key) yang mengontrol proses.

Sistem simetris lebih cepat dan efisien untuk data besar, tetapi membutuhkan distribusi kunci yang aman dan rentan jika kunci bocor. Sistem asimetris lebih aman karena menggunakan kunci publik dan privat, tapi lebih lambat dan kurang efisien untuk data besar.

Distribusi kunci menjadi masalah utama pada kriptografi simetris karena kunci yang sama harus dikirim secara aman; jika jatuh ke pihak tidak berwenang, keamanan data terancam.---

## 8. Kesimpulan
Cryptosystem adalah sistem untuk menjaga keamanan data melalui proses enkripsi (mengubah plaintext menjadi ciphertext) dan dekripsi (mengembalikannya ke bentuk semula). Komponennya meliputi plaintext, ciphertext, algoritma, dan kunci.
Terdapat dua jenis utama:

Simetris: menggunakan satu kunci yang sama untuk enkripsi dan dekripsi.

Asimetris: menggunakan dua kunci berbeda (publik dan privat).
Secara keseluruhan, cryptosystem penting untuk melindungi data dan komunikasi dari akses tidak sah.

---

## 9. Daftar Pustaka
IBM. Cryptography Types. IBM Think. Diakses dari: https://www.ibm.com/id-id/think/topics/cryptography-types

IBM. Asymmetric Encryption. IBM Think. Diakses dari: https://www.ibm.com/id-id/think/topics/asymmetric-encryption

ResearchGate. Kriptografi: Teknik Keamanan Data. Diakses dari: https://www.researchgate.net/publication/373655214_Kriptografi_Teknik_Keamanan_Data

PusatSSL. Enkripsi Simetris dan Asimetris. Diakses dari: https://pusatssl.com/order/knowledgebase/16/Enkripsi-Simetris-dan-Asimetris.html

Digilib STEKOM. Modern Kriptografi. Diakses dari: https://digilib.stekom.ac.id/assets/dokumen/ebook/feb_B8KFO97sXQEkipqdykDJ67yV7946c7deiDGg8j2FlAjTo98D-33QS5c_1721377496.pdf

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit 514ef518250f5c5afb45c12a78e8f1e1d54de351 (HEAD -> main, origin/main, origin/HEAD)
Author: bramby dida baskara <brambybaskara8@gmail.com>
Date:   Tue Oct 14 16:08:38 2025 +0700

    week2-cryptosystem
```
