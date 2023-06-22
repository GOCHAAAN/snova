B = [1.5, -2.3, 4.2, 7.8, -3.5, 6.1, -1.7, -5.2, 2.8, 9.6]
min_index = B.index(min(B))
sum_between_negatives = 0

for i in range(len(B)):
    if B[i] < 0:
        if sum_between_negatives == 0:
            first_negative_index = i
        else:
            second_negative_index = i
            break

for i in range(first_negative_index + 1, second_negative_index):
    sum_between_negatives += B[i]

print("Номер минимального элемента списка: ", min_index)
print("Сумма элементов между первым и вторым отрицательными элементами: ", sum_between_negatives)