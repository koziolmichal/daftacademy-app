from fastapi import FastAPI
from starlette.requests import Request
from pydantic import BaseModel
import json

app = FastAPI()
app.counter = 0


class PostResp(BaseModel):
    method: str

@app.get("/")
def root():
    return {"message": "Hello world!"}

@app.get("/method")
def get_method(request: Request):
    return {"method": f"{request.method}"}

@app.put("/method")
def get_method(request: Request):
    return {"method": f"{request.method}"}

@app.options("/method")
def get_method(request: Request):
    return {"method": f"{request.method}"}

@app.delete("/method")
def get_method(request: Request):
    return {"method": f"{request.method}"}

@app.post("/method", status_code=201)
def post_method(request: Request):
    return {"method": f"{request.method}"}

@app.get("/hello/{name}")
def hello_name_view(name: str):
    return f"Hello {name}"

@app.get("/counter")
def counter():
    app.counter += 1
    return app.counter