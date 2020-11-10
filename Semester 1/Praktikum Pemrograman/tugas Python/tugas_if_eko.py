#Banner aku
from termcolor import colored
print(colored('[---]  UNIVERSITAS BINA DARMA PALEMBANG    [---]', 'blue'))
print(colored('[---]', 'blue'), colored('   TUGAS PRAKTIKUM PEMROGRAMAN      ', 'green'), colored('[---]', 'blue'))
print(colored('[---]', 'blue'), colored('     Nama : Eko Saputra             ', 'red'), colored('[---]', 'blue'))
print(colored('[---]', 'blue'), colored('     NIM  : 201420001               ', 'red'), colored('[---]', 'blue'))
print(colored('[---]', 'blue'), colored(' Fakultas : Ilmu Komputer           ', 'red'), colored('[---]', 'blue'))
print(colored('[---]', 'blue'), colored('    Prodi : Teknik Informatika      ', 'red'), colored('[---]', 'blue'))
print(colored('Website : www.ekovegeance.xyz   | Github : @ekovegeance', 'green'))

print(" TUGAS PRAKTIKUM PEMOGRAMAN V.3 Notasi IF")

#Program greeting

jam = input("Masukan jam anda ? ")

if 0 <= int(jam) <= 12:
    print("Good Morning")

elif 13 <= int(jam) <= 16:
    print("Good Afternoon")

elif 17 <= int(jam) <= 20:
    print("Good Evening")

elif 21 <= int(jam) <= 24:
    print("Good Night")

else:
    print("Wrong Input")