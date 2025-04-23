from pydantic import BaseModel

# Model received from the user to create a new task
class TaskCreate(BaseModel):
    title: str

# Display model to respond to the user
class Task(BaseModel):
    id: int
    title: str
    done: bool

    # Necessary settings to convert ORM (SQLAlchemy) to Python model
    class Config:
        orm_mode = True
