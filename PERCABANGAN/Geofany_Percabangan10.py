# Nama : Geofany
# Kelas : XI TKJ 1
# No Absen : 12

# Input total belanjaan pelanggan
total_belanjaan = float(input("Masukkan total belanjaan pelanggan: "))

# Inisialisasi variabel diskon
diskon = 0

# Mengecek kondisi diskon
if total_belanjaan > 500000:
    diskon = 0.1  # Diskon 10%
elif total_belanjaan >= 300000:
    diskon = 0.05  # Diskon 5%

# Menghitung jumlah diskon
jumlah_diskon = total_belanjaan * diskon

# Menghitung total yang harus dibayarkan pelanggan setelah diskon
total_setelah_diskon = total_belanjaan - jumlah_diskon

# Menampilkan hasil
print(f"Total belanjaan: Rp{total_belanjaan:,.2f}")
print(f"Diskon: Rp{jumlah_diskon:,.2f}")
print(f"Total yang harus dibayarkan: Rp{total_setelah_diskon:,.2f}")
