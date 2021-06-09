print('''
nama: faiz hidayat
nim: 201420026
kelas: if2a
	''')
# Data : 6,4,5,3,0,7
# Buatlah Program untuk mengurutkan data dari angka yang besar ke angka yang kecil dengan mengunakan metode desending.
while True:
    print('''
=========
sort data
=========
menu:
1. ascending
2. Descending
0. exit
''')
    menu = int(input('input menu: '))
    if menu==1:
		while True:
			data = tuple(raw_input('Masukan data yang belum terurut : '))
			data_descending = sorted(data, reverse = True)
			# print ("Data yang belum terurut :",data)
			print("Data yang sudah terurut= ",data_descending)
			d = input('try again(y/n)? ')
			if d=='y' or d=='Y':
				print()
			elif d=='n' or d=='N':
				break

	elif menu==2:
		while True:
			data = tuple(raw_input('Masukan data yang belum terurut : '))
			data_descending = sorted(data, reverse = False)
			print ("Data yang belum terurut :",data)
			# print("Data yang sudah terurut= ",data_descending)
			d = input('try again(y/n)? ')
			if d=='y' or d=='Y':
				print()
			elif d=='n' or d=='N':
				break

	elif menu=0:
		exit()