from pydantic import BaseModel
from datetime import datetime

class Plant(BaseModel):
    tipo: str
    producao: int
    horas_producao: int
    custo_total: int
    nft: bool
    moeda: str