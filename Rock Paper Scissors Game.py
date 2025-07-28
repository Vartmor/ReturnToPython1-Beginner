import random

user_wins = 0
computer_wins= 0

print("Tas kagit makas oyununa hos geldin!")


while True:

    kullanici_secim = int(input("\nLutfen bir secim yap.\n \nTas:1 \nKagit:2 \nMakas:3 \ncikis:4 \nsecim: "))
    bilgisayar_secim = random.randint(1,3)

    if kullanici_secim == 4:
        print(f"Oyun bitti!\nOyuncu skoru: {user_wins}\nBilgisayar skoru: {computer_wins}")
        break

    if kullanici_secim == 1:
        kullanici_secim = "Tas"
    elif kullanici_secim == 2:
        kullanici_secim = "Kagit"
    elif kullanici_secim == 3:
        kullanici_secim = "Makas"

    if bilgisayar_secim == 1:
        bilgisayar_secim = "Tas"
    elif bilgisayar_secim == 2:
        bilgisayar_secim = "Kagit"
    elif bilgisayar_secim == 3:
        bilgisayar_secim = "Makas"




    if kullanici_secim == bilgisayar_secim:
        print(f'Esitlik! kullanici {kullanici_secim} ve bilgisayar {bilgisayar_secim} secti, kimseye puan eklenmedi.')

    elif kullanici_secim == "Tas" and bilgisayar_secim == "Kagit":
        print(f'Bilgisayar kazandi! kullanici {kullanici_secim} ve bilgisayar {bilgisayar_secim} secti, bilgisayar +1 puan.')
        computer_wins = computer_wins +1

    elif kullanici_secim == "Tas" and bilgisayar_secim == "Makas":
        print(f'Oyuncu kazandi! kullanici {kullanici_secim} ve bilgisayar {bilgisayar_secim} secti, oyuncu +1 puan.')
        user_wins = user_wins +1

    elif kullanici_secim == "Kagit" and bilgisayar_secim == "Tas":
        print(f'Oyuncu kazandi! kullanici {kullanici_secim} ve bilgisayar {bilgisayar_secim} secti, oyuncu +1 puan.')
        user_wins = user_wins +1

    elif kullanici_secim == "Kagit" and bilgisayar_secim == "Makas":
        print(f'Bilgisayar kazandi! kullanici {kullanici_secim} ve bilgisayar {bilgisayar_secim} secti, bilgisayar +1 puan.')
        computer_wins = computer_wins +1

    elif kullanici_secim == "Makas" and bilgisayar_secim == "Tas":
        print(f'Bilgisayar kazandi! kullanici {kullanici_secim} ve bilgisayar {bilgisayar_secim} secti, bilgisayar +1 puan.')
        computer_wins = computer_wins +1

    elif kullanici_secim == "Makas" and bilgisayar_secim == "Kagit":
        print(f'Oyuncu kazandi! kullanici {kullanici_secim} ve bilgisayar {bilgisayar_secim} secti, oyuncu +1 puan.')
        user_wins = user_wins +1

    print(f'Guncel skorlar: Kullanici -> {user_wins} ve Bilgisayar -> {computer_wins} .')



#Another example can be found below.

    import random

    user_wins = 0
    computer_wins = 0

    secenekler = {
        1: "Tas",
        2: "Kagit",
        3: "Makas"
    }

    print("Tas Kagit Makas oyununa hos geldin!")

    while True:
        try:
            secim = int(input("\nLütfen bir seçim yap:\n1 - Taş\n2 - Kağıt\n3 - Makas\n4 - Çıkış\nSeçim: "))
        except ValueError:
            print("Rakam girmen lazim kardesim.")
            continue

        if secim == 4:
            print(f"\nOyun bitti!\nOyuncu skoru: {user_wins}\nBilgisayar skoru: {computer_wins}")
            break

        if secim not in secenekler:
            print("Geçerli bir seçim yapmadın.")
            continue

        kullanici = secenekler[secim]
        bilgisayar = secenekler[random.randint(1, 3)]

        print(f"Kullanici: {kullanici} | Bilgisayar: {bilgisayar}")

        if kullanici == bilgisayar:
            print("➖ Beraberlik! Kimseye puan yok.")
        elif (kullanici == "Tas" and bilgisayar == "Makas") or \
                (kullanici == "Kagit" and bilgisayar == "Tas") or \
                (kullanici == "Makas" and bilgisayar == "Kagit"):
            print("✅ Oyuncu kazandı!")
            user_wins += 1
        else:
            print("❌ Bilgisayar kazandı!")
            computer_wins += 1

        print(f"📊 Skorlar → Oyuncu: {user_wins} | Bilgisayar: {computer_wins}")








