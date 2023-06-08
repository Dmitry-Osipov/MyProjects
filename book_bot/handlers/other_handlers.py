from aiogram import Router
from aiogram.types import Message


router: Router = Router()


@router.message()
async def send_echo(message: Message):
    await message.answer(f'Отвечу Вам тем же: {message.text}')
