from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Plant(BaseModel):
    tipo: str
    producao: int
    horas_producao: int
    custo_total: int
    nft: bool
    moeda: Optional[str] = None