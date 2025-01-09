import asyncio

from loader import bot, dp
from handlers import *
from db import init_models


async def main() -> None:
    await init_models()
    await dp.start_polling(bot, )


if __name__ == "__main__":
    asyncio.run(main())
