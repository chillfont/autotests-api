"""
Pydantic-модели для работы с эндпоинтом POST /api/v1/users.
"""

from pydantic import BaseModel, Field, EmailStr, constr

PasswordStr = constr(min_length=1, max_length=250)
NameStr = constr(min_length=1, max_length=50)


class UserSchema(BaseModel):
    """
    Модель данных пользователя.
    Используется для сериализации и десериализации информации о пользователе.
    """
    id: str
    email: EmailStr = Field(min_length=1, max_length=250)
    last_name: NameStr = Field(alias="lastName")
    first_name: NameStr = Field(alias="firstName")
    middle_name: NameStr = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Модель запроса на создание пользователя.
    Применяем constr для проверки длины строк и EmailStr для email.
    """
    email: EmailStr
    password: PasswordStr
    last_name: NameStr = Field(alias="lastName")
    first_name: NameStr = Field(alias="firstName")
    middle_name: NameStr = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    Модель ответа после создания пользователя.
    Содержит вложенный объект user с данными созданного пользователя.
    """
    user: UserSchema
