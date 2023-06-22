t = (1, 3, 5, 6, 8, 4, 2, 7, 9, 10, 12, 14, 16, 18)
last_even_pair_idx = 0
for i in range(len(t) - 1):
    if t[i] % 2 == 0 and t[i + 1] % 2 == 0:
        last_even_pair_idx = i + 1
for i in range(last_even_pair_idx):
    print(t[i])