# Program: 01_tabel_perkalian.py
# Deskripsi: Menampilkan tabel perkalian menggunakan perulangan for.

n = int(input("Masukkan angka untuk tabel perkalian: "))

print(f"\nTabel Perkalian {n}:")
for i in range(1, 11):
    hasil = n * i
    print(f"{n} x {i} = {hasil}")