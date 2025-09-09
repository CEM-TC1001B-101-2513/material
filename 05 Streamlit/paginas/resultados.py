import pandas as pd
import streamlit as st

def cargar_resultados(nombre):
    df = pd.read_csv(nombre)
    return df

df = cargar_resultados("datos/resultados.csv")

st.header("Resultados de nuestra encuesta")

st.write("Hablar de mi encuesta...")

# st.dataframe(df) # Desplegar todos los resultados
st.dataframe(df.tail(10)) # Desplegar las últimas 10 filas