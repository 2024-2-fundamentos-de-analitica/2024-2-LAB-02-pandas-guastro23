"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import os
import pandas as pd

def pregunta_01():
     """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40
     """
  
     script_path = os.path.dirname(os.path.abspath(__file__))
     tsv_path = os.path.join(script_path, "..", "files\\input", "tbl0.tsv")

     # Lee el archivo .tsv usando pandas
     df = pd.read_csv(tsv_path, sep="\t")

     # Retorna el número de filas
     return df.shape[0]
