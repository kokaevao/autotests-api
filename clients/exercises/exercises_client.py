from typing import TypedDict
from clients.api_client import ApiClient
from httpx import Response

from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class Exercise(TypedDict):
    """
    Описание структуры упражнений.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExerciseQueryDict(TypedDict):
    """
    Описание структуры запроса на получение упражени.
    """
    courseId: str


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение упражени.
    """
    exercise_id: str




class CrateExerciseRequestType(TypedDict):
    """
    Описание структуры запроса на создание упражений.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа получения упражнений.
    """
    exercises: Exercise

class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа получения упражнений.
    """
    exercises: Exercise


class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа создания упражнений.
    """
    exercise: Exercise

class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа обновления упражнений.
    """
    exercise: Exercise

class UpdateExerciseRequestType(TypedDict):
    """
    Описание структуры запроса на обновление упражнения.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(ApiClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExerciseQueryDict) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: GetExercisesQueryDict) -> Response:
        """
        Метод получения упражения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CrateExerciseRequestType) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с title, maxScore, minScore, description, orderIndex,
        courseId, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: GetExercisesQueryDict, request: UpdateExerciseRequestType) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, description, orderIndex,
         estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: GetExercisesQueryDict) -> GetExerciseResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()


    def get_exercises(self, query: GetExerciseQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise(self, request: CrateExerciseRequestType) -> CreateExerciseResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: GetExercisesQueryDict, request: UpdateExerciseRequestType) -> UpdateExerciseResponseDict:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_exercise_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))

