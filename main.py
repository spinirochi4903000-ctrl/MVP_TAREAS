from fastapi import FastAPI
from model.task_connection import TaskConnection
from schema.task_schema import TaskSchema

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI is running!"}

@app.post("/api/insert")
def insert(task_data: TaskSchema):
    print(task_data)
    return {"message": "Task inserted successfully!"}
