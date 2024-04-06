from connections import Base
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, func, Boolean, JSON


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    first_name = Column(String(255), nullable=False, default="")
    last_name = Column(String(255), nullable=False, default="")
    email = Column(String(255), nullable=False, unique=True, index=True)
    password = Column(String(255), nullable=False)
    user_metadata = Column(JSON, default=lambda: {})
    is_email_verified = Column(Boolean, default=False)
    is_phone_verified = Column(Boolean, default=False)
    is_disabled = Column(Boolean, nullable=False, default=False)
    last_signed_in = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), onupdate=func.now())
