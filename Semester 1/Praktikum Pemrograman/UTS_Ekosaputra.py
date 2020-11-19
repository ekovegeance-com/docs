# Banner
print("[]=====UNIVERSITAS BINA DARMA PALEMBANG======[]")
print("         [] Nama : Eko Saputra []")
print("         [] NIM  : 201420001   []")
print("    [] Fakultas : Ilmu Komputer   []")
print("   [] Prodi : Teknik Informatika   []")
print('-'*60)
print("Website : www.ekovegeance.xyz   | Github : @ekovegeance")
print('.')
print(" TUGAS PRAKTIKUM PEMOGRAMAN V.4UTS")


def lingkaran (r): # Luas Lingkaran
    return 3.14 * (r*r) 

while True:
    print('\nMenu operasi:\n1. Lingkaran\n2. Ganjil Genap\n3. Tutup')
    line = int(input('silahkan masukan menu pilihan (dalam angka): '))
    if line == 1:
        r = input('Masukan jari -jari lingkaran: ')
        luas = lingkaran(int(r))
        print('Luasnya: {}'.format(luas))
    elif line == 2: # Ganjil Genap
        bilangan = int(input('masukan angka : '))
        if (bilangan % 2) == 0:
                print(bilangan,"adalah bilangan genap")
        else:
                print(bilangan,"adalah bilangan ganjil")
    elif line == 3:
        break
    else:
        print('Operasi tidak dikenali')