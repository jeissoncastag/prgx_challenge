from fastapi import FastAPI
from models import User, Address
import pickle

app = FastAPI()

db = {
    "users": [],
    "addresses": []
}

@app.post("/users/")
def create_user(user: User):
    db["users"].append(user)
    with open('usuarios.pkl', 'wb') as archivo:
        pickle.dump(db, archivo)
    return {"message": "User successfully created"}

@app.get("/users/by_country/")
def get_users_by_country(country: str):
    with open('usuarios.pkl', 'rb') as archivo:
        db = pickle.load(archivo)
    users = [user for user in db["users"] if any(addr.country == country for addr in user.addresses)]
    return users

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
