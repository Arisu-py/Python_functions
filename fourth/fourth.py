def factorials(n: int) -> int:
    """
    Подсчитывает факториалы чисел от 1 до n

    :param n: до какого числа нужно подсчитать факториалы
    :returns: факториал для числа
    """
    cur_fact = 1
    for i in range(1, n + 1):
        cur_fact *= i
        yield cur_fact


user_number = int(input('Введите число: '))

res = factorials(user_number)

for el in res:
    print(el)
