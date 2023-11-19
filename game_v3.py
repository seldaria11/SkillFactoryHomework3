import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    start = 0 # начало массива 
    end = 101 # конец массива
    count = 1 # счетчик попыток угадываний
    while True:
        predict = (start + end) // 2 # вычисляем середину массива (предполагаемое число)
        if number == predict: # если угадали - прерываем
            break
        count += 1 # если не угадали увеличиваем число попыток на один
        if number > predict: # если искомое число больше предполагаемого
            start = predict # то предполагаемое число становится началом отрезка угадывания
        elif number < predict: # если искомое число меньше предполагаемого
            end = predict # то предполагаемое число становится концом отрезка угадывания 
    # Ваш код заканчивается здесь
    return count

def score_game(game_core_v3) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

if __name__ == "__main__":
    score_game(game_core_v3)


