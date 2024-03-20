import asyncio
from aiogram import Bot, Dispatcher
from decouple import config
from handlers import private, group, private_news
from optional import options


async def main():
    bot = Bot(token=config('TOKEN'))
    dp = Dispatcher()
    dp.include_routers(
        private.private_router,
        group.group_router,
        private_news.news_router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=options.private_commands)
    await dp.start_polling(bot)


asyncio.run(main())
