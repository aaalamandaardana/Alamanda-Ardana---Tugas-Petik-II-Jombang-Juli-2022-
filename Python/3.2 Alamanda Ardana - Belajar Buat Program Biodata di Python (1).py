#Beri ucapan selamat datang
print("Selamat Datang di Website Arda")

#Membuat variabel nama_saya yang menerima inputan
nama_lengkap = input("Masukkan Nama Lengkap : ")

#Membuat variabel asal_daerah yang menerima inputan
asal_daerah = input("Masukkan Asal Daerah : ")

#Membuat array biodata yang mengumpulkan hasil inputan
biodata = [nama_lengkap, asal_daerah]

#Melakukan Perulangan For
for isi_biodata in biodata:
    print(isi_biodata)

