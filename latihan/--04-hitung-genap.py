# Program: 04_hitung_genap.py
# Deskripsi: Menghitung jumlah bilangan genap dalam rentang tertentu.

awal = int(input("Masukkan batas awal: "))
akhir = int(input("Masukkan batas akhir: "))
jumlah_genap = 0

for i in range(awal, akhir + 1):
    if i % 2 == 0:
        jumlah_genap += 1

print(f"Banyaknya bilangan genap dari {awal} sampai {akhir} adalah: {jumlah_genap}")