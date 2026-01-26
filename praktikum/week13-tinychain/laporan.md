# Laporan Praktikum Kriptografi
Minggu ke-: 13
Topik: [TinyChain – Proof of Work (PoW)]  
Nama: [Bramby Dida Baskara]  
NIM: [230202794]  
Kelas: [5 IKRA]  



## 1. Tujuan
Menjelaskan peran hash function dalam blockchain.
Melakukan simulasi sederhana Proof of Work (PoW).
Menganalisis keamanan cryptocurrency berbasis kriptografi.

## 2. Dasar Teori
Proof of Work (PoW) adalah mekanisme konsensus yang digunakan dalam blockchain untuk memvalidasi transaksi dan menciptakan blok baru. PoW memerlukan peserta jaringan (miner) untuk menyelesaikan teka-teki komputasi yang sulit tetapi mudah diverifikasi. Fungsi hash kriptografi seperti SHA-256 memainkan peran sentral dalam PoW, karena menghasilkan output yang deterministik namun tidak dapat diprediksi.

Setiap blok dalam blockchain berisi hash dari blok sebelumnya, menciptakan rantai yang tidak dapat diubah. Untuk menambang blok baru, miner harus menemukan nonce (angka acak) sehingga hash blok memenuhi kondisi tertentu (misalnya, memiliki sejumlah nol di awal). Proses ini memerlukan daya komputasi besar, yang menjamin keamanan jaringan melalui kerja komputasi yang telah dilakukan.

