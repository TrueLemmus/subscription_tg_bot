from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False)
    full_name = Column(String, nullable=False)

    subscriptions = relationship("Subscription", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, full_name='{self.full_name}')>"
