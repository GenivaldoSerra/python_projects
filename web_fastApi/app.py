from fastapi import FastAPI


funcionarios = [
    {'id': 1, 'nome': 'Joao', 'sobrenome': 'Silva'},
    {'id': 2, 'nome': 'Maria', 'sobrenome': 'Santos'},
    {'id': 3, 'nome': 'Jose', 'sobrenome': 'Souza'},
]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/funcionarios")
async def get_funcionarios():
    return {'funcionarios': funcionarios}
