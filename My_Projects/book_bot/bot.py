import asyncio
import logging
from aiogram import Bot, Dispatcher
from My_Projects.book_bot.config_data.config import Config, load_config
from My_Projects.book_bot.handlers import user_handlers, other_handlers
from My_Projects.book_bot.keyboards.main_menu import set_main_menu


# Инициализируем логгер
logger = logging.getLogger(__name__)


# Ф-ция конфигурирования и запуска бота
async def main():
    logging.basicConfig(
        level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль инф-цию о начале запуска бота
    logger.info('Starting Bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # Настраиваем главное меню бота
    await set_main_menu(bot)

    # Регистрируем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    #Пропускаем накопившиеся апдейты и запускаем бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())