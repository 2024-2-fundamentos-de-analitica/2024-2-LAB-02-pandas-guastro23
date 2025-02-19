"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd
import os

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    script_path = os.path.dirname(os.path.abspath(__file__))
    tbl0_path = os.path.join(script_path, "..", "files", "input", "tbl0.tsv")
    tbl2_path = os.path.join(script_path, "..", "files", "input", "tbl2.tsv")
    
    # Leer los archivos
    df0 = pd.read_csv(tbl0_path, sep="\t")
    df2 = pd.read_csv(tbl2_path, sep="\t")
    
    # Unir ambos dataframes usando c0 como clave
    df_merged = pd.merge(df0, df2, on="c0")
    
    # Agrupar por c1 (de tbl0) y sumar los valores de c5b (de tbl2)
    resultado = df_merged.groupby("c1")["c5b"].sum()
    
    return resultado

