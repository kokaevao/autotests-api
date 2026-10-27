import uuid

from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    id: int = Field(gt=0)
    email: EmailStr = "user@example.com"
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    email: EmailStr = "user@example.com"
    password: str = Field(
      min_length=8, max_length=32, pattern=r"^[A-Za-z0-9@#$%^&+=!]+$"
  )
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    user: UserSchema


get_user_schema = UserSchema(
    id=2,
    lastName="Alex",
    firstName="John",
    middleName="Doe",
)

create_user_request = CreateUserRequestSchema(
    password="Tr430fdt",
    lastName="Shuba",
    firstName="Tuba",
    middleName="Yuba",
)

create_user_response = CreateUserResponseSchema(
    user=get_user_schema,
)

print(get_user_schema)
print(create_user_request)
print(create_user_response)
