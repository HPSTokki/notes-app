from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.excepton import DomainException
from src.routes import notes_route

app = FastAPI()

origins = ["http://localhost:8000", "http://localhost"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_headers="[*]",
    allow_methods="[*]",
    allow_credentials=True,
)


@app.exception_handler(DomainException)
async def exception_handler(request: Request, exc: DomainException) -> JSONResponse:
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


app.include_router(notes_route.router)


@app.get("/")
async def health_check() -> dict[str, bool]:
    return {"ok": True}
