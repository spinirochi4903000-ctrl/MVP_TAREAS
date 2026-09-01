from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model.task_connection import TaskConnection
from schema.task_schema import TaskSchema, TaskUpdateSchema

app = FastAPI()
conn = TaskConnection()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "FastAPI is running!"}


@app.post("/api/insert")
def insert(task_data: TaskSchema):
    data = task_data.model_dump(exclude={"id_tarea"}, mode="json")
    conn.write(data)
    return {"message": "Task inserted successfully!"}


@app.get("/api/tasks")
def get_tasks(date: str | None = None):
    tasks = conn.get_by_date(date) if date else conn.get_all()
    return {"tasks": tasks}


@app.get("/api/tasks/{id_tarea}")
def get_task(id_tarea: int):
    task = conn.get_by_id(id_tarea)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"task": task}


@app.put("/api/tasks/{id_tarea}")
def update_task(id_tarea: int, task_data: TaskUpdateSchema):
    existing = conn.get_by_id(id_tarea)
    if not existing:
        raise HTTPException(status_code=404, detail="Task not found")

    updated_fields = task_data.model_dump(exclude_unset=True, mode="json")
    conn.update(id_tarea, updated_fields)
    return {"message": "Task updated successfully!"}


@app.delete("/api/tasks/{id_tarea}")
def delete_task(id_tarea: int):
    existing = conn.get_by_id(id_tarea)
    if not existing:
        raise HTTPException(status_code=404, detail="Task not found")

    conn.delete(id_tarea)
    return {"message": "Task deleted successfully!"}