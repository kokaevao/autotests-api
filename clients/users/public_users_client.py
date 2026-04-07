from clients.api_client import ApiClient
from httpx import Response
from typing import TypedDict

class CreateUserDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(ApiClient):
    """
    Клиент для работы с /api/v1/users
    """

    def create_user_api(self, request: CreateUserDict) -> Response:
        """
        Метод выполняет создание нового юзера.

        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)

