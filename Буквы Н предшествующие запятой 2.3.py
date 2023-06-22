s = "Данное предложение"

count = 0

for letter in s:
    if letter == "н":
        count += 1
    elif letter == ",":
        break

print("Количество букв 'н', предшествующих первой запятой: ", count)