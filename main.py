import asyncio

from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers.commands import router as command_router
from handlers.content import router as content_router

dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=TOKEN, parse_mode="HTML")
    dp.include_router(command_router)
    dp.include_router(content_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
