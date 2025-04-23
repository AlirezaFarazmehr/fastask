from sqlalchemy.orm import Session
from database import TaskModel
from models import TaskCreate

# Get all tasks
def get_tasks(db: Session):
    return db.query(TaskModel).all()

# Create a new task
def create_task(db: Session, task: TaskCreate):
    db_task = TaskModel(title=task.title)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Change status (done or not)
def toggle_task(db: Session, task_id: int):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task:
        task.done = not task.done
        db.commit()
        return task
    return None

# Remove the task
def delete_task(db: Session, task_id: int):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return True
    return False
