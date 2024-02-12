from fastapi import FastAPI
import uvicorn
from user.infrastructure.routes.Routes import router, initialize_routes
from user.infrastructure.Factory.Repository import RepositorioFactory


repositorio_factory = RepositorioFactory()

# repositorio = repositorio_factory.get_repositorio("mysql") 
repositorio = repositorio_factory.get_repositorio("sqlite")  

initialize_routes(repositorio)

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)