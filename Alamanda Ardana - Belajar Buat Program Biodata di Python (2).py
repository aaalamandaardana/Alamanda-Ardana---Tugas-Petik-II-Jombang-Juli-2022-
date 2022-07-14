#Membuat array siswa
siswa = []

#Perulangan For
for i in range(3):

    #Mengecek nilai index
    print("ini adalah index ke-",i+1)

    #Menerima inputan nama
    nama_siswa = input("Masukkan Nama Siswa : ")

    #Memasukkan hasil inputan nama ke array siswa
    siswa.append(nama_siswa)
    
#Membuat perulangan untuk mencetak data dari array siswa
for j in siswa:
    print("Nama Siswa = ",j)
