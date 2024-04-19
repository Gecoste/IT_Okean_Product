import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
load_dotenv()


bot = Bot(token=getenv("TOKEN")) #init bot
dp = Dispatcher()

def webapp_builder():
    builder = InlineKeyboardBuilder()
    builder.button(text='Начать', web_app=WebAppInfo(
        url=getenv("URL_WEB"),
    ))
    return builder.as_markup()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Для запуска CryptoHub-Web нажмите кнопку, <b>{message.from_user.full_name}</b>!", reply_markup = webapp_builder())

async def main() -> None:
    bot = Bot(token=getenv("TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())