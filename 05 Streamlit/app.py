import streamlit as st

pages = [
    st.Page("paginas/introduccion.py",
            title="Introducción a la problemática"),
    st.Page("paginas/estudios.py",
            title="Estudios consultados")
    ]

pg = st.navigation(pages)

pg.run()