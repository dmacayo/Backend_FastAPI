from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={404: {"message": "No encontrado"}})

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

@router.get("/usersjson")
async def usersjson():
    return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35},
            {"name": "David", "surname": "Macayo", "url": "https://david.com", "age": 30},
            {"name": "Blanca", "surname": "Chacon", "url": "https://blanca.com", "age": 29},
            ]
    
@router.get("/")
async def users():
    return users_list

# Path
@router.get("/{id}")
async def user(id: int):
    return search_user(id)

# Query
@router.get("/user/")
async def user(id: int):
    return search_user(id)

# POST
@router.post("/user/",response_model=User, status_code = 201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail="El usuarion ya existe")
    else:
        users_list.append(user)
        return user
         
# PUT
@router.put("/user/")
async def user(user: User):
    
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    
    if not found:
        return {"error": "No se ha actualizado usuario"}
    else: return user
    
# DELETE
@router.delete("/user/{id}")
async def user(id: int):
    
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index] 
            found = True
    
    if not found:
        return {"error": "No se ha eliminado el usuario"}   
        
    
def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado usuario"}
    
