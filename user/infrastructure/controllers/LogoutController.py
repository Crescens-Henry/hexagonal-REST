from fastapi import APIRouter, Depends
from user.infrastructure.middleware.auth import oauth2_scheme
from user.domain.Models.Logout import invalid_tokens

logout_router = APIRouter()

def initialize_endpoints(repositorio): 
    @logout_router.post("/")
    async def logout(token: str = Depends(oauth2_scheme)):
        invalid_tokens.add(token)
        return {"message": "Logged out"}