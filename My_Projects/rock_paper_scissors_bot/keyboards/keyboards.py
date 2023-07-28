from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from My_Projects.rock_paper_scissors_bot.lexicon.lexicon import LEXICON

# ---Создаём клавиатуру через builder---
button_yes: KeyboardButton = KeyboardButton(text=LEXICON['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON['no_button'])
# Инициализируем билдер для клваиатуры с кнопками "Давай" и "Не хочу"
yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
yes_no_kb_builder.row(button_yes, button_no, width=2)
yes_no_kb = yes_no_kb_builder.as_markup(one_time_keyboard=True,
                                        resize_keyboard=True)
# ---Создаём игровую клавиатуру без builder---
button_1: KeyboardButton = KeyboardButton(text=LEXICON['rock'])
button_2: KeyboardButton = KeyboardButton(text=LEXICON['scissors'])
button_3: KeyboardButton = KeyboardButton(text=LEXICON['paper'])
game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_1],
                                                             [button_2],
                                                             [button_3]],
                                                   resize_keyboard=True)