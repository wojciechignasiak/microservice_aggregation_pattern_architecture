from beanie import Document, Indexed


class Task(Document):
    name: Indexed(str, unique=True)
    description: str

    class Settings:
        name = "task"