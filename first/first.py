def are_parenthesis_fine(text: str, index=0, stack=[]) -> bool:
    """
    Проверяет правильность скобочной последовательности

    :param text: пользовательский текст
    :param index: текущий индекс символа из текста
    :param stack: список незакрытых скобок на данный момент
    :return: True, если скобки расставлены верно, False, если нет
    """
    matching = {')': '(', ']': '[', '}': '{'}
    opening_parenthesis = '([{'
    all_parenthesis = '()[]{}'

    if index == len(text):
        return not stack

    if text[index] not in all_parenthesis:
        return are_parenthesis_fine(text, index + 1, stack)

    if text[index] in opening_parenthesis:
        return are_parenthesis_fine(text, index + 1, stack + [text[index]])

    if stack and stack[-1] == matching[text[index]]:
        stack.pop()
        return are_parenthesis_fine(text, index + 1, stack)

    return False


user_text = input('Введите строку: ')

res = are_parenthesis_fine(user_text)

print(res)
