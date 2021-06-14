print('''
nama : faiz hidayat
nim  : 201420026
kelas: if2a

menu: 
1. METODE LIFO
2. METODE FIFO
0. exit
''')


while True:
	menu = int(input('input menu: '))
	if menu==1:
		while True: 
			print('\n1.METODE LIFO')
			data = [46,12,54]
			data.append(34)
			data.append(80)
			print('data = ',data)
			data.pop()
			print(data,'\n')
			break
	elif menu==2:
		while True:
			print('\n2. METODE FIFO')
			data = [38,6,2]
			data.insert(1,20)
			data.insert(1,56)
			print('data = ',data)
			data.pop()
			print('data = ',data)
			break
	elif menu==0:
		exit()