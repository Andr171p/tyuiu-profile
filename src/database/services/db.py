from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)
import contextlib
from typing import AsyncIterator, AsyncGenerator, Optional

from src.database.options import DB_URL


class DBSession:
    def __init__(self) -> None:
        self._engine: Optional[AsyncEngine] = None
        self._sessionmaker: Optional[async_sessionmaker[AsyncSession]] = None

    def init(self) -> None:
        self._engine = create_async_engine(
            url=DB_URL,
            echo=True
        )
        self._sessionmaker = async_sessionmaker(
            bind=self._engine,
            expire_on_commit=False
        )

    async def close(self) -> None:
        if self._engine is None:
            return
        await self._engine.dispose()
        self._engine = None
        self._sessionmaker = None

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self._sessionmaker() as session:
            try:
                yield session
            except Exception as _ex:
                await session.rollback()
                raise _ex

    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        if self._engine is None:
            raise IOError("DBSession is not initialized")
        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception as _ex:
                await connection.rollback()
                raise _ex


db = DBSession()


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with db.session() as session:
        yield session
