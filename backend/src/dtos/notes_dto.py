from datetime import datetime

from pydantic import BaseModel


class InsertNote(BaseModel):
    title: str
    description: str | None
    importance: str | None


class ReadNote(BaseModel):
    id: int
    title: str
    description: str | None
    importance: str | None
    create_at: datetime
    updated_at: datetime


class UpdateNote(BaseModel):
    title: str | None = None
    description: str | None = None
    importance: str | None


class ListReadNote(BaseModel):
    notes: list[ReadNote]
