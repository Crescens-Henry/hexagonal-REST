from fastapi import APIRouter
from user.infrastructure.controllers.CreateUserController import crear_usuario_router, initialize_endpoints as initialize_crear_usuario
from user.infrastructure.controllers.VerificarUserController import verificar_usuario_router, initialize_endpoints as initialize_verificar_usuario
from user.infrastructure.controllers.listUsersController import get_list_user_router, initialize_endpoints as intialize_getList_Users
from user.infrastructure.controllers.LoginController import login_router, initialize_endpoints as initialize_login
from user.infrastructure.controllers.UserByIdController import get_user_by_id_router, initialize_endpoints as initialize_get_user_by_id
from user.infrastructure.controllers.PutUserController import update_user_router, initialize_endpoints as initialize_update_user
from user.infrastructure.controllers.DeleteUserController import delete_user_router, initialize_endpoints as initialize_delete_user


router = APIRouter()

def initialize_routes(repositorio):
    initialize_crear_usuario(repositorio)
    initialize_verificar_usuario(repositorio)
    intialize_getList_Users(repositorio)
    initialize_login(repositorio)
    initialize_get_user_by_id(repositorio)
    initialize_update_user(repositorio)
    initialize_delete_user(repositorio)
    router.include_router(crear_usuario_router, prefix="/api/users", tags=["usuarios"])
    router.include_router(verificar_usuario_router, prefix="/verificar/{uuid}", tags=["usuarios"])
    router.include_router(get_list_user_router, prefix="/api/users",tags=["usuarios"])
    router.include_router(login_router, prefix="/api/login", tags=["usuarios"])
    router.include_router(get_user_by_id_router, prefix="/api/users/{user_id}", tags=["usuarios"])
    router.include_router(update_user_router, prefix="/api/users/{user_id}", tags=["usuarios"])
    router.include_router(delete_user_router, prefix="/api/users/{user_id}", tags=["usuarios"])