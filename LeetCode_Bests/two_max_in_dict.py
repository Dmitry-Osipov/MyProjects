from typing import Union

# Задача: в словаре вернуть 2 ключа, значения которых являются самыми большими.


def find_two_max_value(user_dict: dict) -> Union[list, str]:
    if len(user_dict) <= 1:
        for key in user_dict.keys():
            return f'В словаре лишь один ключ: {key}'

    first, second = None, None

    for key, value in user_dict.items():
        if first is None or some_letters[first] < value:
            second = first
            first = key
        elif second is None or user_dict[second] < value:
            second = key

    return [first, second]


some_letters = {
    'a': 12,
    'b': 37,
    'c': 22,
    'd': 9000,
}

print(find_two_max_value(some_letters))
