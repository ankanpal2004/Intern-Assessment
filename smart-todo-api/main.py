from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI(title="Smart ToDo API")

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

tasks: List[Task] = []

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updated_task
            return updated_task
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    return {"error": "Task not found"}
