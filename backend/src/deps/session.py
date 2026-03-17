from pathlib import Path
from typing import Annotated, AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker

BASE_PATH = Path(__file__).resolve().parent.parent.parent
LOCAL_DB_PATH = BASE_PATH / "local.db"

SQLITE_URL = "sqlite+aiosqlite:///local.db"

engine = create_async_engine(url=SQLITE_URL)

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]
