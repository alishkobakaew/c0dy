data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

#  Пустые списки
designations = []
codes = []

#  Разделяем строки и коды
for x in data:
    if x.isdigit():
        codes.append(x)
    else:
        designations.append(x)

#  Создаем словарь
operators = {}
current_operator = None

for element in data:
    if not element.isdigit():
        current_operator = element
        operators[current_operator] = set()
    else:
        operators[current_operator].add(element)

#  Удаляем неработающих операторов
operators.pop("Katel", None)
operators.pop("Fonex", None)

#  Добавляем новые коды
operators["O!"] = {"|0700|", "|0509|", "|0502|", "|0999|"}
operators["Megacom"] = {"|0555|", "|0550|", "|0553|"}
operators["Beeline"] = {"|0222|", "|0770|", "|0779|"}


#  Вывод
for op, nums in operators.items():
    print(op, *nums)