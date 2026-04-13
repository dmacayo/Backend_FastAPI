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
              User(id=2, name = "David", surname = "Macayo", url = "https://david.com", age = 30),
              User(id=3, name = "Blanca", surname = "Chacon", url = "https://blanca.com", age = 29),         
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

# Path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# Query
@app.get("/user/")
async def user(id: int):
    return search_user(id)

    
def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado usuario"}