from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int
    
users_list = [User(id=1 ,name = "Brais", surname = "Moure", url = "https://moure.dev", age = 35),
              User(id=1, name = "David", surname = "Macayo", url = "https://david.com", age = 30),
              User(id=1, name = "Blanca", surname = "Chacon", url = "https://blanca.com", age = 29),         
              ]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35},
            {"name": "David", "surname": "Macayo", "url": "https://david.com", "age": 30},
            {"name": "Blanca", "surname": "Chacon", "url": "https://blanca.com", "age": 29},
            ]
    
@app.get("/users")
async def users():
    return users_list