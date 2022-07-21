#Arda, Fatcur, Syahdan - Tugas Kelompok Membuat Aplikasi Input Data Kajian

#Pakai While supaya Program Dapat Berulang-Ulang Terus
while (True) :
    #Judul Program
    print("................................................................................")
    print(".            PENDATAAN KAJIAN ISLAM DI DESA PLOSOGENENG (JOMBANG)              .")
    print(". *Untuk keperluan publikasi di situs web Sistem Informasi Kajian Plosogeneng  .")
    print("................................................................................")

    #Penginputan Data User oleh User, tuk Keperluan Verifikasi dan Mencegah Penipuan Data Kajian
    print()
    nama_user             = input("Nama Kamu          : ")
    nomorHP_user          = input("Nomor HP Kamu      : ")
    
    #Penginputan Data Kajian oleh User
    print()
    print("Silakan masukkan data-data kajian yang mau kamu kirim :)")
    print()
    tema_kajian             = input("Tema Kajian                        : ")
    pengisi_kajian          = input("Pengisi Kajian                     : ")
    tempat_kajian           = input("Tempat Kajian                      : ")
    tanggal_kajian          = input("Tanggal Kajian                     : ")
    waktu_kajian            = input("Waktu Kajian (Pukul Berapa)        : ")
    penyelenggara_kajian    = input("Penyelenggara Kajian               : ")
    contact_person          = input("Nomor HP Penyelenggara Kajian      : ")

   #Pencetakan Hasil Inputan Data Kajian 
    print()
    print()
    print(".........................................................................")
    print(".                             DATA KAJIAN                               .")
    print(".........................................................................")
    print(". Tema Kajian                    : ", tema_kajian)
    print(". Pengisi Kajian                 : ", pengisi_kajian)
    print(". Tempat Kajian                  : ", tempat_kajian)
    print(". Tanggal Kajian                 : ", tanggal_kajian)
    print(". Waktu Kajian                   : ", waktu_kajian)
    print(". Penyelenggara Kajian           : ", penyelenggara_kajian)
    print(". Nomor HP Penyelenggara Kajian  : ", contact_person)
    print(".........................................................................")
    print(". Oke, data kajian yang kamu kirim insyaa Allah akan kami publikasikan  .")
    print(". dalam situs web Sistem Informasi Kajian Plosogeneng                   .")
    print()
    print(". Struk inputan data kajian ini tersimpan dalam file strukKajian.txt    .")
    print(".........................................................................")
    print()
    print()

    #Memasukkan Fungsi Waktu Penginputan Data Kajian oleh User
    import datetime
    waktu_input = datetime.datetime.now()

    #Variabel strukKajian berfungsi untuk memasukkan data ke dalam strukKajian.txt untuk membuat struk/bukti penginputan data kajian
    strukKajian = open("strukKajian.txt", "w")
    print()
    print()
    print(".........................................................................", file=strukKajian)
    print(".                            BUKTI PENGINPUTAN                          .", file=strukKajian)
    print(".                               DATA KAJIAN                             .", file=strukKajian)
    print(".........................................................................", file=strukKajian)
    print(". Tema Kajian                    : ", tema_kajian, file=strukKajian)
    print(". Pengisi Kajian                 : ", pengisi_kajian, file=strukKajian)
    print(". Tempat Kajian                  : ", tempat_kajian, file=strukKajian)
    print(". Tanggal Kajian                 : ", tanggal_kajian, file=strukKajian)
    print(". Waktu Kajian                   : ", waktu_kajian, file=strukKajian)
    print(". Penyelenggara Kajian           : ", penyelenggara_kajian, file=strukKajian)
    print(". Nomor HP Penyelenggara Kajian  : ", contact_person, file=strukKajian)
    print(".........................................................................", file=strukKajian)
    print("Data kajian ini diinput oleh", nama_user, "(Nomor HP : ", nomorHP_user, ")", file=strukKajian)
    print("pada", waktu_input, file=strukKajian)
    print(".........................................................................", file=strukKajian)
    print()
    strukKajian.close()

    #Pertanyaan untuk User Apakah Mau Input Data Kajian yang Lain
    print("[1] Input Data Kajian Lain")
    print("[2] Keluar")
    print()
    status = input("Pilih [1] atau [2]? ")
    if status == "2" :
        print("...................................................................")
        print(".                Terima kasih atas kontribusi kamu                .") 
        print(".   Semoga Allah mencatat kontribusi kamu ini sebagai kebaikan    .")
        print("...................................................................")
        print()
        break
    elif status == "1" :
        print("Silakan input data lagi \n")
    else :
        print("Inputan tidak dikenali \n")
        print()
        print("...................................................................")
        print(".                Terima kasih atas kontribusi kamu                .") 
        print(".   Semoga Allah mencatat kontribusi kamu ini sebagai kebaikan    .")
        print("...................................................................")
        print()
        break
