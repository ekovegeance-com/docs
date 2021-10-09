#Rumus slovin menghitung sampel
while True:
    try:
        N = int(input("Masukkan jumlah sampel: "))
        e = float(input("Masukkan nilai eksperimen: "))
        break
    except ValueError:
        print("Input harus berupa angka")

#rumusnyo
n = N / (1+(N * e**2))
hasilB = (1+(N * e**2))
bulat = round(hasilB,2)
dibulatkan = round(n)
#Outputnyo
print("Nilai sampel = ", N)
print("Nilai eksperimen = ", e)
print("hasil 1 + N x e2 = ", bulat)
print("Nilai n = ", n)
print("Nilai dibulatkan = ", dibulatkan)


