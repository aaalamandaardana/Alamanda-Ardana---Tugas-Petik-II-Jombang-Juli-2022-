#............................................#
#. Alamanda Ardana - Kodingan Bank Alamanda .#
#............................................#
#Masih Belum Sempurna karena Masih Terbatasnya Pengetahuan si Alamanda Ardana

kumpulan_norek = []

#Fungsi Membersihkan Terminal (supaya terlihat rapih)
def bersihkan_terminal() :
    import os
    os.system('cls' if os.name == 'nt' else 'clear') #Kalo Windows, pakai 'cls / #Kalo linux, MacOS, dll, pakai 'clear'

#Membuat Fungsi Awalan Program
def awalan() :
    bersihkan_terminal()
    #Membuat Judul Program
    print("*****************************************")
    print("*****SELAMAT DATANG DI BANK ALAMANDA*****")
    print("*****************************************")
    print()

    #Membuat Menu
    print("MENU :")
    print("[1]  Buka Rekening")
    print("[2]  Setoran Tunai")
    print("[3]  Tarik Tunai")
    print("[4]  Transfer")
    print("[5]  Lihat Daftar Transfer")
    print("[6]  Keluar")
    print("--------------------------------------------")
    
    #Membuat Inputan User terkait Pemilihan Menu
    masukKodeMenu = input("Silakan Masukkan Kode Menu = ")
    
    if(masukKodeMenu == "1"):
        print("--------------------------------------------")
        print()
        buka_rekening()
    elif(masukKodeMenu == "2"):
        print("--------------------------------------------")
        print()
        setoran_tunai()
    elif(masukKodeMenu == "3"):
        print("--------------------------------------------")
        print()
        tarik_tunai()
    elif(masukKodeMenu == "4"):
        print("--------------------------------------------")
        print()
        transfer()
    elif(masukKodeMenu == "5"):
        print("--------------------------------------------")
        print()
        lihat_DaftarTransfer()
    elif(masukKodeMenu == "6"):
        print()
        keluar()
    else:
        print("Anda memilih menu yang salah!")
        print()
        awalan_lagi()

#Membuat Fungsi untuk Kembali ke Awalan Program
def awalan_lagi() :
    print("\n")
    input("Tekan Enter untuk kembali ke Menu Awalan...")
    awalan()

#Membuat Fungsi dari Menu[1] : Buka Rekening
def buka_rekening() :
    while True :
        #Pembuatan Nomor Rekening User
        import random, string
        norek = "REK" + ''.join(random.choice(string.digits) for _ in range(3))

        #Hasil
        print()
        print("***********    BUKA REKENING    *************")
        print("---------------------------------------------")
        print("Peraturan :")
        print("1. Nama harus berupa huruf")
        print("2. Jumlah setoran awal harus berupa angka")
        print("---------------------------------------------")
        nama_user    = input("Masukkan Nama Anda            : ")
        setoran_awal = input("Masukkan Jumlah Setoran Awal  : ")

        #nama_user harus huruf dan setoran_awal harus angka
        nama_huruf    = nama_user.isalpha()
        setWal_angka  = setoran_awal.isdigit()

        if nama_huruf == True and setWal_angka == True :
            print("------------------------------------------------------------------------------------------------")
            print("Pembukaan rekening dengan nomor", norek, "atas nama", nama_user.upper(), "berhasil.")
            print("(Nomor rekening beserta saldo dan nama pemiliknya sudah terdata di file \'nasabah.txt\')")
            
            #Memasukkan Norek ke Kumpulan Norek
            kumpulan_norek.append(norek)

            #Mencatat Rekening yang Tadi Berhasil Dibuka ke dalam file 'nasabah.txt'. 
            teks = "\n {} \t\t\t\t {} \t\t\t\t {} ".format(norek, nama_user.upper(), setoran_awal)
            #Buka File untuk Ditulis. Pakai Mode "a" supaya File Bisa Ditulis Banyak Inputan
            nasabah = open("nasabah.txt", "a")
            #Tulis teks ke file
            nasabah.write(teks)
            #Tutup File
            nasabah.close()

            print()
            awalan_lagi()
        elif nama_huruf == False and setWal_angka == True :
            print("------------------------------------------------------------------------------------------------")
            print("Nama tidak valid. Coba masukkan lagi.")
            print()
        elif nama_huruf == True and setWal_angka == False :
            print("------------------------------------------------------------------------------------------------")
            print("Jumlah setoran awal tidak valid. Coba masukkan lagi.")
            print()
        else :
            print("------------------------------------------------------------------------------------------------")
            print("Nama dan jumlah setoran awal tidak valid. Coba masukkan lagi.")
            print()

