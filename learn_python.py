print('hallo python senang mengenal anda')

# Variabel
nama = 'jabez chrisopras ferdinand'
umur = 18
tinggi = 170.5
mahasiswa = True


while True :
    angka_pertama = int(input('masukan angka pertama :'))

    while True :
        operator = input('masukan operator (+, -, *, /) atau = untuk keluar: ')
        if operator == '=':
            print('hasilnya adalalah : ', angka_pertama)
            print('terimakasih telah menggunakan program ini')
            break

        while True :
            angka_kedua = int(input('masukan angka kedua :'))

            if operator == '+':
                angka_pertama += angka_kedua
            elif operator == '-' :
                angka_pertama -= angka_kedua
            elif operator == '*' :
                angka_pertama *= angka_kedua
            elif operator == '/' :
                if angka_kedua != 0 :
                    angka_pertama /= angka_kedua
                else:
                    print('tidak bisa membagi dengan nol')
                    break
            elif operator == '%' :
                angka_pertama %= angka_kedua 
            elif operator == '**' :
                angka_pertama **= angka_kedua

            else:
                print('operator tidak valid')

    lanjutan = input('apakah anda ingin melanjutkan perhitungan (y/n) :')

    if lanjutan.lower() != 'y':
        print('terimakasih telah menggunakan program ini')
        break


data = 1 + 2j
nama = 'jabez chrisopras ferdinand'
print(type(data))
print('nama saya adalah : %s' % nama)


def menu() :
    print("selamat datang di bioskop".capitalize())
    print("")
