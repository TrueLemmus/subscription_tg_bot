from loader import bot
from config import config


async def remove_user_from_channel(user_id) -> None:
    try:
        await bot.ban_chat_member(chat_id=config.PRIVATE_CHANNEL_ID, user_id=user_id)
        print(f"Пользователь с ID {user_id} успешно удалён из канала {config.PRIVATE_CHANNEL_ID}.")
    except Exception as e:
        print(f"Произошла ошибка при удалении пользователя: {e}")