#Membuat Fungsi dari Menu[2] : Setoran Tunai. #Kekurangan = Belum bisa mengubah jumlah saldo di 'nasabah.txt'
def setoran_tunai() :
    while True :
        #Tampilan Halaman Inputan Setoran Tunai
        print()
        print("***********    SETORAN TUNAI    *************")
        print("---------------------------------------------")
        print("Peraturan :")
        print("1. Nomor rekening harus sudah terdata di file \'nasabah.txt\'")
        print("2. Nominal setoran harus berupa angka")
        print("---------------------------------------------")
        nomor_rekening  = input("Masukkan Nomor Rekening                : ")
        setoran         = input("Masukkan Nominal yang Akan Disetor     : ")

        #Memasukkan Peraturan Setoran Tunai ke Dalam Kodingan
        data_norek      = nomor_rekening in kumpulan_norek
        bentuk_setoran  = setoran.isdigit()

        if data_norek == True  and bentuk_setoran == True :
            print("------------------------------------------------------------------------------------------------")
            print("Setoran tunai sebesar", setoran, "ke rekening", nomor_rekening, "berhasil.")
            print()
            awalan_lagi()
        elif data_norek == False  and bentuk_setoran == True :
            print("------------------------------------------------------------------------------------------------")
            print("Nomor rekening belum terdata di file \'nasabah.txt\'. Setoran tunai gagal.")
            print()
        elif data_norek == True and bentuk_setoran == False :
            print("------------------------------------------------------------------------------------------------")
            print("Nominal setoran tidak valid. Setoran tunai gagal.")
            print()
        else :
            print("------------------------------------------------------------------------------------------------")
            print("Nomor rekening belum terdata di file \'nasabah.txt\' dan nominal setoran tidak valid.") 
            print("Setoran tunai gagal.")
            print()

#Membuat Fungsi dari Menu[3] : Tarik Tunai.  #Kekurangan = Belum bisa mengubah jumlah saldo di 'nasabah.txt'
def tarik_tunai() :
    while True :
        #Tampilan Halaman Inputan Setoran Tunai
        print()
        print("***********     TARIK TUNAI     *************")
        print("---------------------------------------------")
        print("Peraturan :")
        print("1. Nomor rekening harus sudah terdata di file \'nasabah.txt\'")
        print("2. Nominal penarikan harus berupa angka")
        print("3. Nominal penarikan harus lebih kecil dari atau sama dengan saldo rekening")
        print("---------------------------------------------")
        nomor_rekening  = input("Masukkan Nomor Rekening                : ")
        tarikan         = input("Masukkan Nominal yang Akan Ditarik     : ")

        #Memasukkan Peraturan Tarik Tunai ke Dalam Kodingan
        data_norek      = nomor_rekening in kumpulan_norek
        bentuk_tarikan  = tarikan.isdigit()

        if data_norek == True  and bentuk_tarikan == True :
            print("------------------------------------------------------------------------------------------------")
            print("Tarik tunai sebesar", tarikan, "ke rekening", nomor_rekening, "berhasil.")
            print()
            awalan_lagi()
        elif data_norek == False  and bentuk_tarikan == True :
            print("------------------------------------------------------------------------------------------------")
            print("Nomor rekening belum terdata di file \'nasabah.txt\'. Tarik tunai gagal.")
            print()
        elif data_norek == True and bentuk_tarikan == False :
            print("------------------------------------------------------------------------------------------------")
            print("Nominal setoran tidak valid. Tarik tunai gagal.")
            print()
        else :
            print("------------------------------------------------------------------------------------------------")
            print("Nomor rekening belum terdata di file \'nasabah.txt\' dan nominal setoran tidak valid.") 
            print("Tarik tunai gagal.")
            print()

