## 🎂 foodDrinkMenu 
#### Needed :
Choose integer 1 or 2
```py
daftar_menu = int(input("Pilih Menu Diatas 1/2:"))
```
Input the price
```py
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

def total(harga , jumlah):
    return harga*jumlah

harga = int(input("Masukkan Harga: "))
```
Input Total of the Food or Drink price
```py
jumlah = int(input("Masukkan Jumlah: "))
Total = total(harga, jumlah)
```
Input your NIM and Name
```py
Nim=int(input("Masukkan NIM:"))
Nama=input("Nama Anda:")
print("====================================")
Bayar=int(input("Jumlah Nominal Pembayaran:"))
Kembalian=(Bayar-Total)
print("====================================")
print("Nama:", Nama ,"|", "Nim:", Nim)
print("Uang Kembalian:","Rp.",Kembalian)
```
