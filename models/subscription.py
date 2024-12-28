from sqlalchemy import Column, Integer, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
import enum

from models.base import Base


class SubscriptionType(enum.Enum):
    ONE_MONTH = 1
    THREE_MONTHS = 3
    SIX_MONTHS = 6
    TWELVE_MONTHS = 12
    LIFETIME = "Lifetime"


class SubscriptionStatus(enum.Enum):
    ACTIVE = "active"
    EXPIRED = "expired"
    CANCELLED = "cancelled"


class Subscription(Base):
    __tablename__ = 'subscriptions'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    type = Column(Enum(SubscriptionType), nullable=False)
    status = Column(Enum(SubscriptionStatus),
                    default=SubscriptionStatus.ACTIVE, nullable=False)

    user = relationship("User", back_populates="subscriptions")

    def __repr__(self):
        return (f"<Subscription(id={self.id}, user_id={self.user_id}, "
                f"start_date={self.start_date}, end_date={self.end_date}, "
                f"type={self.type}, status={self.status})>")
