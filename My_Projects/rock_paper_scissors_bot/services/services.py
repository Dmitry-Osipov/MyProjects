import random
from My_Projects.rock_paper_scissors_bot.lexicon.lexicon import LEXICON


def get_bot_choice() -> str:
    return random.choice(['rock', 'scissors', 'paper'])


# Ф-ция, взвращающая ключ из словаря, по которому хранится значение,
# передаваемое как аргумент - выбор пользователя
def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON:
        if LEXICON[key] == user_answer:
            return key
    raise Exception


# Ф-ция определяющая победителя
def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules: dict[str, str] = {'rock': 'scissors',
                             'scissors': 'paper',
                             'paper': 'rock'}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    else:
        return 'bot_won'