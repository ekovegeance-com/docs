#!/usr/bin/python

daftar_belanja = ['apel','mangga','wortel','pisang']
print ('barang tersebut :')
for barang in daftar_belanja:
    print (barang)
print ('Saya harus membeli beras')
daftar_belanja.append('beras')
print ('daftar belanja sekarang :',(daftar_belanja))

print ('Saya akan mengurutkan daftar belanja saya')
daftar_belanja.sort()
print ('daftar belanja setelah diurutkan',(daftar_belanja))
print ('barang yang harus saya beli pertama', (daftar_belanja[0]))
barang_pertama = daftar_belanja[0]
del daftar_belanja [0]
print ('Saya membeli', (barang_pertama))
print ('daftar belanja sekarang :', (daftar_belanja))
