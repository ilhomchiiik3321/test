print('Assalomu aleykum!')
print('Iltimos pin-kodni kiriting')
kiritilgan_kod = input('pin-kod: ')

pin_kod = '0207'

if kiritilgan_kod == pin_kod:
    print("Pin-kod to'g'ri!")
    print('Bankomatga xush kelibsiz!')

    balance = 100000
    while True:
        print("1 - Balance")
        print("2 - Mablag' qo'shish")
        print("3 - Mablag' yechish")
        print("4 - Kommunal hizmatlar uchun to'lovlar")
        print("0 - Chiqish")


        print("[1] [2] [3] [4] [0]")
        command = int(input("Komandani tanlang => "))

        if command == 0:
            print("Dastur tugadi!")
            break
        elif command == 1:
            print(f"Sizning balansingiz {balance} so'm")
        elif command == 2:
            qoshish = int(input("Mablag'ni kiriting: "))
            balance += qoshish
            print(f"{qoshish}so'm muvaffaqiyatli qo'shildi! Hozirgi balansingiz {balance}so'm")
        elif command == 3:
            yechish = int(input("Qancha yechmoqchisiz: "))
            if balance >= yechish:
                balance -= yechish
                print(f"{yechish}so'm muvaffaqiyatli yechildi! Hozirgi balansingiz {balance}so'm")
            else:
                print(" Hisonbingizda mablag' yetarli emas")
        elif command == 4:
            print("Kommunal hizmatlar!")
            print("Quyidagilardan birini tanlang:")
            print("1 - Svet uchun to'lov")
            print("2 - Gaz uchun to'lov")
            print("3 - Sovuq suv ucuhun to'lov")
            print("4 - Issiq suv uchun to'lov")
            print("5 - MIB uchun to'lov")
            print("0 - Chiqish")
            print("[1] [2] [3] [4] [0]")
            command = int(input("Komandani tanlang => "))
            if command == 0:
                print("Dastur tugadi!")
                break
            elif command == 1:
                svet = int(input("Mablag'ni kiriting: "))
                if balance >= svet:
                    balance -= svet
                    print("Svet uchun to'lov muvaffaqiyatli to'llandi! ")

                else:
                    print("Hisom=bingizda mablag' yetarli emas!")
            elif command == 2:
                gaz = int(input("Mablag'ni kiriting: "))
                if balance >= gaz:
                    balance -= gaz
                    print("Gaz uchun to'lov muvaffaqiyatli to'landi!")
                else:
                    print("Hisobingizda mablag' yetarli emas!")
            elif command == 3:
                sovuq_suv = int(input("Mablag'ni kiriting: "))
                if balance >= sovuq_suv:
                    balance -= sovuq_suv
                    print("Sovuq suv uchun to'lov muvaffaqiyatli to'landi!")
                else:
                    print("Hisobingizda mablag' yetarli emas!")
            elif command == 4:
                issiq_suv = int(input("Mablag'ni kiriting: "))
                if balance >= issiq_suv:
                    balance -= issiq_suv
                    print("Issiq suv uchun to'lov!")
                else:
                    print("Hisobingizda mablag' yetarli emas!")
            elif command == 5:
                mib = int(input("Mablag'ni kiriting: "))
                if balance >= mib:
                    balance -= mib
                    print("MIB uchun to;lov muvaffaqiyatli to'landi!")
                else:
                    print("Hisobingizda mablag' yetarli emas!")
        else:
            print("Notug'ri lomanda kiritildi")
else:
    print("Notug'ri pin-kod. Kirish rad etildi!!!")



