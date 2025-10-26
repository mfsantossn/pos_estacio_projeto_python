# src/app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from typing import Dict, Any

# --- Configuração ---
STATS_PATH = "stats.json" # Caminho para o arquivo gerado

# --- Modelo Pydantic para o POST /soma ---
class SomaRequest(BaseModel):
    """Define o formato de entrada para o endpoint /soma."""
    x: float
    y: float

# --- Instância da API ---
app = FastAPI(
    title="Mini-Projeto Integrado Python",
    description="API com estatísticas (Pandas) e desafio FP.",
    version="1.0.0"
)

# --- Funções Auxiliares ---
def load_stats() -> Dict[str, Any]:
    """Tenta carregar o stats.json."""
    try:
        with open(STATS_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # Se o arquivo não existir, retorna um erro 500
        raise HTTPException(
            status_code=500,
            detail="stats.json não encontrado. Execute o make_stats.py primeiro!"
        )
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500,
            detail="Erro ao ler stats.json. Arquivo corrompido ou mal formatado."
        )

# --- Endpoints ---

@app.get("/health", summary="Status", tags=["Geral"])
def get_health():
    """Verifica se a API está online."""
    return {"status": "ok"}

@app.get("/stats.json", summary="Estatísticas e FP", tags=["Dados"])
def get_stats():
    """Retorna o conteúdo de stats.json."""
    return load_stats()

@app.post("/soma", summary="Calculadora", tags=["Utilidade"])
def post_soma(data: SomaRequest):
    """Recebe x e y e retorna a soma."""
    resultado = data.x + data.y
    return {"resultado": round(resultado, 2)}