import math

def asal_kontrol(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(math.sqrt(sayi)) + 1):
        if sayi % i == 0:
            return False
    return True

while True:
    try:
        girilen_sayi = int(input("Girdiğiniz sayıya kadarki asal sayılar listelenecek: "))
        if girilen_sayi < 2:
            print("Lütfen 2 veya daha büyük bir sayı girin.")
            continue
        break
    except ValueError:
        print("Geçerli bir tam sayı girin.")

for j in range(2, girilen_sayi + 1):
    if asal_kontrol(j):
        print(j)