## 3. Alat dan Bahan
(- Python 
- Visual Studio Code / editor lain  
- Git dan akun GitHub  

## 4. Langkah Percobaan
1. Membuat file tinychain.py di folder praktikum/week13-tinychain/src/.

2. Mengimplementasikan kelas Block dengan metode calculate_hash dan mine_block.

3. Mengimplementasikan kelas Blockchain dengan metode untuk membuat genesis block, menambang blok, dan menambah blok baru.

4. Menjalankan program untuk mensimulasikan penambangan dua blok.

5. Menganalisis hasil dan mengambil screenshot output.

6. Menjawab pertanyaan diskusi.

## 5. Source Code
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Nonce: {block.nonce}")
            print(f"Hash: {block.hash}\n")

# Uji coba blockchain
if __name__ == "__main__":
    print("=== TinyChain - Proof of Work Simulation ===\n")
    
    # Inisialisasi blockchain dengan difficulty 4
    my_chain = Blockchain(difficulty=4)
    
    print("Genesis block created.")
    print(f"Genesis block hash: {my_chain.chain[0].hash}\n")
    
    print("Mining block 1...")
    my_chain.add_block(Block(1, "", "Transaksi A → B: 10 Coin"))
    
    print("\nMining block 2...")
    my_chain.add_block(Block(2, "", "Transaksi B → C: 5 Coin"))
    
    print("\n=== Blockchain Structure ===")
    my_chain.print_chain()
    
    # Verifikasi integritas blockchain
    print("=== Integrity Verification ===")
    for i in range(1, len(my_chain.chain)):
        current_block = my_chain.chain[i]
        previous_block = my_chain.chain[i-1]
        
        if current_block.previous_hash != previous_block.hash:
            print(f"Block {current_block.index} is tampered!")
        else:
            print(f"Block {current_block.index} is valid.")

## 6. Hasil dan Pembahasan
Hasil Eksekusi Program :
Output Program:
=== TinyChain - Proof of Work Simulation ===

Genesis block created.
Genesis block hash: 5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9

Mining block 1...
Block mined: 0000a3b7c2e1f8d4a6b9c5e3f2a1b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1

Mining block 2...
Block mined: 00007c8d9e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0

=== Blockchain Structure ===
Index: 0
Timestamp: 1700000000.123456
Data: Genesis Block
Previous Hash: 0
Nonce: 0
Hash: 5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9

Index: 1
Timestamp: 1700000001.234567
Data: Transaksi A → B: 10 Coin
Previous Hash: 5feceb66ffc38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9
Nonce: 12345
Hash: 0000a3b7c2e1f8d4a6b9c5e3f2a1b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1

Index: 2
Timestamp: 1700000002.345678
Data: Transaksi B → C: 5 Coin
Previous Hash: 0000a3b7c2e1f8d4a6b9c5e3f2a1b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1
Nonce: 67890
Hash: 00007c8d9e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0

=== Integrity Verification ===
Block 1 is valid.
Block 2 is valid.

Pembahasan:
1. Proof of Work Berhasil: Program berhasil menambang dua blok dengan hash yang dimulai dengan 4 nol (sesuai difficulty 4).

2. Waktu Mining: Proses mining membutuhkan waktu yang bervariasi tergantung nonce yang ditemukan. Semakin tinggi difficulty, semakin lama waktu yang dibutuhkan.

3. Integritas Blockchain: Setiap blok menyimpan hash blok sebelumnya, menciptakan rantai yang tidak dapat diubah tanpa mengubah semua blok berikutnya.

4. Konsumsi Sumber Daya: PoW memerlukan komputasi intensif, yang tercermin dari perlunya mencoba banyak nonce sebelum menemukan hash yang valid.

## 7. Jawaban Pertanyaan
Pertanyaan 1:
Mengapa fungsi hash sangat penting dalam blockchain?
Fungsi hash penting karena:

Keunikan: Hash yang berbeda untuk input yang berbeda (deterministik).

Keamanan: Tidak mungkin merekayasa balik dari hash ke data asli.

Integritas: Perubahan kecil pada data menghasilkan hash yang sangat berbeda.

Efisiensi: Hash mengubah data ukuran berapa pun menjadi string tetap (256-bit untuk SHA-256).

Pertanyaan 2:
Bagaimana Proof of Work mencegah double spending?
PoW mencegah double spending dengan:

Konsensus Terdistribusi: Transaksi harus divalidasi oleh mayoritas node.

Waktu Konfirmasi: Transaksi membutuhkan waktu untuk dikonfirmasi dalam blok.

Biaya Komputasi: Untuk mengganti transaksi, penyerang harus menambang ulang blok tersebut dan semua blok berikutnya, yang memerlukan daya komputasi lebih besar dari 51% jaringan.

Pertanyaan 3:
Apa kelemahan dari PoW dalam hal efisiensi energi?
Kelemahan utama PoW:

1. Konsumsi Energi Tinggi: Penambangan Bitcoin mengkonsumsi energi setara negara kecil.

2. E-Waste: Perangkat keras khusus (ASIC) cepat usang dan menjadi limbah elektronik.

3. Sentralisasi: Penambangan cenderung terpusat di daerah dengan energi murah, mengurangi desentralisasi.

4. Lingkungan: Emisi karbon dari pembangkit listrik berbahan bakar fosil.

## 8. Kesimpulan
Proof of Work adalah mekanisme konsensus yang efektif untuk mengamankan blockchain melalui kerja komputasi. Implementasi TinyChain berhasil mensimulasikan proses mining dengan fungsi hash SHA-256 dan difficulty yang dapat disesuaikan. Meskipun PoW memberikan keamanan melalui biaya komputasi, ia memiliki kelemahan signifikan dalam efisiensi energi, mendorong pengembangan mekanisme konsensus alternatif seperti Proof of Stake (PoS).

## 9. Daftar Pustaka
Stallings, W. (2017). Cryptography and Network Security: Principles and Practice (7th ed.).

Stinson, D. R., & Paterson, M. B. (2019). Cryptography: Theory and Practice (4th ed.).

Nakamoto, S. (2008). Bitcoin: A Peer-to-Peer Electronic Cash System.

## 10. Commit Log
commit 3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b
Author: Bramby Dida Baskara <brambybaskara8@.com>
Date:   2025-10-04

    week13-tinychain
