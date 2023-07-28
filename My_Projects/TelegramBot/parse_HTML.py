from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from My_Projects.secrets import bot_token

API_TOKEN: str = bot_token
bot: Bot = Bot(token=bot_token, parse_mode='HTML')
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Привет!\n\nЯ бот, демонстрирующий '
             'как работает HTML-разметка. Отправь команду '
             'из списка ниже:\n\n'
             '/bold - жирный текст\n'
             '/italic - наклонный текст\n'
             '/underline - подчеркнутый текст\n'
             '/strike - зачеркнутый текст\n'
             '/spoiler - спойлер\n'
             '/link - внешняя ссылка\n'
             '/tglink - внутренняя ссылка\n'
             '/code - моноширинный текст\n'
             '/pre - предварительно форматированный текст\n'
             '/precode - предварительно форматированный блок кода\n'
             '/precodediff - разница между &lt;code&gt; и &lt;pre&gt;\n'
             '/boldi - жирный наклонный текст\n'
             '/iu - наклонный подчеркнутый текст\n'
             '/biu - жирный наклонный подчеркнутый текст')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        text='Я бот, демонстрирующий '
             'как работает HTML-разметка. Отправь команду '
             'из списка ниже:\n\n'
             '/bold - жирный текст\n'
             '/italic - наклонный текст\n'
             '/underline - подчеркнутый текст\n'
             '/strike - зачеркнутый текст\n'
             '/spoiler - спойлер\n'
             '/link - внешняя ссылка\n'
             '/tglink - внутренняя ссылка\n'
             '/code - моноширинный текст\n'
             '/pre - предварительно форматированный текст\n'
             '/precode - предварительно форматированный блок кода\n'
             '/precodediff - разница между &lt;code&gt; и &lt;pre&gt;\n'
             '/boldi - жирный наклонный текст\n'
             '/iu - наклонный подчеркнутый текст\n'
             '/biu - жирный наклонный подчеркнутый текст')


# Этот хэндлер будет срабатывать на команду "/bold"
@dp.message(Command(commands='bold'))
async def process_bold_command(message: Message):
    await message.answer(
        text='&lt;side_b&gt;Это жирный текст&lt;/side_b&gt;:\n'
             '<side_b>Это жирный текст</side_b>\n\n'
             '&lt;strong&gt;И это тоже жирный текст&lt;/strong&gt;:\n'
             '<strong>И это тоже жирный текст</strong>')


# Этот хэндлер будет срабатывать на команду "/italic"
@dp.message(Command(commands='italic'))
async def process_italic_command(message: Message):
    await message.answer(
        text='&lt;i&gt;Это наклонный текст&lt;/i&gt;:\n'
             '<i>Это наклонный текст</i>\n\n'
             '&lt;em&gt;И это тоже наклонный текст&lt;/em&gt;:\n'
             '<em>И это тоже наклонный текст</em>')


# Этот хэндлер будет срабатывать на команду "/underline"
@dp.message(Command(commands='underline'))
async def process_underline_command(message: Message):
    await message.answer(
        text='&lt;u&gt;Это подчеркнутый текст&lt;/u&gt;:\n'
             '<u>Это подчеркнутый текст</u>\n\n'
             '&lt;ins&gt;И это тоже подчеркнутый текст&lt;/ins&gt;:\n'
             '<ins>И это тоже подчеркнутый текст</ins>')


# Этот хэндлер будет срабатывать на команду "/strike"
@dp.message(Command(commands='strike'))
async def process_strike_command(message: Message):
    await message.answer(
        text='&lt;s&gt;Это зачеркнутый текст&lt;/s&gt;:\n'
             '<s>Это зачеркнутый текст</s>\n\n'
             '&lt;strike&gt;И это зачеркнутый текст&lt;/strike&gt;:\n'
             '<strike>И это зачеркнутый текст</strike>\n\n'
             '&lt;del&gt;И это тоже зачеркнутый текст&lt;/del&gt;:\n'
             '<del>И это тоже зачеркнутый текст</del>')


# Этот хэндлер будет срабатывать на команду "/spoiler"
@dp.message(Command(commands='spoiler'))
async def process_spoiler_command(message: Message):
    await message.answer(
        text='&lt;span class="tg-spoiler"&gt;Это текст '
             'под спойлером&lt;/span&gt;:\n'
             '<span class="tg-spoiler">Это текст под '
             'спойлером</span>\n\n'
             '&lt;tg-spoiler&gt;И это текст под '
             'спойлером&lt;/tg-spoiler&gt;:\n'
             '<tg-spoiler>И это текст под спойлером</tg-spoiler>')


