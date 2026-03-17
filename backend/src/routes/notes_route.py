from fastapi import APIRouter

from src.deps.session import SessionDep
from src.dtos.notes_dto import InsertNote, ListReadNote, ReadNote, UpdateNote
from src.services.notes_service import NotesService

router = APIRouter(prefix="/notes", tags=["Notes"])


@router.post("/", response_model=ReadNote)
async def create_notes(session: SessionDep, data: InsertNote):
    service = NotesService(session)
    new_note = await service.create_note(data)
    return new_note


@router.get("/", response_model=ReadNote | ListReadNote)
async def get_notes(session: SessionDep, search: str | None = None):
    service = NotesService(session)
    note = (
        await service.get_notes() if search is None else await service.get_notes(search)
    )
    return note


@router.get("/{note_id}", response_model=ReadNote)
async def get_note_by_id(session: SessionDep, note_id: int):
    service = NotesService(session)
    note = await service.get_note_by_id(note_id)
    return note


@router.put("/{note_id}", response_model=ReadNote)
async def update_note(session: SessionDep, note_id: int, data: UpdateNote):
    service = NotesService(session)
    note = await service.update_note(note_id, data)
    return note


@router.delete("/{note_id}", response_model=ReadNote)
async def delete_note(session: SessionDep, note_id: int):
    service = NotesService(session)
    note = await service.delete_note(note_id)
    return note
