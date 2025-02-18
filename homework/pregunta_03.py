"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd
import os

def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
     c1
     A     8
     B     7
     C     5
     D     6
     E    14
    Name: count, dtype: int64
     """
     
    script_path = os.path.dirname(os.path.abspath(__file__))
    tsv_path = os.path.join(script_path, "..", "files\input", "tbl0.tsv")
    
     # Leer el archivo tsv usando pandas
    df = pd.read_csv(tsv_path, sep="\t")
    
     # Agrupar por la columna 'c1' y contar los registros
    resultado = df.groupby("c1").size().rename("count")
    
    return resultado

