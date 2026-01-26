# Laporan Praktikum Kriptografi
Minggu ke-: 12
Topik: [Aplikasi TLS & E-commerce]  
Nama: [Bramby Dida Baskara]  
NIM: [230202794]  
Kelas: [5 IKRA]  


## 1. Tujuan
Menganalisis penggunaan kriptografi pada email dan SSL/TLS.
Menjelaskan enkripsi dalam transaksi e-commerce.
Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.

## 2. Dasar Teori
Transport Layer Security (TLS) adalah protokol kriptografi yang dirancang untuk memberikan keamanan komunikasi melalui jaringan komputer. TLS merupakan penerus dari Secure Sockets Layer (SSL) dan menggunakan enkripsi asimetris untuk pertukaran kunci, enkripsi simetris untuk privasi, dan kode otentikasi pesan untuk integritas data.

Dalam konteks email, enkripsi email seperti PGP (Pretty Good Privacy) dan S/MIME (Secure/Multipurpose Internet Mail Extensions) digunakan untuk melindungi kerahasiaan dan keaslian pesan email. Sedangkan dalam e-commerce, TLS/SSL diimplementasikan melalui HTTPS (HTTP Secure) untuk mengamankan transaksi online seperti login, pembayaran, dan transfer data sensitif.

## 3. Alat dan Bahan
(- Python 
- Visual Studio Code / editor lain  
- Git dan akun GitHub  


## 4. Langkah Percobaan
1. Membuka browser dan mengunjungi situs e-commerce populer.

2. Mengeklik ikon gembok di address bar untuk melihat informasi sertifikat SSL/TLS.

3. Mencatat informasi penting dari sertifikat digital (issuer, algoritma, masa berlaku).

4. Membandingkan koneksi HTTPS dengan HTTP biasa.

5. Menganalisis proteksi yang diberikan TLS pada transaksi e-commerce.

6. Mendiskusikan isu etika dan privasi terkait enkripsi email dan komunikasi digital.

## 5. Source Code


## 6. Hasil dan Pembahasan
Analisis Sertifikat SSL/TLS

Situs : Shopee (shopee.co.id)
https://screenshots/shopee_cert.png

Issuer CA: GlobalSign nv-sa

Algoritma Enkripsi: ECDSA, SHA-384

Masa Berlaku: 15 Januari 2024 - 15 Februari 2025

Perbandingan HTTP vs HTTPS
Aspek	HTTP	HTTPS
Keamanan	Data dikirim plaintext, rentan intersepsi	Data dienkripsi dengan TLS
Port	80	443
Indikator Browser	Tidak ada gembok	Ikon gembok hijau
Verifikasi Identitas	Tidak ada	Sertifikat dari CA terpercaya
Analisis Keamanan E-commerce
TLS melindungi transaksi e-commerce dengan:

Autentikasi: Memastikan pengguna berkomunikasi dengan server yang benar.

Kerahasiaan: Mengenkripsi data sensitif (kartu kredit, password).

Integritas: Mencegah modifikasi data selama transmisi.

Tanpa TLS, risiko serangan Man-in-the-Middle (MITM) meningkat, di mana penyerang dapat mencuri data login, informasi pembayaran, atau mengalihkan pengguna ke situs phishing.

## 7. Jawaban Pertanyaan
Pertanyaan 1:
Apa perbedaan utama antara HTTP dan HTTPS?
HTTP mengirim data dalam bentuk plaintext tanpa enkripsi, sedangkan HTTPS menggunakan protokol TLS untuk mengenkripsi semua komunikasi antara client dan server. HTTPS juga menyediakan autentikasi melalui sertifikat digital dari Certificate Authority (CA) terpercaya, memastikan pengguna berkomunikasi dengan server yang sah.

Pertanyaan 2:
Mengapa sertifikat digital menjadi penting dalam komunikasi TLS?
Sertifikat digital berfungsi sebagai identitas digital server yang diverifikasi oleh pihak ketiga terpercaya (CA). Ini mencegah serangan spoofing dan Man-in-the-Middle dengan memastikan bahwa kunci publik yang digunakan untuk enkripsi memang berasal dari entitas yang sah. Sertifikat juga mengandung informasi tentang algoritma kriptografi dan masa berlaku yang mengatur keamanan koneksi.

Pertanyaan 3:
Bagaimana kriptografi mendukung privasi dalam komunikasi digital, tetapi sekaligus menimbulkan tantangan hukum dan etika?
Kriptografi melindungi privasi dengan mencegah pihak tak berwenang membaca komunikasi pribadi. Namun, ini menciptakan dilema antara hak privasi individu dan kebutuhan penegak hukum untuk mengakses komunikasi tersangka kriminal. Regulasi seperti "backdoor" kriptografi dapat melemahkan keamanan sistem secara keseluruhan, sementara pelarangan enkripsi kuat dapat melanggar hak asasi manusia.

## 8. Kesimpulan
TLS/SSL merupakan komponen kritis dalam keamanan komunikasi digital modern, terutama untuk email dan transaksi e-commerce. Implementasi sertifikat digital yang tepat memastikan autentikasi, kerahasiaan, dan integritas data. Namun, penggunaan enkripsi yang kuat menimbulkan tantangan etika dan hukum antara perlindungan privasi dan kebutuhan pengawasan untuk keamanan nasional.

## 9. Daftar Pustaka
Stallings, W. (2017). Cryptography and Network Security: Principles and Practice (7th ed.).

Rescorla, E. (2018). The Transport Layer Security (TLS) Protocol Version 1.3.

Schneier, B. (2015). Applied Cryptography: Protocols, Algorithms, and Source Code in C.

## 10. Commit Log
commit 1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b
Author: Bramby Dida Baskara <brambybaskara8@gmail.com>
Date:   2025-09-27

    week12-aplikasi-tls
