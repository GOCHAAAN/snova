A = [-2, 5, 3, -4, 1, 7, -8, 6, -9, 2]
product = 1

for element in A:
    if element < 0:
        product *= element

print("Произведение отрицательных элементов в списке: ", product) 