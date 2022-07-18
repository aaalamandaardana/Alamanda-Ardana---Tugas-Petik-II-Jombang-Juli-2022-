#Pakai While supaya Program Dapat Berulang-Ulang Terus
while (True) :
    #Judul Program
    print("-------------------------------------------------")
    print("PENDATAAN KAJIAN ISLAM DI DESA PLOSOGENENG (JOMBANG)")
    print("*Untuk keperluan publikasi di situs web Sistem Informasi Kajian Plosogeneng")
    print("-------------------------------------------------")

    #Penginputan Data Kajian oleh Penyelenggara Kajian
    tema_kajian = input("Tema Kajian            : ")
    pengisi_kajian = input("Pengisi Kajian      : ")
    tempat_kajian = input("Tempat Kajian        : ")
    tanggal_kajian = input("Tanggal Kajian      : ")
    waktu_kajian = input("Waktu Kajian (Pukul Berapa)       : ")
    penyelenggara_kajian = input("Penyelenggara Kajian      : ")

   #Pencetakan Hasil Inputan Data Kajian 
    print()
    print("-------------------------------------------------")
    print("Tema Kajian          : ", tema_kajian)
    print("Pengisi Kajian       : ", pengisi_kajian)
    print("Tempat Kajian        : ", tempat_kajian)
    print("Tanggal Kajian       : ", tanggal_kajian)
    print("Waktu Kajian         : ", waktu_kajian)
    print("Penyelenggara Kajian : ", penyelenggara_kajian)
    print("-------------------------------------------------")
    print()
    print("Oke, data kajian yang kamu kirim insyaa Allah akan kami publikasikan dalam situs web Sistem Informasi Kajian Plosogeneng")
    print ()

    #Pertanyaan untuk Penyelenggara Kajian Apakah Mau Input Data Kajian yang Lain
    status = input("Apakah masih ada data kajian lain yang ingin diinput? (y = ya, t = tidak) ")
    if status == "t" :
        print("Program berhenti \n")
        break
    elif status == "y" :
        print("Silakan input data lagi \n")
    else :
        print("Inputan tidak dikenali \n")
        break
