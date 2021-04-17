#!/usr/bin/python


kebun_binatang = ['ular python', 'gajah', 'pinguin']
print ('jumlah binatang yang ada di kebun binatang :',len(kebun_binatang))

kebun_binatang_baru = ['monyet', 'unta', kebun_binatang]
print ('jumlah kandang di kebun binatang baru:',len(kebun_binatang_baru))
print ('binatang yang ada di kebun bintatang baru:',(kebun_binatang_baru))
print ('binatang dari kebun binatang lama:', (kebun_binatang_baru[2]))
print ('binatang terakhir dari kebun binatang lama:',(kebun_binatang_baru[2][2]))

jumlah_binatang = len(kebun_binatang_baru) - 1 + len(kebun_binatang_baru[2])
print ('jumlah binatang yang ada di kebun binatang baru :',(jumlah_binatang))
