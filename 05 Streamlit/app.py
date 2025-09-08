import streamlit as st

pages = [
    st.Page("paginas/introduccion.py",
            title="Introducción a la problemática"),
    st.Page("paginas/estudios.py",
            title="Estudios consultados"),
    st.Page("paginas/adicional.py",
            title="Información adicional"),
    st.Page("paginas/formulario.py",
            title="Formulario de..."),
    st.Page("paginas/resultados.py",
            title="Resultados del estudio"),
    st.Page("paginas/referencias.py",
            title="Referencias consultadas")
    ]

pg = st.navigation(pages)

pg.run()