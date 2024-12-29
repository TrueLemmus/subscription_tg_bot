import asyncio
from db import AsyncSessionLocal, init_models
from crud import (
    create_user,
    create_subscription,
    get_subscriptions_by_user,
    update_subscription_status,
    delete_subscription,
    renew_subscription
)
from models import SubscriptionType, SubscriptionStatus


async def main():
    # Инициализация моделей и создание таблиц
    # await init_models()

    # Создание новой сессии
    async with AsyncSessionLocal() as session:
        await renew_subscription(session, 3, SubscriptionType.LIFETIME)

    #     # Создание нового пользователя
    #     user = await create_user(session, "Иван Иванов")
    #     print(f"Добавлен пользователь: {user}")

    #     # Создание новой подписки для пользователя
    #     subscription = await create_subscription(
    #         session,
    #         user_id=user.id,
    #         type=SubscriptionType.THREE_MONTHS
    #     )
    #     print(f"Добавлена подписка: {subscription}")

    #     # Получение всех подписок пользователя
    #     subscriptions = await get_subscriptions_by_user(session, user.id)
    #     print(f"Подписки пользователя {user.id}: {subscriptions}")

    #     # Обновление статуса подписки
    #     updated_subscription = await update_subscription_status(
    #         session,
    #         subscription_id=subscription.id,
    #         new_status=SubscriptionStatus.EXPIRED
    #     )
    #     print(f"Обновленная подписка: {updated_subscription}")

        # Удаление подписки
        # await delete_subscription(session, subscription.id)
        # print(f"Подписка с id {subscription.id} удалена.")

if __name__ == "__main__":
    asyncio.run(main())
