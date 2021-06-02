def tukar(lists,i,j):
    lists[i],lists[j]=lists[j], lists[i]
    
def bubbleTugas(listku):
    perubahan = True
    sesi = len(listku) 
    while sesi > 1 and perubahan:
        perubahan = False
        j = 1
        while j < sesi:
            if listku[j]<listku[j-1]:
                perubahan = True
                tukar(listku,j,j-1) 
            j+=1
        print(listku)
        if not perubahan:
            print("hasil akhir = %s" %str(listku))
        sesi-=1
print("==================================================================")
print("Sebelum Bubble Sort")
mylist=[35,50,10,45,15,15]
print(mylist)
print("Setelah Bubble Sort")
bubbleTugas(mylist)
