from sqlalchemy import Column, Integer, String, Enum
from models import Base, SubscriptionType


class SubscriptionPlan(Base):
    __tablename__ = 'subscription_plans'

    id = Column(Integer, primary_key=True)
    label = Column(String, nullable=False)
    description = Column(String, nullable=False)
    type = Column(Enum(SubscriptionType), nullable=False)
    price = Column(Integer, nullable=False)

    def __repr__(self):
        return (f"<SubscriptionPlan(id={self.id}, label='{self.label}', "
                f"type='{self.type.name}', price={self.price})>")