# Этот хэндлер будет срабатывать на команду "/link"
@dp.message(Command(commands='link'))
async def process_link_command(message: Message):
    await message.answer(
        text='&lt;side_a href="https://stepik.org/120924"&gt;Внешняя '
             'ссылка&lt;/side_a&gt;:\n'
             '<side_a href="https://stepik.org/120924">Внешняя ссылка</side_a>')


# Этот хэндлер будет срабатывать на команду "/tglink"
@dp.message(Command(commands='tglink'))
async def process_tglink_command(message: Message):
    await message.answer(
        text='&lt;side_a href="tg://user?id=515851662"&gt;Внутренняя '
             'ссылка&lt;/side_a&gt;:\n'
             '<side_a href="tg://user?id=515851662">Внутренняя ссылка</side_a>')


# Этот хэндлер будет срабатывать на команду "/code"
@dp.message(Command(commands='code'))
async def process_code_command(message: Message):
    await message.answer(
        text='&lt;code&gt;Это моноширинный текст&lt;/code&gt;:\n'
             '<code>Это моноширинный текст</code>')


# Этот хэндлер будет срабатывать на команду "/pre"
@dp.message(Command(commands='pre'))
async def process_pre_command(message: Message):
    await message.answer(
        text='&lt;pre&gt;Предварительно отформатированный '
             'текст&lt;/pre&gt;:\n'
             '<pre>Предварительно отформатированный текст</pre>')


# Этот хэндлер будет срабатывать на команду "/precode"
@dp.message(Command(commands='precode'))
async def process_precode_command(message: Message):
    await message.answer(
        text='&lt;pre&gt;&lt;code class="language-'
             'python"&gt;Предварительно отформатированный '
             'блок кода на языке Python&lt;/code&gt;&lt;/pre&gt;:\n'
             '<pre><code class="language-python">Предварительно '
             'отформатированный блок кода на языке Python</code></pre>')


# Этот хэндлер будет срабатывать на команду "/precodediff"
@dp.message(Command(commands='precodediff'))
async def process_precodediff_command(message: Message):
    await message.answer(
        text='С помощью этого текста можно лучше понять '
             'разницу между тегами &lt;code&gt; и '
             '&lt;pre&gt; - текст внутри '
             'тегов &lt;code&gt; <code>не выделяется в '
             'отдельный блок</code>, а становится '
             'частью строки, внутрь которой помещен, в то время как '
             'тег &lt;pre&gt; выделяет текст <pre>в отдельный '
             'блок,</pre> разрывая '
             'строку, внутрь которой помещен')


# Этот хэндлер будет срабатывать на команду "/boldi"
@dp.message(Command(commands='boldi'))
async def process_boldi_command(message: Message):
    await message.answer(
        text='&lt;side_b&gt;&lt;i&gt;Это жирный наклонный '
             'текст&lt;/i&gt;&lt;/side_b&gt;:\n\n'
             '<side_b><i>Это жирный наклонный текст</i></side_b>')


# Этот хэндлер будет срабатывать на команду "/iu"
@dp.message(Command(commands='iu'))
async def process_iu_command(message: Message):
    await message.answer(
        text='&lt;i&gt;&lt;u&gt;Это наклонный подчеркнутый '
             'текст&lt;/u&gt;&lt;/i&gt;:\n\n'
             '<i><u>Это наклонный подчеркнутый текст</u></i>')


# Этот хэндлер будет срабатывать на команду "/biu"
@dp.message(Command(commands='biu'))
async def process_biu_command(message: Message):
    await message.answer(
        text='&lt;side_b&gt;&lt;i&gt;&lt;u&gt;Это жирный '
             'наклонный подчеркнутый '
             'текст&lt;/u&gt;&lt;/i&gt;&lt;/side_b&gt;:\n\n'
             '<side_b><i><u>Это жирный наклонный подчеркнутый '
             'текст</u></i></side_b>')


# Этот хэндлер будет срабатывать на любые сообщения, кроме команд,
# отлавливаемых хэндлерами выше
async def send_echo(message: Message):
    await message.answer(
        text='Я даже представить себе не могу, '
             'что ты имеешь в виду\n\n'
             'Чтобы посмотреть список доступных команд - '
             'отправь команду /help')


if __name__ == '__main__':
    dp.run_polling(bot)
