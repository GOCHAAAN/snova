word = "абракадабра"

unique_letters = ""

for letter in word:
    if letter not in unique_letters:
        unique_letters += letter

print(unique_letters)