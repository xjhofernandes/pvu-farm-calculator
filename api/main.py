from datetime import timedelta
from dateutil.parser import parse
import pandas as pd

def calcular_frequencia_ganhos(frequencia: int, producao: int, custo_total: int, data_inicio_str: str = "20180101"):
    data_inicio = parse(data_inicio_str)
    dias = [7, 14, 30]
    
    listagem_frequencia_ganhos = []
    
    for dia in dias:
        ciclo = list(pd.date_range(start=data_inicio, end=data_inicio + timedelta(days=dia), freq=f"{frequencia}H"))
        ciclo.pop(0)
        valor_produzido = producao * len(ciclo)
        valor_custo = custo_total * len(ciclo)
        valor_lucro = valor_produzido - valor_custo
        
        listagem_frequencia_ganhos.append({"frequencia": f"{dia}d", "produzido": valor_produzido, "custo": valor_custo, "lucro": valor_lucro})
    
    datas_colheitas = [a.to_pydatetime() for a in ciclo]
    
    saida = {"frequencia_ganhos": listagem_frequencia_ganhos,
             "datas_colheitas": datas_colheitas
            }
    
    return saida


def obter_frequencia_total(listagem_time: list, data_inicio_str: str) -> list:
    lista = []

    for x in listagem_time:
        lista.extend(calcular_frequencia_ganhos(x["horas_producao"], x["producao"], x["custo_total"], data_inicio_str)["frequencia_ganhos"])
    
    lista_df = pd.DataFrame(lista)

    lista_saida = lista_df.groupby("frequencia").sum().reset_index().to_dict("records")
    
    return lista_saida