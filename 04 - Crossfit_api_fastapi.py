from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="API CrossFit")

# Modelo de dados
class Atleta(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    peso: float
    altura: float

# Banco de dados simulado
atletas_db: List[Atleta] = []

# Criar atleta
@app.post("/atletas/", response_model=Atleta)
async def criar_atleta(atleta: Atleta):
    atleta.id = len(atletas_db) + 1
    atletas_db.append(atleta)
    return atleta

# Listar todos os atletas
@app.get("/atletas/", response_model=List[Atleta])
async def listar_atletas():
    return atletas_db

# Buscar atleta por ID
@app.get("/atletas/{atleta_id}", response_model=Atleta)
async def buscar_atleta(atleta_id: int):
    for atleta in atletas_db:
        if atleta.id == atleta_id:
            return atleta
    raise HTTPException(status_code=404, detail="Atleta não encontrado")

# Atualizar atleta
@app.put("/atletas/{atleta_id}", response_model=Atleta)
async def atualizar_atleta(atleta_id: int, dados: Atleta):
    for idx, atleta in enumerate(atletas_db):
        if atleta.id == atleta_id:
            dados.id = atleta_id
            atletas_db[idx] = dados
            return dados
    raise HTTPException(status_code=404, detail="Atleta não encontrado")

# Deletar atleta
@app.delete("/atletas/{atleta_id}")
async def deletar_atleta(atleta_id: int):
    for idx, atleta in enumerate(atletas_db):
        if atleta.id == atleta_id:
            del atletas_db[idx]
            return {"detail": "Atleta deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Atleta não encontrado")

# Executar a API com: uvicorn crossfit_api_fastapi:app --reload
