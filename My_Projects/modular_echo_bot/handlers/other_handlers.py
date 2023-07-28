from aiogram import Router
from aiogram.types import Message
from My_Projects.modular_echo_bot.lexicon.lexicon import LEXICON


# Инициализируем роутер уровня модуля
router: Router = Router()


@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON['no_echo'])