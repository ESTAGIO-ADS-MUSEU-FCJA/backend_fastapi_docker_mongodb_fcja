# sistema-fastapi
cria sua venv
ative a venv

crie seu arquivo .env
    adicine as seguinte enviroments : /n
        MONGO_URL = "sua string de conexão com o mongoDB atlas "
        MONGO_ENVIROMENT = "nome do data base"
        SECRET_KEY_JWT = "sercret_key_jwt que deve gerada a partir do aquivo gerar_secret_key.py"

usar o comando docker-compose up --build

rodar o debug do vccode

e entrar no localhost:80/docs para obeter a documentação da api
