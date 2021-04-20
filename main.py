from fastapi import FastAPI, Response
from starlette.requests import Request
from pydantic import BaseModel
from functions import dehash
from datetime import datetime, timedelta

app = FastAPI()
app.patient = 0
app.patients = dict()

class RegisterResponse(BaseModel):
    name: str
    surname: str

class PatientResponse(BaseModel):
    id: int
    name: str
    surname: str
    register_date: str
    vaccination_date: str

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

@app.post("/register", status_code = 201, response_model=PatientResponse)
def register(request: RegisterResponse):
    app.patient += 1
    name = request.name
    surname = request.surname
    register_date = datetime.date(datetime.now())
    name_letters = 0
    surname_letters = 0
    for i in range(len(name)):
        if name[i].isalpha():
            name_letters += 1
    for i in range(len(surname)):
        if surname[i].isalpha():
            surname_letters += 1
    name_surname_letters = name_letters + surname_letters
    vaccination_date = register_date + timedelta(days=name_surname_letters)
    register_response = PatientResponse(id=app.patient, name=name, surname=surname, register_date=str(register_date), vaccination_date=str(vaccination_date))
    app.patients[app.patient] = dict(register_response)
    return register_response