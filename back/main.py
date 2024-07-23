from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users = [
    {
        "id":1,
        "nombre":"Leonardo",
        "apellido":"Martinez",
        "DNI":3999393
    },
    {
        "id":2,
        "nombre": "Ana",
        "apellido": "García",
        "DNI": 45678901
    },
    {
        "id":3,
        "nombre": "Pedro",
        "apellido": "López",
        "DNI": 98765432
    },
    {
        "id":4,
        "nombre": "María",
        "apellido": "Fernández",
        "DNI": 12345678
    },
    {
        "id":5,
        "nombre": "Juancito",
        "apellido": "Fernández",
        "DNI": 12345633
    }
]

@app.get("/users")
def getUsers():
    return users

@app.get("/{id}")
def getUserById(id:int):
    return users[id]