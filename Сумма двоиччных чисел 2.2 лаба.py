for i in range(10, 100): 
    digits_sum = sum(int(d) for d in str(i)) 
    if i % digits_sum == 0: 
        print(i)