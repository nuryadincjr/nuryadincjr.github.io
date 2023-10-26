# Fungsi untuk menghitung berapa kali karakter angka muncul dalam string
def hitung_karakter_angka(string):
    # Membagi string menjadi daftar angka dengan menggunakan koma atau spasi sebagai pemisah
    angka = re.split(r'[,\s]+', string)
    jumlah_angka = {}
    
    for karakter in angka:
        karakter = karakter.strip()
        if karakter.isnumeric():
            if karakter in jumlah_angka:
                jumlah_angka[karakter] += 1
            else:
                jumlah_angka[karakter] = 1
    
    return jumlah_angka

# Fungsi untuk menghitung berapa kali setiap karakter muncul dalam string
def hitung_karakter(string):
    jumlah_karakter = {}
    
    for karakter in string:
        if karakter in jumlah_karakter:
            jumlah_karakter[karakter] += 1
        else:
            jumlah_karakter[karakter] = 1
    
    return jumlah_karakter

# Fungsi untuk mencari data dalam string yang dipisahkan oleh koma atau spasi
def cari_data(string, target):
    # Membagi string menjadi daftar data dengan menggunakan koma atau spasi sebagai pemisah
    data = re.split(r'[,\s]+', string)
    jumlah_data = data.count(target)  # Menghitung berapa kali data ditemukan
    hasil_pencarian = [item for item in data if item == target]
    
    if jumlah_data > 0:
        print(f"Data '{target}' ditemukan sebanyak {jumlah_data} kali.")
    
    return hasil_pencarian
    
# Fungsi untuk menampilkan menu pilihan operasi
def tampilkan_menu():
    print("Pilihan Operasi:")
    print("1. Hitung karakter angka dalam string yang")
    print("2. Hitung karakter dalam string")
    print("3. Urutkan angka dalam string")
    print("4. Cari angka dalam string")
    print("0. Keluar")

# Fungsi untuk mengurutkan angka dalam string
def urutkan_angka(string):
    # Membagi string menjadi daftar angka dengan menggunakan koma atau spasi sebagai pemisah
    angka = re.split(r'[,\s]+', string)
    angka_terurut = sorted(angka, key=lambda x: int(x))
    return ', '.join(angka_terurut)

import re

# Loop utama program
while True:
    tampilkan_menu()
    pilihan = input("Pilih operasi (1/2/3/4/0): ")

    if pilihan == "0":
        break
    elif pilihan == "1":
        data = input("Masukkan string dengan angka: ")
        hasil = hitung_karakter_angka(data)
    elif pilihan == "2":
        data = input("Masukkan string: ")
        hasil = hitung_karakter(data)
    elif pilihan == "3":
        data = input("Masukkan string dengan angka yang dipisahkan oleh koma atau spasi: ")
        hasil = urutkan_angka(data)
    elif pilihan == "4":
        data = input("Masukkan string dengan data yang dipisahkan oleh koma atau spasi: ")
        target = input("Masukkan data yang ingin Anda cari: ")
        hasil = cari_data(data, target)
    else:
        print("Pilihan tidak valid.")
        continue