import pandas as pd
import streamlit as st

@st.cache_data
def cargar_datos_csv(nombre_archivo):
    df = pd.read_csv(nombre_archivo)
    return df

@st.cache_data
def cargar_datos_excel(nombre_archivo):
    df = pd.read_excel(nombre_archivo)
    return df

df1 = cargar_datos_csv("datos/CIAD_4_acreditaciones.csv")
df2 = cargar_datos_excel("datos/Calificaciones.xlsx")
df3 = cargar_datos_csv("datos/estados_mexico_centroides.csv")

st.header("Estudios sobre la problemática")

st.dataframe(df1.head(10))

st.dataframe(df2)

st.write("Introducción al estudio....")

st.bar_chart(df2, x="Nombre", y="Calificación")

st.scatter_chart(df2, x="Calificación", y="Calificación")

st.write("Justificación o reflexión de por qué son relevantes los datos...")

st.dataframe(df3)

st.map(df3, latitude="Latitud", longitude="Longitud")



