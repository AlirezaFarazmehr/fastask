from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

# Project files
from database import SessionLocal
import crud, models

# Build a FastAPI application
app = FastAPI()

# Link the static folder to display index.html
app.mount("/static", StaticFiles(directory="static"), name="static")

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Display HTML GUI in the root of the site
@app.get("/", response_class=FileResponse)
def serve_frontend():
    return "static/index.html"

# Get a list of all tasks
@app.get("/tasks", response_model=list[models.Task])
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

# ایجاد تسک جدید
@app.post("/tasks", response_model=models.Task)
def create_task(task: models.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

# Create a new task
@app.put("/tasks/{task_id}", response_model=models.Task)
def toggle_done(task_id: int, db: Session = Depends(get_db)):
    task = crud.toggle_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Delete task with specific ID
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    if not crud.delete_task(db, task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Deleted"}
