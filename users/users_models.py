from connections import Base
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, func, Boolean, JSON


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String(255), nullable=True, default="")
    last_name = Column(String(255), nullable=True, default="")
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    user_metadata = Column(JSON)
    is_email_verified = Column(Boolean, default=False)
    is_phone_verified = Column(Boolean, default=False)
    is_disabled = Column(Boolean, nullable=False, default=False)
    last_signed_in = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), onupdate=func.now())
