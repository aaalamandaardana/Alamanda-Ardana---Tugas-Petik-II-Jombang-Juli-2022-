#Mengganti Spasi dengan Tanda Pagar
print('A', 1, 'XYZ', 2, sep='#')
print ('ini pesan pertama', end=" - ")
print('dan ini pesan kedua')

#-----------------------------------------------------------------

#Membuat Daftar Angka Berurutan
for bilangan_urut in range(10):
    print(bilangan_urut+1)

#-----------------------------------------------------------------

#Membuat Fungsi Array Mobil
mobil = ['Honda Jazz', 'Avanza', 'Kijang', 'Fortuner']

for indeks in mobil:
    print(indeks)

#----------------------------------------------------------------

#Membuat Array Buah
buah = ['mangga', 'jeruk', 'anggur', 'ceri', 'alpukat', 'sirsak', 'apel']
#Indeks selalu dimulai dengan 0 (nol)
#Indeks 0 = mangga
#Indeks 1 = jeruk
#dst

#Mencetak Jeruk
print(buah[1])

#Melakukan Perulangan For (1)
for buah_buahan in buah:
    print(buah_buahan)

#Melakukan Perulangan For (2)
for buah_buahan in buah:
    print('Nama Buah : ', buah_buahan)
