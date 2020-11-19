#Banner aku
import sys
from termcolor import colored, cprint
print(colored('[---]  UNIVERSITAS BINA DARMA PALEMBANG    [---]', 'blue'))
print(colored('[---]', 'blue'), colored('   TUGAS PRAKTIKUM PEMROGRAMAN      ', 'green'), colored('[---]', 'blue'))
print(colored('[---]', 'blue'), colored('     Nama : Eko Saputra             ', 'red'), colored('[---]', 'blue'))
print(colored('[---]', 'blue'), colored('     NIM  : 201420001               ', 'red'), colored('[---]', 'blue'))
print(colored('[---]', 'blue'), colored(' Fakultas : Ilmu Komputer           ', 'red'), colored('[---]', 'blue'))
print(colored('[---]', 'blue'), colored('    Prodi : Teknik Informatika      ', 'red'), colored('[---]', 'blue'))
print(colored('Website : www.ekovegeance.xyz   | Github : @ekovegeance', 'green'))

print(" TUGAS PRAKTIKUM PEMOGRAMAN V.2")

#Program konversi
suhu = input("Masukan suhu? (Misal: 30C, 20F): ")
drjt = int(suhu[:-1])
inputan = suhu[-1]

if inputan.upper() == "C":
  hasil1 = float((9 * drjt) / 5 + 32)
  hasil2 = float(drjt + 273.15)
  jenisX = "Celcius"
  jenis1 = "Fahrenheit"
                
elif inputan.upper() == "F":
  hasil1 = float((drjt - 32) * 5 / 9)
  hasil2 = float(((drjt - 32) * 5 / 9) + 273.15)
  jenisX = "Fahrenheit"
  jenis1 = "Celsius"

print(drjt,jenisX,"=","{:.1f}".format(hasil1),jenis1)

while True:

    cont = input("Mau coba lagi? Y/N > ")
    while cont.lower() not in ("yes","no"):
        cont = input("Mau coba lagi? Y/N > ")
    if cont == "no":
        break