#Membuat Fungsi dari Menu[4] : Transfer. #Kekurangan = Belum bisa mengubah jumlah saldo di 'nasabah.txt'
def transfer() :
    while True :
        #Pembuatan Waktu Transfer
        import datetime
        waktu_transfer = datetime.datetime.now()
        
        #Pembuatan Kode Transfer
        import random, string
        kode_transfer = "TRA" + ''.join(random.choice(string.digits) for _ in range(3))

        #Tampilan Halaman Utama Menu Transfer
        print()
        print("***********       TRANSFER      *************")
        print("---------------------------------------------")
        print("Peraturan :")
        print("1. Nomor rekening harus sudah terdata di file \'nasabah.txt\'")
        print("2. Nominal transfer harus berupa angka")
        print("---------------------------------------------")
        rekening_sumber    = input("Masukkan Nomor Rekening Sumber         : ")
        rekening_tujuan    = input("Masukkan Nomor Rekening Tujuan         : ")
        nominal_transfer   = input("Masukkan Nominal yang Akan Ditransfer  : ")

        #Memasukkan Peraturan Setoran Tunai ke Dalam Kodingan
        norekSumber     = rekening_sumber in kumpulan_norek
        norekTujuan     = rekening_tujuan in kumpulan_norek
        transfer_angka  = nominal_transfer.isdigit()
        
        if norekSumber == True  and norekTujuan == True  and transfer_angka == True :
            print("------------------------------------------------------------------------------------------------")
            print("Transfer sebesar", nominal_transfer, "dari rekening", norekSumber, "ke rekening", norekTujuan, "berhasil.")
            print("(Data transfer ini sudah tersimpan di file \'transfer.txt\')")
            
            #Mencatat Data Transfer yang Tadi Berhasil ke dalam file 'transfer.txt'
            teks = "\n {} \t\t\t\t {} \t\t\t\t {} \t\t\t\t {} \t\t\t\t {}".format(waktu_transfer, kode_transfer, rekening_sumber, rekening_tujuan, nominal_transfer)
            #Buka File untuk Ditulis. Pakai Mode "a" supaya File Bisa Ditulis Banyak Inputan
            data_transfer = open("transfer.txt", "a")
            #Tulis teks ke file
            data_transfer.write(teks)
            #Tutup File
            data_transfer.close()

            print()
            awalan_lagi()
        elif norekSumber == False  and norekTujuan == True  and transfer_angka == True :
            print("------------------------------------------------------------------------------------------------")
            print("Nomor rekening sumber belum terdata di file \'nasabah.txt\'. Transfer gagal.")
            print()
        elif norekSumber == True  and norekTujuan == False  and transfer_angka == True :
            print("------------------------------------------------------------------------------------------------")
            print("Nomor rekening tujuan belum terdata di file \'nasabah.txt\'. Transfer gagal.")
            print()
        elif norekSumber == True  and norekTujuan == True  and transfer_angka == False :
            print("------------------------------------------------------------------------------------------------")
            print("Nominal transfer tidak valid. Transfer gagal.")
            print()
        elif norekSumber == False and norekTujuan == False  and transfer_angka == True :
            print("------------------------------------------------------------------------------------------------")
            print("Nomor rekening sumber dan tujuan belum terdata di file \'nasabah.txt\'. Transfer gagal.")
            print()
        elif norekSumber == False and norekTujuan == True  and transfer_angka == False :
            print("------------------------------------------------------------------------------------------------")
            print("Nomor rekening sumber belum terdata di file \'nasabah.txt\', dan nominal transfer tidak valid. Transfer gagal.")
            print()
        elif norekSumber == True and norekTujuan == False and transfer_angka == False :
            print("------------------------------------------------------------------------------------------------")
            print("Nomor rekening tujuan belum terdata di file \'nasabah.txt\', dan nominal transfer tidak valid. Transfer gagal.")
            print()
        else :
            print("------------------------------------------------------------------------------------------------")
            print("Nomor rekening sumber dan tujuan belum terdata di file \'nasabah.txt\', serta nominal transfer tidak valid. Transfer gagal.")
            print()

#Membuat Fungsi dari Menu[5] : Lihat Daftar Transfer
def lihat_DaftarTransfer() :
    #Buka File 'transfer.txt'  untuk Dibaca
    daftar_transfer = open("transfer.txt", "r")
    #Baca Isi File
    print(daftar_transfer.read())
    #Tutup File
    daftar_transfer.close()
    
    print()
    awalan_lagi()

#Membuat Fungsi dari Menu[6] : Keluar dan Program Akan Berakhir
def keluar() :
    #Membuat Ucapan Terima Kasih kepada User. Setelah Itu, Program Selesai
    print("**************************************************************")
    print("*** Terima kasih karena sudah mengunjungi Bank Alamanda :D ***")
    print("**************************************************************")

#Memanggil Fungsi awalan() dan Program Mulai Berjalan
awalan()