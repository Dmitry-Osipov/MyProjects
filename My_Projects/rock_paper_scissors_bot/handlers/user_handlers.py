from aiogram import Router
from aiogram.filters import CommandStart, Text
from aiogram.types import Message
from My_Projects.rock_paper_scissors_bot.keyboards.keyboards import game_kb, yes_no_kb
from My_Projects.rock_paper_scissors_bot.lexicon.lexicon import LEXICON
from My_Projects.rock_paper_scissors_bot.services.services import get_bot_choice, get_winner


router: Router = Router()
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'], reply_markup=yes_no_kb)


@router.message(Text(text=LEXICON['yes_button']))
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON['yes'], reply_markup=game_kb)


@router.message(Text(text=LEXICON['no_button']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON['no'])


@router.message(Text(text=[LEXICON['rock'],
                           LEXICON['scissors'],
                           LEXICON['paper']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON["bot_choice"]} '
                              f'- {LEXICON[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON[winner], reply_markup=yes_no_kb)