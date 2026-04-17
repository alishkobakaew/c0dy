data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for x in data_tuple:
    if type(x) == str:
        letters.append(x)
    else:
        numbers.append(x)

numbers.remove(6.13) # удаленме числа

letters.append(True) # Перемещение True в конец

numbers.insert(1, 2)

numbers.sort() # Cортировка

letters.reverse()

letters[2] = 'b'
letters[4] = 'n'

for i in range(len(numbers)): # Возведение в степень
    numbers[i] = numbers[i] ** 2

    letters = tuple(letters) #Korteji
numbers = tuple(numbers)

print(letters)
print(numbers)
