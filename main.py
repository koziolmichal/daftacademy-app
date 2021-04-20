from fastapi import FastAPI, Response
from starlette.requests import Request
from pydantic import BaseModel
from functions import dehash

app = FastAPI()

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

@app.get("/auth")
def auth(password: str = '', password_hash: str = ''):
    hashed = dehash(password) == password_hash
    if hashed and password and password_hash:
        status_code = 204
    else:
        status_code = 401
    return Response(status_code=status_code)