day = int(input("Введите день: "))
month = int(input("Введите месяц: "))

if month == 3:
    if day >= 21:
        print("Овен")
    else:
        print("Рыбы")

elif month == 4:
    if day <= 20:
        print("Овен")
    else:
        print("Телец")

elif month == 5:
    if day <= 21:
        print("Телец")
    else:
        print("Близнецы")

elif month == 6:
    if day <= 21:
        print("Близнецы")
    else:
        print("Рак")

elif month == 7:
    if day <= 22:
        print("Рак")
    else:
        print("Лев")

elif month == 8:
    if day <= 21:
        print("Лев")
    else:
        print("Дева")

elif month == 9:
    if day <= 23:
        print("Дева")
    else:
        print("Весы")

elif month == 10:
    if day <= 23:
        print("Весы")
    else:
        print("Скорпион")

elif month == 11:
    if day <= 22:
        print("Скорпион")
    else:
        print("Стрелец")

elif month == 12:
    if day <= 22:
        print("Стрелец")
    else:
        print("Козерог")

elif month == 1:
    if day <= 20:
        print("Козерог")
    else:
        print("Водолей")

elif month == 2:
    if day <= 19:
        print("Водолей")
    else:
        print("Рыбы")

else:
    print("Ошибка месяца")