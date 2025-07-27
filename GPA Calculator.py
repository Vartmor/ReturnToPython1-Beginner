while True:
    try:
        ders_sayisi = int(input("Toplam kac ders notunun ortalamasini hesaplayacaksiniz? : "))
        if ders_sayisi > 0:
            break
        else:
            print("Pozitif sayi gir.")
    except ValueError:
        print("Gecerli sayi gir.")


dersler = [None] * ders_sayisi
ders_notlari = [None] * ders_sayisi



i=0
while i < ders_sayisi:
    dersler[i] = input(f'{i+1}. dersin adini yazar misiniz? : ')

    try:
        ders_notlari[i] = int(input(f'{dersler[i]} dersinden kac aldigini yazar misiniz? : '))
        if ders_notlari[i] < 0 or ders_notlari[i] > 100:
            print("0 ve 100 arasinda bir not girebilirsin.")
            continue
    except ValueError:
        print("gecerli bir SAYI girmelisin")
        continue


    i = i+1

def ortalama_hesapla():
    toplam = 0
    i= 0
    while i in range(ders_sayisi):
        toplam = toplam + ders_notlari[i]
        i = i +1
    ortalama = toplam / ders_sayisi
    b=0
    while b in range(ders_sayisi):
        print("-----------------------")
        print(f'{dersler[b]} dersinden aldigin not: {ders_notlari[b]}')
        b = b +1

    if ortalama >= 85:
        print(f'harikasin! ortalaman: {ortalama}')
    elif 70 <= ortalama <= 84:
        print(f'iyi! ortalaman: {ortalama}')
    elif 50<= ortalama <= 69:
        print(f'hmm fena degil. ortalaman: {ortalama}')
    elif 0<= ortalama <= 49:
        print(f'malesef kaldin. ortalaman: {ortalama}')





ortalama_hesapla()











