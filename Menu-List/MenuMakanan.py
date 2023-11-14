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
subMenu1("Rp. 34,000 Nasi Goreng")
subMenu1("Rp. 23,000 Mie Goreng")
subMenu1("Rp. 12,000 Kerak Telor")
subMenu1("Rp. 23,000 Mie Rebus")
subMenu1("Rp. 35,000 Ayam Goreng")

def subMenu2(minuman):
    if daftar_menu == 2:
        print ("Daftar Minuman:", minuman)
    else:
       return
subMenu2("Rp. 8,000 Air Putih")
subMenu2("Rp. 23,000 Jus Stawberry")
subMenu2("Rp. 24,000 Jus Mangga")
subMenu2("Rp. 20,000 Jus Alpukat")
subMenu2("Rp. 21,000 Jus Sirsak")

def total(harga, jumlah):
    return harga * jumlah

harga = int(input("Masukkan Harga: "))
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
    print("Tidak Mendapat Diskon :(")

Nim=int(input("Masukkan NIM:"))
Nama=input("Nama Anda:")
print("====================================")
Bayar=int(input("Jumlah Nominal Pembayaran:"))
Kembalian=(Bayar-Total)
print("====================================")
print("Nama:", Nama ,"|", "Nim:", Nim)
print("Uang Kembalian:","Rp.",Kembalian)
