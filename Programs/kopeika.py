def money(coin):
    rub = coin // 100
    coin = coin % 100
    if rub > 0:
        if rub % 10 == 1:
            print(str(rub) + " РУБЛЬ")
        elif (10 <= rub <= 20) or (rub % 10 == "0", "5", "6", "7", "8", "9"):
            print(str(rub) + " РУБЛЕЙ")
        else:
            print(str(rub) + " РУБЛЯ")
    if coin % 10 == 1:
        print(str(coin) + " КОПЕЙКА")
    elif (10 <= coin <= 20) or (coin % 10 == "0", "5", "6", "7", "8", "9"):
        print(str(coin) + " КОПЕЕК")
    else:
        print(str(coin) + " КОПЕЙКИ")


coin = int(input("Введите количество копеек: "))
money(coin)