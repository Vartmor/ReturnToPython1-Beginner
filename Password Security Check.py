
print("\nSifre guvenlik kontrol uygulamasina hos geldiniz.")
print("\nSifre olusturma kurallari:\n1-En az 8 karakter uzunlugunda olmali \n2-En az 1 harf, 1 rakam ve 1 ozel karakter icermeli (!@#$%^&*()-_+=<>?/\|{}[]~).")

kullanici_denemesi = input("Olusturmak istedigin sifreyi buraya gir: ")
kullanici_denemesi_list = []
rakamlar = ["0","1","2","3","4","5","6","7","8","9"]
ozel_karakterler = ["!" , "@" , "#" , "$" , "%" , "^" , "&" , "*", "(", ")", "-" , "_" ,"+" ,"=" , "<" , ">" , "?" , "/" , "\ ", "|" , "}", "[ ", "]", "~"]

for karakterler in kullanici_denemesi:
    kullanici_denemesi_list.append(karakterler)

#print(kullanici_denemesi_list)

def sifre_dogrula(liste: list) -> bool:


    rakam_sayisi = 0
    ozel_karakter_sayisi= 0

    if len(liste) < 8:
        print("sifrenizdeki karakter sayisi 8 veya daha fazla olmalidir.")
        return False

    for eleman in liste:
        if eleman in ozel_karakterler:
            ozel_karakter_sayisi = ozel_karakter_sayisi + 1

    for eleman in liste:
        if eleman in rakamlar:
            rakam_sayisi = rakam_sayisi + 1

    if rakam_sayisi == 0 and ozel_karakter_sayisi ==0:
        print("sifrenizde hic rakam ve ozel karakter yok")
        return False
    elif rakam_sayisi ==0 and ozel_karakter_sayisi>0:
        print("sifrenizde hic rakam yok")
        return False
    elif rakam_sayisi>0 and ozel_karakter_sayisi==0:
        print("sifrenizde hic ozel karakter yok")
        return False
    else:
        return True




sonuc = sifre_dogrula(kullanici_denemesi_list)

if sonuc:
    print("sifreniz basariyla olusturuldu: " + kullanici_denemesi)
else:
    print("\nprogram kapaniyor...")




#u can find what chatgpt did below:

def sifre_dogrula(sifre: str) -> bool:
    ozel_karakterler = "!@#$%^&*()-_+=<>?/\\|{}[]~"

    eksikler = []

    if len(sifre) < 8:
        eksikler.append("🔒 Şifre en az 8 karakter olmalı.")
    if not any(harf.isalpha() for harf in sifre):
        eksikler.append("🔡 En az 1 harf içermeli.")
    if not any(rakam.isdigit() for rakam in sifre):
        eksikler.append("🔢 En az 1 rakam içermeli.")
    if not any(ozel in ozel_karakterler for ozel in sifre):
        eksikler.append("🔧 En az 1 özel karakter içermeli.")

    if eksikler:
        print("\n".join(eksikler))
        return False
    return True


# Ana program
print("Şifre Güvenlik Kontrolü")
sifre = input("Şifrenizi girin: ")

if sifre_dogrula(sifre):
    print(f"✅ Şifre başarılı: {sifre}")
else:
    print("❌ Şifre geçersiz. Tekrar deneyin.")

