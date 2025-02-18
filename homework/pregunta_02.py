"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd
import os

def pregunta_02():
     """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4
     """
    
     script_path = os.path.dirname(os.path.abspath(__file__))
     tsv_path = os.path.join(script_path, "..", "files\input", "tbl0.tsv")

     # Lee el archivo TSV utilizando pandas
     df = pd.read_csv(tsv_path, sep="\t")

     # Retorna la cantidad de columnas, que es la segunda dimensión del shape
     return df.shape[1]