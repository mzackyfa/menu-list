print ("====Pilih Menu====")
print (" " " " " " " " "1.Makanan")
print (" " " " " " " " "2.Minuman")
print ("===================")
daftar_menu = int(input("Pilih Menu Diatas 1/2:"))

def subMenu1(makanan):
    if daftar_menu == 1:
        print ("Daftar Makanan:", makanan)
    else:
        return
subMenu1("Rp. 34,000 nasiGoreng")
subMenu1("Rp. 23,000 mieGoreng")
subMenu1("Rp. 12,000 kerakTelor")
subMenu1("Rp. 23,000 mieRebus")
subMenu1("Rp. 35,000 ayamGoreng")


def subMenu2(minuman):
    if daftar_menu == 2:
        print ("Daftar Minuman:", minuman)
    else:
       return
subMenu2("Rp. 8,000 airPutih")
subMenu2("Rp. 10,000 esTeh")
subMenu2("Rp. 24,000 jusMangga")
subMenu2("Rp. 20,000 jusAlpukat")
subMenu2("Rp. 21,000 jusSirsak")



def total(harga, jumlah):
    if harga.lower() == "airputih":
        return airPutih * jumlah
    elif harga.lower() == "esteh":
        return esTeh * jumlah
    elif harga.lower() == "jusmangga":
        return jusMangga * jumlah
    elif harga.lower() == "jusalpukat":
        return jusAlpukat * jumlah
    elif harga.lower() == "jussirsak":
        return jusSirsak * jumlah
    elif harga.lower() == "nasigoreng":
        return nasiGoreng * jumlah
    elif harga.lower() == "miegoreng":
        return mieGoreng * jumlah
    elif harga.lower() == "keraktelor":
        return kerakTelor * jumlah
    elif harga.lower() == "ayamgoreng":
        return ayamGoreng * jumlah
    else:
        print("Menu tidak valid")
        return 0


nasiGoreng = 34000
mieGoreng = 23000
kerakTelor = 12000
mieRebus = 23000
ayamGoreng = 35000

airPutih = 8000
esTeh = 10000
jusMangga = 24000
jusAlpukat = 20000
jusSirsak = 21000


harga = input("Makanan/Minuman yang anda pilih: ")
jumlah = int(input("Masukkan Jumlah: "))
Total = total(harga, jumlah)

if Total > 500000:
    Total = Total - 0.25 * Total
    print("Nominal Pembayaran Diskon 25%: Rp.", Total)
elif Total > 250000:
    Total = Total - 0.15 * Total
    print("Nominal Pembayaran Diskon 15%: Rp.", Total)
elif Total > 100000:
    Total = Total - 0.10 * Total
    print("Nominal Pembayaran Diskon 10%: Rp.", Total)
else:
    print("Nominal Pembayaran:", Total)


Nim=int(input("Masukkan NIM:"))
Nama=input("Nama Anda:")
print("====================================")
Bayar=int(input("Jumlah Nominal Pembayaran:"))
Kembalian=(Bayar-Total)
print("====================================")
print("Nama:", Nama ,"|", "Nim:", Nim)
print("Uang Kembalian:","Rp.",Kembalian)
