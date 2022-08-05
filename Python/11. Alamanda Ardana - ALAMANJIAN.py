#Alamanda Ardana - Program Aplikasi Sistem Informasi Kajian Islam Kota Depok

import csv
import os

namafile = 'kajiandepok.csv'

#Membuat fungsi yang dapat membersihkan terminal (supaya rapih)
def bersihkan_terminal(): 
    #Jika OS = Windows --> muncul 'cls' ,, selain itu --> muncul 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

#Membuat Fungsi yang Menampilkan Menu 
def tampilkan_menu():
    bersihkan_terminal()
    print("..........................................................")
    print(".                       ALAMANJIAN                       .")
    print(". (Sistem Informasi Kajian Islam Masjid Balaikota Depok) .")
    print("..........................................................")
    print()
    print("MENU :")
    print("[1] Lihat Daftar Informasi Kajian")
    print("[2] Buat Informasi Kajian Baru")
    print("[3] Edit Informasi Kajian")
    print("[4] Hapus Informasi Kajian")
    print("[5] Cari Informasi Kajian")
    print("[0] Keluar")
    print("------------------------")
    memilih_menu = input("Pilih menu> ")
    
    if(memilih_menu == "1"):
        tampilkanListKajian()
    elif(memilih_menu == "2"):
        buat_InfoKajian()
    elif(memilih_menu == "3"):
        edit_InfoKajian()
    elif(memilih_menu == "4"):
        hapus_InfoKajian()
    elif(memilih_menu == "5"):
        cari_InfoKajian()
    elif(memilih_menu == "0"):
        keluar()
    else:
        print("Kamu memilih menu yang salah!")
        kembali_ke_menu()

#Membuat Fungsi kembali_ke_menu()
def kembali_ke_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    tampilkan_menu()

#Membuat Fungsi dari Menu [1] Lihat Daftar Informasi Kajian
def tampilkanListKajian():
    bersihkan_terminal()
    info_kajian = []

    with open(namafile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            info_kajian.append(row)

    #Jika ada data kajiannya, maka akan dicetak tuh datanya
    if (len(info_kajian) > 0):
        header = info_kajian.pop(0)
        print(header[0], '\t', header[1], '\t', '\t', header[2])
        print("-"*34)
        for data in info_kajian:
            print(data[0], '\t', data[1], '\t', '\t', data[2])
    #Kalo gaada data kajiannya, maka program mengucapkan permintaan maaf
    else:
        print("Maaf, belum ada data kajiannya")

    kembali_ke_menu()

#Membuat Fungsi dari Menu [2] Buat Informasi Kajian Baru
def buat_InfoKajian():
    bersihkan_terminal()
    with open(namafile, mode='a') as csv_file:
        fieldnames = ['NO', 'JUDUL', 'TANGGAL']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        no          = input("Nomor Urut Kajian  : ")
        judul       = input("Judul Kajian       : ")
        tanggal     = input("Tanggal Kajian     : ")

        #Menulis inputan di 'kajiandepok.csv'
        writer.writerow({'NO' : no, 'JUDUL': judul, 'TANGGAL': tanggal})
        #Membuat tanda di terminal bahwa data kajian sudah ditulis di 'kajiandepok.csv'
        print("Data kajian berhasil disimpan!")

    kembali_ke_menu()

#Membuat Fungsi dari Menu [3] Edit Informasi Kajian
def edit_InfoKajian():
    bersihkan_terminal()
    info_kajian = []

    with open(namafile, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            #Memasukkan data ke list
            info_kajian.append(row)

    print("NO \t JUDUL \t \t TANGGAL")
    print("-" * 32)

    for data in info_kajian:
        print(f"{data['NO']} \t {data['JUDUL']} \t {data['TANGGAL']}")

    print("-----------------------")
    no          = input("Pilih Nomor Urut> ")
    judul       = input("Judul Kajian Terbaru                                : ")
    tanggal     = input("Tanggal Kajian Terbaru (Format = Hari/Bulan/Tahun)  : ")

    # Mencari info kajian dan mengubah datanya dengan data yang baru
    indeks = 0
    for data in info_kajian:
        if (data['NO'] == no):
            info_kajian[indeks]['JUDUL'] = judul
            info_kajian[indeks]['TANGGAL'] = tanggal
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(namafile, mode='w') as csv_file:
        fieldnames = ['NO', 'JUDUL','TANGGAL']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in info_kajian:
            writer.writerow({'NO': new_data['NO'], 'JUDUL': new_data['JUDUL'], 'TANGGAL': new_data['TANGGAL']})

    kembali_ke_menu()

#Membuat Fungsi dari Menu [4] Hapus Informasi Kajian
def hapus_InfoKajian():
    bersihkan_terminal()

    info_kajian = []

    with open(namafile, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            info_kajian.append(row)

    print("NO \t JUDUL \t TANGGAL")
    print("-" * 32)

    for data in info_kajian:
        print(f"{data['NO']} \t {data['JUDUL']} \t {data['TANGGAL']}")

    print("-----------------------")
    no = input("Masukkan nomor urut dari kajian yang ingin dihapus> ")

    # Mencari info kajian dan mengubah datanya dengan data yang baru
    indeks = 0
    for data in info_kajian:
        if (data['NO'] == no):
            info_kajian.remove(info_kajian[indeks])
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(namafile, mode="w") as csv_file:
        fieldnames = ['NO', 'JUDUL', 'TANGGAL']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in info_kajian :
           writer.writerow({'NO': new_data['NO'], 'JUDUL': new_data['JUDUL'], 'TANGGAL': new_data['TANGGAL']}) 

    print("Info kajian sudah terhapus")
    kembali_ke_menu()

#Membuat Fungsi dari Menu [5] Cari Informasi Kajian
def cari_InfoKajian():
    bersihkan_terminal()
    info_kajian = []

    with open(namafile, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            info_kajian.append(row)

    no = input("Cari Berdasarkan Nomor Urut > ")

    data_found = []

    # Mencari Info Kajian
    indeks = 0
    for data in info_kajian:
        if (data['NO'] == no):
            data_found = info_kajian[indeks]
            
        indeks = indeks + 1

    if len(data_found) > 0:
        print("DATA DITEMUKAN: ")
        print(f"Judul Kajian    : {data_found['JUDUL']}")
        print(f"Tanggal Kajian  : {data_found['TANGGAL']}")
    else:
        print("Tidak ada data yang ditemukan")
    kembali_ke_menu()
    
#Membuat fungsi dari Menu [0]Keluar
def keluar():
    #Membuat ucapan terima kasih kepada user
    print("**************************************************************")
    print("*** Terima kasih karena sudah mengunjungi ALAMANJIAN :D ***")
    print("**************************************************************")
    print()

#Memanggil fungsi tampilkan_menu() dan program mulai berjalan
tampilkan_menu()

#-----------------------
#Referensi Kodingan : https://www.petanikode.com/python-csv-crud/ 