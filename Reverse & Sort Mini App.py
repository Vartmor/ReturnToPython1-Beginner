girilecek_sayi_adedi = int(input("kac tane sayi gireceksin? : "))
girilen_sayilar = [0] * girilecek_sayi_adedi

i=0
while i < girilecek_sayi_adedi:
    girilen_sayilar[i] = int(input(f'{i+1}. sayiyi gir : '))
    i = i+1


print(f'orijinal liste: {girilen_sayilar}')
girilen_sayilar.reverse()
print(f'ters cevirilmis liste: {girilen_sayilar}')
girilen_sayilar.sort(reverse=False)
print(f'kucukten buyuge siralanmis liste: {girilen_sayilar}')











