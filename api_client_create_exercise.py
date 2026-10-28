
from clients.courses.courses_client import get_courses_client
from clients.exercises.exercises_client import  ExercisesClient, get_exercise_client
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.fakers import get_random_email
from clients.courses.courses_schema import CreateCoursesRequestSchema
from clients.exercises.exercises_schema import CrateExerciseRequestSchema

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

# Инициализируем запрос на создание пользователя
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercise_client(authentication_user)

create_file_request = CreateFileRequestSchema(
    filename='image123.png',
    directory='courses',
    upload_file='./testdata/files/image123.png'
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

create_course_request = CreateCoursesRequestSchema(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API Course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

create_exercise_request = CrateExerciseRequestSchema(
    title="Helping a teammate",
    courseId=create_course_response.course.id,
    maxScore=101,
    minScore=15,
    orderIndex=2,
    description="Code review",
    estimatedTime="2 days",
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)

