from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4


class Task(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
    completed: bool = False
