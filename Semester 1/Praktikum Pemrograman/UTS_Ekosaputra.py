luas=0.0
while True:
   print ("PROGRAM CONTOH PENGGUNAAN PERINTAH While")
   print ("MENU PROGRAM")
   print ("1. Menghitung Luas Segitiga")
   print ("2. Menghitung Luas Lingkaran")
   print ("0. Keluar")
   line=input('>')
   if line=='exit':
     break
   elif line[0]=='1':
     alas=int(input('Ketikan alas segitiga : '))
     tinggi=int(input('Ketikan tinggi segitiga : '))
     luas=(alas*tinggi)/2
     print ("Luas Segitiga = ",luas)
print ('Keluar')