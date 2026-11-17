# print("selamat datang di latihan logika if else :")

# email = input("masukan email anda : ")

# if email == "jabezchrisopras@gmail.com" :
#     pasword = input("Masukan pasword anda : ")

#     if pasword == '20maret2008' :
#         print("selamat datang bos")
        
#     else:
#         print('pasword anda salah')
# else:
#     print("email anda tidak valid")


# print("Selamat Datang Di Sistem Parkir")
# print("1. Sepeda Motor ")
# print("2. Mobil")
# print("3. Truck/Bus")

# jenis = int(input("Masukan Jenis Kendaraan Anda Menurut Indeks :"))
# durasi = int(input("Masukan Durasi Parkir Anda (JAM) : "))


# if jenis == 1:
#     nm_kendaraan = "sepeda motor"
#     if durasi > 12 :
#         kategori = "mengginap".title()
#         biaya = 50000
#     else:
#         biaya = durasi * 5000
#         kategori = "tidak mengginap".title()

# elif jenis == 2:
#     nm_kendaraan = "mobil".title()
#     if durasi > 12 : 
#         kategori = "mengginap".title()
#         biaya = 75000
#     else:
#         biaya = durasi * 7500
#         kategori = "tidak mengginap".title()

# elif jenis == 3 :
#     nm_kendaraan = "truck".title()
#     if durasi > 12 :
#         kategori = "mengginap".title()
#         biaya = 250000
#     else :
#         biaya = durasi * 25000
#         kategori = "tidak mengginap".title()


# print("Catatan Pembayaran Anda")
# print(f"""
# jenis kendaraan : {nm_kendaraan}
# durasi parkir : {durasi}
# kendaraan anda termasuk kategori : {kategori}
# """.title())

# while True :
#     bayar = int(input(f"masukan biaya parkir : sebesar Rp.{biaya} : ".title()))

#     if bayar > biaya :
#         print(f"uang anda kelebihan silahkan ambil kembalian anda : {bayar - biaya}")
#         break

#     elif bayar < biaya :
#         print("mohon maaf uang anda tidak cukup silahkan masukan sesuai biaya yang tertera")
#     else:
#         break
    
# print("terimakasih sudah menggunakan sistem kami".title())
# print("sampai jumpa lagi".title())


print("selamat datang di siadin mahasiswa".upper())
print('=' * 50)
print('silahkan aktifkan akun siadin anda')
'\n'
print('lengkapi biodata anda')
nama = input('masukan nama lengkap anda : ')
umur = int(input('masukan umur anda : '))
nim = input('masukan nim anda : ')
status = input('masukan status mahasiswa (aktif/tiidak) : ')
dosen = input('masukan nama dosen wali mahasiswa : ')
alamat = input('masukan alamat mahasiswa : ')
nomor = int(input('masukan no hp anda : '))
emailmhs = input('masukan email mahasiswa anda : ')



password_pengguna = '20maret2008'
nama_pengguna = 'jabez chrisopras ferdinand'

if nama == nama_pengguna :
    password = int(input('masukan password anda : '))
    if password == password_pengguna : 
        print('selamat datang di dasbord mahasiswa '.upper())
        print("""
            1. akademik
            2. biodata 
            3. keungan
            4. dokumen
            5. tugas akhir
            6. lainnya""".upper())

        pilihan = int(input("masukan pilihan anda berdasarkan indeks : ".upper()))

        if pilihan == 1 :
            pass
        elif pilihan == 2 :
            pass
        elif pilihan == 3 :
            pass
        elif pilihan == 4 :
            pass
        elif pilihan == 5 :
            pass 
        elif pilihan == 6 :
            pass

def Akademik() :
    print('selamat datang di dasbord akademik'.title())

    print('apa yang anda ingin cek'.title())

    pilihan = int(input('masukan pilihan anda sesuai indeks : '.upper()))

def Biodata() :
    print('selamat datang di dasbord biodata ')

    print(f"""
        Nama : {nama}
        Umur : {umur}
        nim : {nim}
        status : {status}
        dosen pembimbing: {dosen}
        alamat : {alamat}
        nomor : {nomor}
        email mahasiswa : {emailmhs}
""")









