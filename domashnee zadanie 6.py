def is_strong_password(password):
    if len(password) < 6:   #Длина пароля
        return False

    kolichestvo_cifr = 0
    kolichestvo_simvolov = 0
    big = False
    small = False

    for char in password:
        if char.isdigit():
            kolichestvo_cifr += 1
        elif char.isupper():
            big = True
        elif char.islower():
            small = True
        else:
            kolichestvo_simvolov += 1

    if kolichestvo_cifr == 2 and kolichestvo_simvolov == 2 and big and small:
        return True

    return False


# Проверка
print(is_strong_password("$PassW/12"))
print(is_strong_password("12345"))
print(is_strong_password("Pa55!!"))
print(is_strong_password("defnfelsa12#"))
print(is_strong_password("???!!!!"))
print(is_strong_password("k2-iR149;"))
