from fastapi import FastAPI
from models import User, Address

app = FastAPI()

# Simula una base de datos en memoria
db = {
    "users": [],
    "addresses": []
}

@app.post("/users/")
def create_user(user: User):
    db["users"].append(user)
    return {"message": "Usuario creado con éxito"}

@app.get("/users/by_country/")
def get_users_by_country(country: str):
    users = [user for user in db["users"] if any(addr.pais == country for addr in user.direcciones)]
    return users

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
