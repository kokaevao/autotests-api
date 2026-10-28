from pydantic import BaseModel, Field, ConfigDict


class ExerciseSchema(BaseModel):
    """
    Описание структуры упражнений.
    """
    model_config = ConfigDict(populate_by_name=True)
    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExerciseQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение упражени.
    """
    model_config = ConfigDict(populate_by_name=True)
    course_id: str = Field(alias="courseId")


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение упражени.
    """
    exercise_id: str




class CrateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражений.
    """
    model_config = ConfigDict(populate_by_name=True)
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа получения упражнений.
    """
    exercises: ExerciseSchema

class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа получения упражнений.
    """
    exercises: ExerciseSchema


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания упражнений.
    """
    exercise: ExerciseSchema

class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления упражнений.
    """
    exercise: ExerciseSchema

class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")