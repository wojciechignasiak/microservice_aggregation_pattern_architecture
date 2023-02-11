from typing import Optional
from pydantic import BaseModel, Field


class TaskModel(BaseModel):
    id: Optional[str]
    name: str = Field(...)
    description: Optional[str] = None
    


    class Config:
        schema_extra = {
            "example": {
                "id": "",
                "name": "Task name",
                "description": "This is task description",
            }
        }