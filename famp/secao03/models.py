from typing import Optional

from pydantic import BaseModel


class Cursor(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None