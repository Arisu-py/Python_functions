import re


def find_abbreviation(s: str) -> list:
    abbreviations = re.findall(r'\b[A-ZА-Я]{2,6}\b', user_string)
    return abbreviations


user_string = input('Введите строку: ')

res = find_abbreviation(user_string)

print(res)
