#Membuat Program yang Meminta User untuk Memasukkan Bilangan Ganjil yang Lebih Besar dari 25

#User Akan Menginput Bilangan
a=int(input('Masukkan Bilangan Ganjil yang Lebih Besar dari 25 = '))

#Perulangan For untuk Menanggapi User yang Salah dalam Memasukkan Bilangan
while a%2 !=1 or a<=25:
    a=int(input('Kamu salah. Coba lagi yuk, Masukkan Bilangan Ganjil yang Lebih Besar dari 25 = '))

#Ucapan untuk User yang Benar dalam Memasukkan Bilangan
print('Kamu sudah berhasil memasukkan bilangan ganjil yang lebih besar dari 25. MANTAP!!!')