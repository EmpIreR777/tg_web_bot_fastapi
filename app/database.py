from sqlalchemy import func
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import (AsyncAttrs,
                                    AsyncSession,
                                    async_sessionmaker,
                                    create_async_engine)


database_url = 'sqlite+aiosqlite:///db.sqlite3'
engine = create_async_engine(url=database_url)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession)


class Base(AsyncAttrs, DeclarativeBase):
    create_at: Mapped[datetime] = mapped_column(
        server_default=func.now()
        )
    update_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        onupdate=func.now()
        )

    __abstract__ = True
