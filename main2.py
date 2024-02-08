# main.py
from fastapi import FastAPI
import uvicorn
from user.controllers.main import router, initialize_endpoints

from user.application.casos_de_uso import UserUseCases
from user.infrastructure.Repository import RepositorioFactory


repositorio_factory = RepositorioFactory()

repositorio = repositorio_factory.get_repositorio("mongodb") 
# repositorio = repositorio_factory.get_repositorio("mysql") 
# repositorio = repositorio_factory.get_repositorio("sqlite")  

casos_de_uso = UserUseCases(repositorio)
initialize_endpoints(casos_de_uso)

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)