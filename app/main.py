from fastapi import FastAPI

from .routes import notas, usuario, authenticate

app = FastAPI(
    title="Projeto de estágio FCJA", #mudar titulo
    description="Projeto FastAPI para a criação de rotas com link linkados a um QrCode e usando MongoDB Atlas com data-base",
)


app.include_router(usuario.router)
app.include_router(authenticate.router)
app.include_router(notas.router)

