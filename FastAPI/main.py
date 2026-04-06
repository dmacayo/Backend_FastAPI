from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Fast API!"}

@app.get("/url")
async def root():
    return {"url": "Esto es un mensaje"}

# Inicia el server: fastapi dev 

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc
