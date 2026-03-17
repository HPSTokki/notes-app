from datetime import datetime

from pydantic import BaseModel


class InsertNote(BaseModel):
    title: str
    description: str | None


class ReadNote(BaseModel):
    id: int
    title: str
    description: str | None
    create_at: datetime
    updated_at: datetime


class UpdateNote(BaseModel):
    title: str | None = None
    description: str | None = None


class ListReadNote(BaseModel):
    notes: list[ReadNote]
