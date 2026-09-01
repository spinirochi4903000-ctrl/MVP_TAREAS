from fastapi import FastAPI

app = FastAPI()

app.get("/")
def root():
    return{"menssage": "Fastapi is Runing"}

