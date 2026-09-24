import math

jumlah_buku = int(input("Masukkan jumlah buku: "))
tanggal_pinjam = int(input("Masukkan tanggal pinjam: "))
tanggal_jatuh_tempo = int(input("Masukkan tanggal jatuh tempo: "))
tanggal_pengembalian = int(input("Masukkan tanggal pengembalian: "))

lama_peminjaman = tanggal_pengembalian - tanggal_pinjam
biaya_buku = 1000 * lama_peminjaman
if tanggal_pengembalian > tanggal_jatuh_tempo:
    denda = 0.10 * biaya_buku
else: 
    denda = 0
    
total_biaya = (biaya_buku + denda) * jumlah_buku
print("Total biaya yang harus dibayar:", total_biaya)