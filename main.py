from fastapi import FastAPI
from model.task_connection import TaskConnection
from schema.task_schema import TaskSchema

app = FastAPI()
conn = TaskConnection()

@app.get("/")
def root():
    return {"message": "FastAPI is running!"}

@app.post("/api/insert")
def insert(task_data: TaskSchema):
    conn.write(task_data.dict())
    return {"message": "Task inserted successfully!"}
