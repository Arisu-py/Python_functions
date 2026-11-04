def fibonacci(n: int) -> int:
    """
    Возвращает запрошенный элемент ряда Фибоначчи

    :param n: номер запрошенного элемента
    :return: число Фибоначчи на каждом шаге
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


user_number = int(input('Введите число: '))

res = fibonacci(user_number)

print(res)
