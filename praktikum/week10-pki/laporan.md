# Laporan Praktikum Kriptografi
Minggu ke-: 10  
Topik: [Public Key Infrastructure (PKI & Certificate Authority)]  
Nama: [Bramby Dida Baskara]  
NIM: [230202794]  
Kelas: [5 IKRA]  

---

## 1. Tujuan
Setelah melaksanakan praktikum ini, mahasiswa diharapkan mampu:

Membuat sertifikat digital sederhana (self-signed).

Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.

Mengevaluasi fungsi PKI dalam menjamin komunikasi yang aman (contoh: HTTPS, TLS).

## 2. Dasar Teori
Public Key Infrastructure (PKI) adalah kerangka kerja yang terdiri dari kebijakan, prosedur, dan sistem yang diperlukan untuk mengelola sertifikat digital dan public key. PKI memastikan bahwa public key tertentu benar-benar milik entitas tertentu (individu, server, atau organisasi).

Komponen utama PKI adalah Certificate Authority (CA). CA adalah pihak ketiga tepercaya yang bertanggung jawab untuk menerbitkan, memperbarui, dan mencabut sertifikat digital. CA memverifikasi identitas pemohon sertifikat dan kemudian menandatangani sertifikat tersebut menggunakan private key-nya. Tanda tangan digital ini memungkinkan pihak lain (seperti web browser) untuk memverifikasi keaslian dan integritas sertifikat.

Sertifikat digital, seperti sertifikat X.509, mengikat public key dengan informasi identitas pemiliknya, dan ditandatangani oleh CA. Dalam konteks HTTPS/TLS, PKI sangat penting untuk:

Autentikasi: Memverifikasi identitas server (web browser memverifikasi sertifikat server).

Kerahasiaan: Memfasilitasi pertukaran kunci untuk enkripsi sesi.

Integritas: Memastikan data tidak dimodifikasi selama transmisi.

## 3. Alat dan Bahan
- Python  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  

## 4. Langkah Percobaan
Membuat struktur folder praktikum/week10-pki/src/ dan file src/pki_cert.py.

Menginstal library cryptography dan pyopenssl dengan perintah pip install cryptography pyopenssl.

Menyalin kode program dari panduan praktikum ke dalam file src/pki_cert.py. Kode ini berfungsi untuk menghasilkan pasangan kunci RSA dan membuat sertifikat digital self-signed.

Menjalankan program dengan perintah python src/pki_cert.py di terminal.

Memeriksa keberadaan file cert.pem di root folder.

Mengambil screenshot hasil eksekusi program dan menyimpannya di screenshots/hasil.png.

Melengkapi file laporan.md ini dengan hasil, pembahasan, dan jawaban pertanyaan diskusi.

Melakukan commit Git dengan pesan week10-pki.

## 5. Source Code
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

# Generate key pair
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Buat subject & issuer (CA sederhana = self-signed)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
])

# Buat sertifikat
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))
    .sign(key, hashes.SHA256())
)

# Simpan sertifikat
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Sertifikat digital berhasil dibuat: cert.pem")
print("Key size:", key.key_size)
print("Common Name:", subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value)
print("Valid Until:", cert.not_valid_after)

## 6. Hasil dan Pembahasan
Hasil Eksekusi Program: Program pki_cert.py dijalankan dan berhasil membuat file cert.pem.

Pembahasan: Program berhasil menghasilkan pasangan kunci RSA 2048-bit dan membuat sertifikat X.509 self-signed yang valid selama satu tahun. Dalam konteks ini, entitas yang membuat sertifikat (subject) sama dengan entitas yang menandatanganinya (issuer), yaitu "UPB Kriptografi, ID, CN=example.com". Ini mensimulasikan CA paling sederhana, di mana sertifikat dipercaya karena ditandatangani oleh pembuatnya sendiri. File cert.pem berisi sertifikat dalam format PEM (Base64-encoded X.509).

## 7. Jawaban Pertanyaan
1. Apa fungsi utama Certificate Authority (CA)?
Fungsi utama Certificate Authority (CA) adalah bertindak sebagai pihak ketiga tepercaya (Trusted Third Party/TTP) yang bertanggung jawab untuk:

