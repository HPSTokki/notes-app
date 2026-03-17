from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import col, select

from src.dtos.notes_dto import InsertNote, ListReadNote, ReadNote, UpdateNote
from src.excepton import NoteNotFound
from src.models.notes_model import Notes


class NotesService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_note(self, data: InsertNote) -> ReadNote:
        note = Notes(**data.model_dump())
        self.session.add(note)
        await self.session.commit()
        await self.session.refresh(note)
        return ReadNote.model_validate(note, from_attributes=True)

    async def get_notes(self, search: str | None = None) -> ReadNote | ListReadNote:
        query = select(Notes)
        if search:
            query = query.where(col(Notes.title).ilike(f"%{search}%"))
        result = await self.session.execute(query)
        notes = result.scalars().all()

        if len(notes) == 1:
            return ReadNote.model_validate(notes[0], from_attributes=True)

        return ListReadNote(
            notes=[
                ReadNote.model_validate(note, from_attributes=True) for note in notes
            ]
        )

    async def get_note_by_id(self, id: int) -> ReadNote:
        note = await self.session.get(Notes, id)
        if note is None:
            raise NoteNotFound()
        return ReadNote.model_validate(note, from_attributes=True)

    async def delete_note(self, id: int) -> ReadNote:
        note = await self.session.get(Notes, id)
        if note is None:
            raise NoteNotFound()
        await self.session.delete(note)
        await self.session.commit()
        return ReadNote.model_validate(note, from_attributes=True)

    async def update_note(self, id: int, data: UpdateNote) -> ReadNote:
        note = await self.session.get(Notes, id)
        if note is None:
            raise NoteNotFound()
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(note, key, value)
        await self.session.commit()
        await self.session.refresh(note)
        return ReadNote.model_validate(note, from_attributes=True)
