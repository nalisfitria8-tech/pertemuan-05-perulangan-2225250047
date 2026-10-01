# Program: 02_jumlah_bilangan.py
# Deskripsi: Menghitung jumlah total dari deret angka menggunakan for.

n = int(input("Masukkan batas angka (n): "))
total = 0

for i in range(1, n + 1):
    total += i

print(f"Jumlah total dari 1 sampai {n} adalah: {total}")