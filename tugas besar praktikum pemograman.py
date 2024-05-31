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
        totalharga += hargamenunasgor[pesanan -1]
    return totalharga

def totalsemua():
    hargamenunasgor = [13000, 15000, 15000, 17000, 22000, 13000, 13000, 13000, 3000, 5000, 10000]
    menu = []

  
    while True:
        pesanan = input("Masukkan nomor menu yang ingin dipesan (ketik 0 untuk total harga yang harus dibayar): ")

        if pesanan == "0":
          break

        pesanan = int(pesanan)
        if pesanan < 1 or pesanan > len(hargamenunasgor):
            print("mohon maaf pesanan yang anda input tidak ada di menu. Silahkan masukan kembali nomor pesanan yang ada di menu!")
            continue

      menu.append(pesanan)

  if len(menu) == 0:
      print("tidak ada yang dipesan")
  else:
      totalharga = totalsemuahargamenu(menu, hargamenunasgor)
      print("Total harga: Rp.", totalharga)

      menu.sort()
      print("Pesanan Anda: ")
      for pesanan in menu:
          if pesanan <=5 :
              kategori = "Makanan"
          else pesanan >=5 :
              kategori = "Minuman"
        
          if pesanan == 1:
              item = "Nasi goreng biasa"
          elif pesanan == 2:
              item = "Nasi goreng sosis"
          elif pesanan == 3:
              item = "Nasi goreng bakso"
          elif pesanan == 4:
              item = "Nasi goreng ati ampela"
          elif pesanan == 5:
              item = "Nasi goreng Spesial"
          elif pesanan == 6:
              item = "Kwetiau goreng"
          elif pesanan == 7:
              item = "Mie goreng"
          elif pesanan == 8:
              item = "Mie kuah"
          elif pesanan == 9:
              item = "Es teh"
          elif pesanan == 10:
              item = "Es jeruk"
          elif pesanan == 11:
              item = "Es buah"
        
          print(f"- {kategori}: {item}")

totalsemua()
        


    

       
    


    
  
 

 



    
