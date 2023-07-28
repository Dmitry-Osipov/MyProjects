from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from My_Projects.modular_echo_bot.lexicon.lexicon import LEXICON


# Инициализируем роутер уровня модуля
router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'])


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['/help'])