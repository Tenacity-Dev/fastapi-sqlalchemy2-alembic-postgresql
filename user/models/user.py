from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from core.database import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    # is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    # created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    # updated_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.utcnow)
