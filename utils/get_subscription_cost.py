from typing import Dict
from config import config


def get_subscription_cost() -> Dict[str, float]:
    # 1 3 6 12 LifeTime
    cost = {}
    cost['one_month'] = float(config.MONTHLY_COST)
    cost['three_months'] = round(config.MONTHLY_COST * 3 * 0.84, 0)
    cost['six_months'] = round(config.MONTHLY_COST * 6 * 0.67, 0)
    cost['twelve_months'] = round(config.MONTHLY_COST * 12 * 0.50, 0)
    cost['life_time'] = float(config.MONTHLY_COST * 12)
    return cost
