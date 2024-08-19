import random
def tas_kagit_makas_Berra_Zeren_Hol():
    print("Taş, Kağıt, Makas oyununa hoşgeldiniz!")
    print("İşte oyunu nasıl oynayacağınız:")
    print("Lütfen her set başladığında aşağıdaki elemanlar listesinden bir eleman giriniz.")
    print("Elemanlar = ['Taş', 'Kağıt', 'Makas']")
    print("Oyundan ayrılmak için 'Çıkış' yazmanız yeterli.")
    print("Bol şans!")
    OyuncuSkoru = 0
    BilgisayarSkoru = 0
    TurSayısı = 0
    OyunSayısı = 0
    elemanlar = ["Taş", "Kağıt", "Makas"]
    Oyuncu = input("Elemanlardan seçtiğinizi girin. Eğer devam etmek istemiyorsanız lütfen 'Çıkış' yazınız: ")
    Bilgisayar = random.choice(elemanlar)
    while Oyuncu != "Çıkış":
        if Oyuncu == "Taş" and Bilgisayar == "Taş":
            if OyuncuSkoru == 2 or BilgisayarSkoru == 2:
                OyunSayısı += 1
            if (Oyuncu != "Çıkış"):
                TurSayısı += 1
            print(f'Oyun = {OyunSayısı}     Tur = {TurSayısı}')
            OyuncuSkoru += 0
            BilgisayarSkoru += 0
            print(f'Bilgisayar bunu seçti: {Bilgisayar}')
            print("Ah ne yazık berabere! İşte skorunuz:")
            print(f'Oyuncu = {OyuncuSkoru}   Bilgisayar = {BilgisayarSkoru}')
            Oyuncu = input("'Taş', 'Kağıt', 'Makas'tan birini seçiniz veya çıkmak için 'Çıkış' yazınız: ")
        elif Oyuncu == "Taş" and Bilgisayar == "Kağıt":
            if OyuncuSkoru == 2 or BilgisayarSkoru == 2:
                OyunSayısı += 1
            if Oyuncu != "Çıkış":
                TurSayısı += 1
            print(f'Oyun = {OyunSayısı}     Tur = {TurSayısı}')
            OyuncuSkoru += 0
            BilgisayarSkoru += 1
            print(f'Bilgisayar bunu seçti: {Bilgisayar}')
            print("Şanssız gününzdesiniz yenildiniz. Aşağıda skorunuzu göreceksiniz. Üzülmeyin bir tur daha?")
            print(f'Oyuncu = {OyuncuSkoru}   Bilgisayar = {BilgisayarSkoru}')
            Oyuncu = input("'Taş', 'Kağıt', 'Makas'tan birini seçiniz veya çıkmak için 'Çıkış' yazınız: ")
        elif Oyuncu == "Taş" and Bilgisayar == "Makas":
            if OyuncuSkoru == 2 or BilgisayarSkoru == 2:
                OyunSayısı += 1
            if Oyuncu != "Çıkış":
                TurSayısı += 1
            print(f'Oyun = {OyunSayısı}     Tur = {TurSayısı}')
            OyuncuSkoru += 1
            BilgisayarSkoru += 0
            print(f'Bilgisayar bunu seçti: {Bilgisayar}')
            print("Şanslı gününüzdesiniz! Ne mutlu size! İşte skorunuz:")
            print(f'Oyuncu = {OyuncuSkoru}   Bilgisayar = {BilgisayarSkoru}')
            Oyuncu = input("'Taş', 'Kağıt', 'Makas'tan birini seçiniz veya çıkmak için 'Çıkış' yazınız: ")
        elif Oyuncu == "Kağıt" and Bilgisayar == "Taş":
            if OyuncuSkoru == 2 or BilgisayarSkoru == 2:
                OyunSayısı += 1
            if Oyuncu != "Çıkış":
                TurSayısı += 1
            print(f'Oyun = {OyunSayısı}     Tur = {TurSayısı}')
            OyuncuSkoru += 1
            BilgisayarSkoru += 0
            print(f'Bilgisayar bunu seçti: {Bilgisayar}')
            print("Şanslı gününüzdesiniz! Ne mutlu size! İşte skorunuz:")
            print(f'Oyuncu = {OyuncuSkoru}   Bilgisayar = {BilgisayarSkoru}')
            Oyuncu = input("'Taş', 'Kağıt', 'Makas'tan birini seçiniz veya çıkmak için 'Çıkış' yazınız: ")
        elif Oyuncu == "Kağıt" and Bilgisayar == "Kağıt":
            if OyuncuSkoru == 2 or BilgisayarSkoru == 2:
                OyunSayısı += 1
            if Oyuncu != "Çıkış":
                TurSayısı += 1
            print(f'Oyun = {OyunSayısı}     Tur = {TurSayısı}')
            OyuncuSkoru += 0
            BilgisayarSkoru += 0
            print(f'Bilgisayar bunu seçti: {Bilgisayar}')
            print("Ah ne yazık berabere! İşte skorunuz:")
            print(f'Oyuncu = {OyuncuSkoru}   Bilgisayar = {BilgisayarSkoru}')
            Oyuncu = input("'Taş', 'Kağıt', 'Makas'tan birini seçiniz veya çıkmak için 'Çıkış' yazınız: ")
        elif Oyuncu == "Kağıt" and Bilgisayar == "Makas":
            if OyuncuSkoru == 2 or BilgisayarSkoru == 2:
                OyunSayısı += 1
            if Oyuncu != "Çıkış":
                TurSayısı += 1
            print(f'Oyun = {OyunSayısı}     Tur = {TurSayısı}')
            OyuncuSkoru += 0
            BilgisayarSkoru += 1
            print(f'Bilgisayar bunu seçti: {Bilgisayar}')
            print("Şanssız gününzdesiniz yenildiniz. Aşağıda skorunuzu göreceksiniz. Üzülmeyin bir tur daha?")
            print(f'Oyuncu = {OyuncuSkoru}   Bilgisayar = {BilgisayarSkoru}')
            Oyuncu = input("'Taş', 'Kağıt', 'Makas'tan birini seçiniz veya çıkmak için 'Çıkış' yazınız: ")
        elif Oyuncu == "Makas" and Bilgisayar == "Taş":
            if OyuncuSkoru == 2 or BilgisayarSkoru == 2:
                OyunSayısı += 1
            if Oyuncu != "Çıkış":
                TurSayısı += 1
            print(f'Oyun = {OyunSayısı}     Tur = {TurSayısı}')
            OyuncuSkoru += 0
            BilgisayarSkoru += 1
            print(f'Bilgisayar bunu seçti: {Bilgisayar}')
            print("Şanssız gününzdesiniz yenildiniz. Aşağıda skorunuzu göreceksiniz. Üzülmeyin bir tur daha?")
            print(f'Oyuncu = {OyuncuSkoru}   Bilgisayar = {BilgisayarSkoru}')
            Oyuncu = input("'Taş', 'Kağıt', 'Makas'tan birini seçiniz veya çıkmak için 'Çıkış' yazınız: ")
        elif Oyuncu == "Makas" and Bilgisayar == "Kağıt":
            if OyuncuSkoru == 2 or BilgisayarSkoru == 2:
                OyunSayısı += 1
            if Oyuncu != "Çıkış":
                TurSayısı += 1
            print(f'Oyun = {OyunSayısı}     Tur = {TurSayısı}')
            OyuncuSkoru += 1
            BilgisayarSkoru += 0
            print(f'Bilgisayar bunu seçti: {Bilgisayar}')
            print("Şanslı gününüzdesiniz! Ne mutlu size! İşte skorunuz:")
            print(f'Oyuncu = {OyuncuSkoru}   Bilgisayar = {BilgisayarSkoru}')
            Oyuncu = input("'Taş', 'Kağıt', 'Makas'tan birini seçiniz veya çıkmak için 'Çıkış' yazınız: ")
        elif Oyuncu == "Makas" and Bilgisayar == "Makas":
            if OyuncuSkoru == 2 or BilgisayarSkoru == 2:
                OyunSayısı += 1
            if Oyuncu != "Çıkış":
                TurSayısı += 1
            print(f'Oyun = {OyunSayısı}     Tur = {TurSayısı}')
            OyuncuSkoru += 0
            BilgisayarSkoru += 0
            print(f'Bilgisayar bunu seçti: {Bilgisayar}')
            print("Ah ne yazık berabere! İşte skorunuz:")
            print(f'Oyuncu = {OyuncuSkoru}   Bilgisayar = {BilgisayarSkoru}')
            Oyuncu = input("'Taş', 'Kağıt', 'Makas'tan birini seçiniz veya çıkmak için 'Çıkış' yazınız: ")
        elif Oyuncu == "çıkış":
            print("Yaa gidiyor musunuz? Olsun güle güle, yine bekleriz!")
        else:
            Oyuncu = input("Geçersiz eleman. Lütfen geçerli bir eleman girin: ")




tas_kagit_makas_Berra_Zeren_Hol()