Menerbitkan Sertifikat Digital: Memverifikasi identitas pemohon dan menerbitkan sertifikat yang mengikat public key mereka dengan identitas tersebut.

Menjamin Keaslian: Menandatangani sertifikat menggunakan private key-nya sendiri, yang memungkinkan pengguna akhir (misalnya, browser) memverifikasi bahwa sertifikat tersebut benar-benar dikeluarkan oleh CA yang sah dan tidak diubah.

Mengelola Siklus Hidup Sertifikat: Memperbarui dan mencabut sertifikat yang telah kedaluwarsa atau dikompromikan (melalui Certificate Revocation List / CRL atau OCSP).

2. Mengapa self-signed certificate tidak cukup untuk sistem produksi?
Self-signed certificate tidak cukup untuk sistem produksi karena:

Kurangnya Kepercayaan (Trust): Dalam sistem produksi global (seperti web), browser atau sistem operasi hanya akan secara otomatis mempercayai sertifikat yang ditandatangani oleh Root CA tepercaya yang telah ditanam (embedded) di dalamnya. Karena self-signed certificate ditandatangani oleh entitas itu sendiri, tidak ada rantai kepercayaan yang menghubungkannya ke Root CA global.

Masalah Autentikasi: Pengguna akhir tidak memiliki mekanisme independen dan tepercaya untuk memverifikasi bahwa self-signed certificate benar-benar milik entitas yang diklaim (berpotensi terkena serangan man-in-the-middle / MITM).

Peringatan Keamanan: Pengguna browser akan selalu melihat peringatan keamanan (misalnya, "Koneksi Anda tidak privat") karena sertifikat tersebut tidak dapat divalidasi oleh CA yang dikenal.

3. Bagaimana PKI mencegah serangan MITM dalam komunikasi TLS/HTTPS?
PKI mencegah serangan Man-in-the-Middle (MITM) dalam komunikasi TLS/HTTPS melalui proses verifikasi sertifikat:

Autentikasi Server: Saat klien (misalnya, browser) terhubung ke server, server mengirimkan sertifikat digitalnya. Sertifikat ini ditandatangani oleh CA tepercaya.

Verifikasi Tanda Tangan: Klien menggunakan public key dari CA untuk memverifikasi tanda tangan pada sertifikat server. Jika tanda tangan valid, klien yakin bahwa sertifikat tersebut sah dan benar-benar dikeluarkan untuk server yang diklaim.

Mendeteksi Penyusup: Jika penyerang MITM mencoba mencegat koneksi dan menyajikan sertifikat palsu yang ditandatangani sendiri (atau ditandatangani oleh CA yang tidak tepercaya), verifikasi tanda tangan akan gagal. Klien akan mendeteksi ketidaksesuaian ini (karena public key CA yang tepercaya tidak cocok dengan tanda tangan sertifikat palsu) dan segera menghentikan koneksi atau menampilkan peringatan keamanan, sehingga mencegah penyerang mendapatkan kunci sesi.

## 8. Kesimpulan
Praktikum ini berhasil mensimulasikan pembuatan sertifikat digital self-signed sederhana menggunakan library cryptography Python. Self-signed certificate adalah dasar dari sertifikat digital, namun tidak memadai untuk sistem produksi karena kurangnya rantai kepercayaan dari Certificate Authority (CA) global. PKI, melalui peran CA, sangat penting untuk komunikasi aman seperti HTTPS/TLS, karena menyediakan mekanisme autentikasi tepercaya yang mencegah serangan Man-in-the-Middle dengan menjamin keaslian public key server.

## 9. Daftar Pustaka
Stallings, W. (2017). Cryptography and Network Security: Principles and Practice (7th ed.). Pearson. (Materi rujukan Bab 14)

Panduan Praktikum Minggu 10: Public Key Infrastructure (PKI & Certificate Authority).
## 10. Commit Log
commit [hash-commit-terakhir-anda]
Author: Bramby Dida Baskara <[brambybaskara8@gmail.com]>
Date:   [Tanggal-Commit]

    week10-pki
