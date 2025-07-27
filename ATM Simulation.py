user = "Ahmet"
user_current_balance = 1000
user_password = 1234

def withdraw(amount):
    global user_current_balance
    if amount <= 0:
        print("Negatif veya sifir para cekilemez.")
    elif amount > user_current_balance:
        print("Yetersiz bakiye.")
    else:
        user_current_balance -= amount
        print(f"{amount} TL cekildi. Yeni bakiye: {user_current_balance} TL")

def deposit(amount):
    global user_current_balance
    if amount <= 0:
        print("Negatif veya sifir para yatirilamaz.")
    else:
        user_current_balance += amount
        print(f"{amount} TL yatirildi. Yeni bakiye: {user_current_balance} TL")

def view_balance():
    print(f"Guncel bakiyeniz: {user_current_balance} TL")

def atm_menu():
    while True:
        try:
            secilen_islem = int(input(
                "\nLutfen islem seciniz:\n"
                "1 - Bakiye Goruntule\n"
                "2 - Para Cek\n"
                "3 - Para Yatir\n"
                "4 - Cikis\n"
                "Secim: "
            ))
        except ValueError:
            print("Gecerli bir sayi giriniz.")
            continue

        if secilen_islem == 1:
            view_balance()
        elif secilen_islem == 2:
            try:
                amount = float(input("Cekmek istediginiz tutar: "))
                withdraw(amount)
            except ValueError:
                print("Lutfen gecerli bir miktar giriniz.")
        elif secilen_islem == 3:
            try:
                amount = float(input("Yatirmak istediginiz tutar: "))
                deposit(amount)
            except ValueError:
                print("Lutfen gecerli bir miktar giriniz.")
        elif secilen_islem == 4:
            print("Cikis yapiliyor. Gorusmek uzere!")
            break
        else:
            print("Gecersiz secim.")

        input("\nDevam etmek icin Enter’a basin...")

# === Giriş Sistemi ===
print("Bankamatige Hos Geldiniz...")

hak = 3
while hak > 0:
    try:
        girilen_sifre = int(input("Lutfen 4 haneli sifrenizi giriniz: "))
    except ValueError:
        print("Sifre yalnizca rakam olmalidir.")
        continue

    if girilen_sifre == user_password:
        print(f"Hos geldiniz, {user}.")
        atm_menu()
        break
    else:
        hak -= 1
        print(f"Yanlis sifre. Kalan hak: {hak}")

else:
    print("Cok fazla hatali giris yapildi. Kart bloke edildi.")
