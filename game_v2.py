"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
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
                return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    size=10000
    random_array = np.random.randint(1, 101, size)  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} сек. за {size} попыток")
    return score

if __name__ == "__main__":
    # RUN
    score_game(random_predict)
