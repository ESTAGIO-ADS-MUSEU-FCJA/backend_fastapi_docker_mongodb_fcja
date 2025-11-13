from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import notas, usuario, authenticate, nota_not_auth

app = FastAPI(
    title="Projeto de estágio FCJA", #mudar titulo
    description="Projeto FastAPI para a criação de rotas com link linkados a um QrCode e usando MongoDB Atlas com data-base",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuario.router)
app.include_router(authenticate.router)
app.include_router(notas.router)
app.include_router(nota_not_auth.router)

