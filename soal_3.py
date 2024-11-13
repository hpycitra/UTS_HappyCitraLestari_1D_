jumlah_barang = int(input("Masukkan jumlah Barang :"))
total_harga = 0

for a in range ( jumlah_barang ):
    harga = float(input(f"Masukkan Harga Barang Ke-{a+1}:"))
    total_harga += harga
if jumlah_barang >0 :
    total_harga

print(f"Total Belanjaan Rp. {total_harga : 2f}")
