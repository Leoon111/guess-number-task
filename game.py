"""Игра угадай число"""

import numpy as np

for n in range(100):
    number = np.random.randint(1, 101) # загадываем число

    # количество попыток
    count = 0
    min_numb = -1
    max_numb = 101
    nums = list()

    while number not in nums:
        nums = list() 
        select = (max_numb-min_numb)//2 # можно на 4 делить, но медленне получается.
        plus_numb = select if select > 1 else 1
        nums.append(min_numb + plus_numb)
        # код для метода деления промежутка на 4 меняется двумя строчками выше
        # nums.append(min_numb + plus_numb*2)
        # nums.append(min_numb + plus_numb*3)

        for num in nums:
            # print(num, number)
            count+=1
            if num > number:
                max_numb = num
                break
            if num < number:
                min_numb = num
            if num == number:
                print(f"Число угадано за {count} попыток, число было {number}")
                break

