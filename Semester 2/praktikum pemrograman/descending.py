print('Nama : M Yoga Richard Saput')
print('NIM : 201420032')
print('Kelas: IF2A')
while True:
    		print( 'Descending')
    		data = tuple(input('Masukan data yang belum terurut : '))
    		data_descending = sorted(data, reverse = True)
    		print('print data yang belum terurut: ',data)
    		print("Data yang sudah terurut: ",data_descending)
    		d = input('try again(y/n)? ')
    		if d=='y' or d=='Y':
    			print()
    		elif d=='n' or d=='N':
    			break
