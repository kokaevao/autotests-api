from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field()

user_data = {
    "id": 1,
    "name": "Alex",
    "email": "alex@example.com",
    "isActive": True,
}
user = User(**user_data)
print(user.model_dump())