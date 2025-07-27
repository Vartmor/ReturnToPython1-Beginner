
print("Yapmak istediginiz islemi seciniz \n topla:1 \n cikar:2 \n carp:3 \n bol: 4")
islem = float(input("Islemı Gir:"))

if islem not in [1, 2, 3, 4]:
    print("Gecersiz islem talebi")
    exit()

sayi1 = int(input("Sayi 1 ="))
sayi2 = int(input("Sayi 2 ="))



def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b


def bol(a, b):
    return a / b


if islem == 1:
    print(f'Cevap: {topla(sayi1,sayi2)}')
elif islem == 2:
    print(f'Cevap: {cikar(sayi1,sayi2)}')
elif islem == 3:
    print(f'Cevap: {carp(sayi1,sayi2)}')
elif islem == 4:
    try:
        print(f'Cevap: {bol(sayi1,sayi2)}')
    except ZeroDivisionError:
        print("Sıfıra bölme canım.")







