print("selamat datang di latihan logika if else :")

email = input("masukan email anda : ")

if email == "jabezchrisopras@gmail.com" :
    pasword = input("Masukan pasword anda : ")

    if pasword == '20maret2008' :
        print("selamat datang bos")
        
    else:
        print('pasword anda salah')
else:
    print("email anda tidak valid")



print("Selamat Datang Di Sistem Parkir")
print("1. Sepeda Motor ")
print("2. Mobil")
print("3. Truck/Bus")

jenis = int(input("Masukan Jenis Kendaraan Anda Menurut Indeks :"))
durasi = int(input("Masukan Durasi Parkir Anda (JAM) : "))


if jenis == 1:
    nm_kendaraan = "sepeda motor"
    if durasi > 12 :
        kategori = "mengginap".title()
        biaya = 50000
    else:
        biaya = durasi * 5000
        kategori = "tidak mengginap".title()

elif jenis == 2:
    nm_kendaraan = "mobil".title()
    if durasi > 12 : 
        kategori = "mengginap".title()
        biaya = 75000
    else:
        biaya = durasi * 7500
        kategori = "tidak mengginap".title()

elif jenis == 3 :
    nm_kendaraan = "truck".title()
    if durasi > 12 :
        kategori = "mengginap".title()
        biaya = 250000
    else :
        biaya = durasi * 25000
        kategori = "tidak mengginap".title()


print("Catatan Pembayaran Anda")
print(f"""
jenis kendaraan : {nm_kendaraan}
durasi parkir : {durasi}
kendaraan anda termasuk kategori : {kategori}
""".title())

# bayar = int(input(f"masukan biaya parkir : sebesar Rp.{biaya} : ".title()))


while True :
    bayar = int(input(f"masukan biaya parkir : sebesar Rp.{biaya} : ".title()))

    if bayar > biaya :
        print(f"uang anda kelebihan silahkan ambil kembalian anda : {bayar - biaya}")
        break

    elif bayar < biaya :
        print("mohon maaf uang anda tidak cukup silahkan masukan sesuai biaya yang tertera")
    else:
        break
    
print("terimakasih sudah menggunakan sistem kami".title())
print("sampai jumpa lagi".title())



