# guess the number game

import numpy as np

def game_core(number: int=1) -> int:
    """Функция угадывает число меньше, чем за 20 попыток.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Количество попыток
    """
    count = 0
    predict = np.random.randint(1,100)
    
    while predict != number:
        count += 1
        if predict < number:
            predict = int(predict*1.5)
        elif predict > number:
            predict = int(predict/2)
            
    return count
print (f'Количество попыток: {game_core()}')


def score_game(game_core) -> int:
    """Функция вычтсляет среднее количество попыток за 10000 повторений 
    алгоритма функции game_core

    Args:
        game_core (_type_): функция game_core

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(10000))
    
    for number in random_array:
        count_ls.append(game_core(number))
        
    score = int(np.mean(count_ls))
    
    return score
print(f'Ваш алгоритм угадывает число в среднем за: {score_game(game_core)} попытки')
