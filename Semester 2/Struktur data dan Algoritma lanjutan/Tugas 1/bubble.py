def tukar(lists,i,j):
    lists[i],lists[j]=lists[j], lists[i]
    
def bubbleTugas(listku):
    perubahan = True
    sesi = len(listku) #banyaknya sesi yang digunakan untuk mengecek data dari awal
    while sesi > 1 and perubahan:
        perubahan = False
        j = 1
        while j < sesi:
            if listku[j]<listku[j-1]:
                perubahan = True
                tukar(listku,j,j-1) 
            j+=1
        print(listku)
        #Jika penanda 'perubahan' tidak terjadi maka perulangan berhenti dan artinya data sudah terurut tanpa melakukan perulangan lagi.
        if not perubahan:
            print("hasil akhir = %s" %str(listku))
        sesi-=1
print("==================================================================")
print("Sebelum Bubble Sort")
mylist=[50,22,65,30,10,15,10]
print(mylist)
print("Setelah Bubble Sort")
bubbleTugas(mylist)