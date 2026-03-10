from app.core.security import get_password_hash, create_access_token

# Mock User DB
users_db = {}

class UserSignup(BaseModel):
    username: str
    password: str

@app.post("/auth/register")
async def register(user: UserSignup):
    if user.username in users_db:
        return {"error": "User already exists"}
    
    hashed_pw = get_password_hash(user.password)
    users_db[user.username] = {"username": user.username, "password": hashed_pw}
    
    token = create_access_token({"sub": user.username})
    return {"message": "User created", "access_token": token, "token_type": "bearer"}