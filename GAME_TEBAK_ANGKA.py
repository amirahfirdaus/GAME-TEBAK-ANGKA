print (10* "=", "SELAMAT DATANG DI GAME TEBAK ANGKA", 10* "=")
print ("Kesempatan anda sebanyak 7 kali, masukkan angka dari 0 sampai 100")

import random
kesempatan = 0 
angka = random.randint(0,100)

while kesempatan <=7 :
    tebakangka = int(input("Masukkan Angka Tebakan :" ))
    if kesempatan == 7:
        print ("Anda Kurang Beruntung")
        break
    elif tebakangka < angka :
        print ("Tidak tepat, angka terlalu kecil")
    elif tebakangka > angka :
        print ("Tidak tepat, angka terlalu besar")
    elif tebakangka == angka :
        print ("Tebakan anda tepat, anda menebak sebanyak", (kesempatan+1), "kali" )
        break 
    kesempatan +=1
    