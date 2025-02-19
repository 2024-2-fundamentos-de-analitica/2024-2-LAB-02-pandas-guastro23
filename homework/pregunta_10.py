"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd
import os

def pregunta_10():
    """
    Construya una tabla que contenga `c1` y una lista separada por ':' de los
    valores de la columna `c2` para el archivo `tbl0.tsv`.

    Rta/
                                 c2
    c1
    A               1:1:2:3:6:7:8:9
    B                 1:3:4:5:6:8:9
    C                     0:5:6:7:9
    D                   1:2:3:5:5:7
    E   1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    script_path = os.path.dirname(os.path.abspath(__file__))
    tsv_path = os.path.join(script_path, "..", "files\\input", "tbl0.tsv")
    
    # Leer el archivo TSV
    df = pd.read_csv(tsv_path, sep="\t")
    
    # Agrupar por c1 y, para cada grupo, ordenar numéricamente los valores de c2
    # y unirlos con ':'.
    df_grouped = df.groupby("c1")["c2"].apply(
        lambda x: ":".join(map(str, sorted(x)))
    ).to_frame()
    
    # Ajustar el nombre del índice a _c1
    df_grouped.index.name = "_c1"
    
    return df_grouped

