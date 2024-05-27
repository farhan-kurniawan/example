print("          Nasgor Bekasi Gila          ")
print("----------------Makanan----------------")
print("1. Nasi goreng biasa: Rp. 13.000")
print("2. Nasi goreng sosis: Rp. 15.000")
print("3. Nasi goreng bakso: Rp. 15.000")
print("4. Nasi goreng ati ampela: Rp. 17.000")
print("5. Nasi goreng Spesial: Rp. 22.000")
print("6. Kwetiau goreng: Rp. 13.000")
print("7. Mie goreng: Rp. 13.000")
print("8. Mie kuah: Rp. 13.000")
print("--------------Menu Minuman--------------")
print("9. Es teh: Rp. 3000")
print("10. Es jeruk: Rp. 5000")
print("11. Es buah: Rp. 10.000")

def totalsemuahargamenu(menu, hargamenunasgor):
  totalharga = 0
  for pesanan in menu:
    totalharga = hargamenunasgor
  return totalharga

def totalsemua(hargamenunasgor, menu):
  hargamenunasgor = [13000, 15000, 15000, 17000, 22000, 13000, 13000, 13000, 3000, 5000, 10000]
  menu = []

def totalsemua():
  while True:
        pesanan = input("Masukkan nomor menu yang ingin dipesan (ketik 0 untuk total harga yang harus dibayar): ")
    
 while True:
        try:
            pesanan = int(input("Masukkan nomor menu yang ingin dipesan (ketik 0 untuk total harga yang harus dibayar): "))
            if pesanan == 0:
                break
            elif 1 <= pesanan <= 11:
                menu.append(pesanan)
            else:
                print("Nomor menu tidak valid, silakan coba lagi.")
        except ValueError:
            print("Input tidak valid, silakan masukkan nomor menu yang benar.")
  



    
