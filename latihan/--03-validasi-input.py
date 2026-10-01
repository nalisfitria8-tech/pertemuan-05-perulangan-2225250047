# Program: 03_validasi_input.py
# Deskripsi: Melakukan validasi input menggunakan perulangan while agar user mengulang jika input salah.

angka = -1

while angka < 0 or angka > 100:
    angka = int(input("Masukkan angka antara 0 sampai 100: "))
    if angka < 0 or angka > 100:
        print("Masukan salah! Angka harus berada di antara 0 dan 100. Silakan coba lagi.")

print(f"Terima kasih! Anda memasukkan angka yang valid: {angka}")