from datetime import datetime, timezone

from sqlalchemy import String
from sqlmodel import Field, SQLModel


class Notes(SQLModel, table=True):
    __tablename__: str = "notes"  # type: ignore

    id: int = Field(default=None, primary_key=True)
    title: str = Field(default=None, sa_type=String)
    description: str | None = Field(default=None, sa_type=String)
    importance: str | None = Field(default=None, sa_type=String)
    create_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime | None = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
