while True:
    slovo = input("Введите слово : ")

    if slovo.lower() == "exit":
        break

    glasnye_bukvy = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"   # cписок гласных букв

    kol_vo_glasnyh = 0
    kol_vo_soglasnyh = 0

    for bukva in slovo:
        if bukva.isalpha():
            if bukva in glasnye_bukvy:
                kol_vo_glasnyh += 1
            else:
                kol_vo_soglasnyh += 1

    obshee_kol_vo = kol_vo_glasnyh + kol_vo_soglasnyh

    if obshee_kol_vo > 0:
        print("Всего букв:", obshee_kol_vo_kol_vo)
        print("Гласных:", kol_vo_glasnyh)
        print("Согласных:", kol_vo_soglasnyh)
        print("Проценты:",
              f"{kol_vo_glasnyh/obshee_kol_vo*100:.2f}% / {kol_vo_soglasnyh/obshee_kol_vo*100:.2f}%")
    print()