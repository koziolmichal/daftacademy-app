from fastapi import FastAPI
from starlette.requests import Request
from pydantic import BaseModel
import json

app = FastAPI()
app.counter = 0

class HelloResp(BaseModel):
    msg: str

@app.get("/")
def root():
    return {"message": "Hello world!"}

@app.get("/method")
def method(request: Request):
    # closest try, need just space {"method": f"{request.method}"}
    return {"method": f"{request.method}"}

@app.get("/hello/{name}")
def hello_name_view(name: str):
    return f"Hello {name}"

@app.get("/counter")
def counter():
    app.counter += 1
    return app.counter