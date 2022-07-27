#Alamanda Ardana - Program Pendaftaran Akun A
#(memvalidasi inputan Username, Email, dan Nomor HP)
#----------------------------------------------------------------------------

#UNTUK MEMBERSIHKAN TERMINAL
import os
os.system('cls') #Kalo linux atau MacOS, pakai Clear

#Membuat Judul 
print("..............................")
print(". Program Pendaftaran Akun A .")
print("..............................")

status = ''

def username() :
    print("Peraturan tentang Username :")
    print("1. Minimal berisi 10 karakter")
    print("2. Tidak boleh memakai spasi")
    print("3. Huruf kapital hanya digunakan untuk karakter pertama Username")
    print("--------------------------------------------------------------")

    inputan = input('Username Kamu  : ')
    cek1 = len(inputan)
    cek2 = ' ' in inputan
    cek3 = inputan.capitalize()

    if cek1 >= 10 and cek2 == False and cek3 == inputan :
        status = "Berhasil"
        return inputan, status
    else :
        inputan = "Username Tidak Valid"
        status = "Gagal"
        return inputan, status

def email() :
    print("Peraturan tentang Email :")
    print("1. Minimal berisi 8 karakter")
    print("2. Tidak boleh memakai spasi")
    print("3. Wajib memiliki '@' dan '.'")
    print("--------------------------------------------------------------")
    
    inputan = input('Email Kamu : ')
    cek1 = len(inputan)
    cek2 = ' ' in inputan
    cek3 = '@' and "." in inputan

    if cek1 >= 8 and cek2 == False and cek3 == True :
        status = "Berhasil"
        return inputan, status
    else :
        inputan = "Email Tidak Valid"
        status = "Gagal"
        return inputan, status

def nomorHP() :
    print("Peraturan tentang Nomor HP :")
    print("1. Karakternya adalah angka")
    print("--------------------------------------------------------------")

    inputan = input('Nomor HP Kamu  : ')

    if inputan.isdigit() :
        status = "Berhasil"
        return inputan, status
    else :
        inputan = "Nomor HP Tidak Valid"
        status = "Gagal"
        return inputan, status

def main():
    while True :
    #u1 berisi inputan, u2 berisi status
        u1, u2 = username()
        print("Username Kamu = ", u1)
        print('Status = ', u2)
        print()
        print("--------------------------------------------------------------")
        if u2 == 'Berhasil' :
            break

    while True :
         #e1 berisi inputan, e2 berisi status
        e1, e2 = email()
        print("Email Kamu = ", e1)
        print('Status = ',e2)
        print()
        print("----------------------------------------------------------------")
        if e2 == "Berhasil" :
            break

    while True :
         #n1 berisi inputan, n2 berisi status
        n1, n2 = nomorHP()
        print("Nomor HP Kamu = ", n1)
        print('Status = ',n2)
        print()
        print("----------------------------------------------------------------")
        if n2 == "Berhasil" :
            break

    #Membersihkan Terminal Lagi Supaya Lebih Enak Dilihat
    import os
    os.system('cls')
    
    #Memberikan Paparan tentang Username, Email, dan Nomor HP yang Sudah Valid
    print()
    print("....................................")
    print(". Pendaftaran Akun A Kamu Berhasil .")
    print("....................................")
    print(".")
    print(". Username Kamu    : ", u1)
    print(". Email Kamu       : ", e1)
    print(". Nomor HP Kamu    : ", n1)
    print("....................................")

#Memanggil Fungsi main()
main()

