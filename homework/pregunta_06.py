"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd
import os

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']
     """
    script_path = os.path.dirname(os.path.abspath(__file__))
    tsv_path = os.path.join(script_path, "..", "files", "input", "tbl1.tsv")
    
    # Leer el archivo tsv
    df = pd.read_csv(tsv_path, sep="\t")
    
    # Obtener los valores únicos en mayúsculas y ordenarlos alfabéticamente
    unique_vals = sorted(df["c4"].str.upper().unique())
    
    return unique_vals



