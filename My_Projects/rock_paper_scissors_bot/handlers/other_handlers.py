from aiogram import Router
from aiogram.types import Message
from My_Projects.rock_paper_scissors_bot.lexicon.lexicon import LEXICON


router: Router = Router()
@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON['other_answer'])