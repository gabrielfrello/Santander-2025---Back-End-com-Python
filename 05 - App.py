# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
import pytest
from httpx import AsyncClient

# ---------- Configuração MongoDB ----------
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "tdd_fastapi_db"
COLLECTION = "usuarios"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# ---------- Modelos ----------
class Usuario(BaseModel):
    nome: str
    idade: int

# ---------- Instância FastAPI ----------
app = FastAPI(title="API FastAPI com TDD e MongoDB")

# ---------- Funções CRUD ----------
def criar_usuario(usuario: dict):
    return db[COLLECTION].insert_one(usuario).inserted_id

def listar_usuarios():
    return list(db[COLLECTION].find({}, {"_id": 0}))

def buscar_usuario(nome: str):
    return db[COLLECTION].find_one({"nome": nome}, {"_id": 0})

# ---------- Rotas ----------
@app.post("/usuarios/")
def criar(usuario: Usuario):
    if buscar_usuario(usuario.nome):
        raise HTTPException(status_code=400, detail="Usuário já existe")
    criar_usuario(usuario.dict())
    return {"msg": "Usuário criado"}

@app.get("/usuarios/")
def listar():
    return listar_usuarios()

@app.get("/usuarios/{nome}")
def buscar(nome: str):
    usuario = buscar_usuario(nome)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

# ---------- Testes Pytest ----------
@pytest.mark.asyncio
async def test_criar_listar_usuario():
    db[COLLECTION].delete_many({})  # limpa coleção antes do teste

    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Teste criação
        response = await ac.post("/usuarios/", json={"nome": "Joao", "idade": 25})
        assert response.status_code == 200
        assert response.json() == {"msg": "Usuário criado"}

        # Teste listagem
        response = await ac.get("/usuarios/")
        assert response.status_code == 200
        assert response.json() == [{"nome": "Joao", "idade": 25}]

        # Teste busca
        response = await ac.get("/usuarios/Joao")
        assert response.status_code == 200
        assert response.json() == {"nome": "Joao", "idade": 25}

        # Teste usuário não encontrado
        response = await ac.get("/usuarios/Maria")
        assert response.status_code == 404
        assert response.json() == {"detail": "Usuário não encontrado"}

# ---------- Execução ----------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
