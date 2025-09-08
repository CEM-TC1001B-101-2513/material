import streamlit as st

st.header("Formulario")

form = st.form(key="formulario")

# Recuerden que deben minimizar las preguntas abiertas
# Si alguna pregunta que dejaron abierta que pudo
# ser cerrada, está mal

# Evitar lo más posible
nombre = form.text_input("Etiqueta", "Placeholder")

edad = form.number_input("Edad",
                         min_value=0,
                         max_value=120,
                         value=18,
                         step=1)

edad_slider = form.slider("Edad",
                          min_value=0,
                          max_value=120,
                          value=18,
                          step=1)


recibir = form.radio("¿Desea recibir notificaciones?",
                     options=["Sí", "No"], # Listado de opciones
                     index=0) # Opción pre-seleccionada
                   
estados_mexico = [
    "Aguascalientes",
    "Baja California",
    "Baja California Sur",
    "Campeche",
    "Chiapas",
    "Chihuahua",
    "Ciudad de México",
    "Coahuila",
    "Colima",
    "Durango",
    "Estado de México",
    "Guanajuato",
    "Guerrero",
    "Hidalgo",
    "Jalisco",
    "Michoacán",
    "Morelos",
    "Nayarit",
    "Nuevo León",
    "Oaxaca",
    "Puebla",
    "Querétaro",
    "Quintana Roo",
    "San Luis Potosí",
    "Sinaloa",
    "Sonora",
    "Tabasco",
    "Tamaulipas",
    "Tlaxcala",
    "Veracruz",
    "Yucatán",
    "Zacatecas"
]

estado = form.selectbox("Estado de la república",
                        options=estados_mexico,
                        index=0)

form.text("Tipos de comidas que prefieres:")

pizza = form.checkbox("Pizza")
sushi = form.checkbox("Sushi")
hamburguesa = form.checkbox("Hamburguesa")
tacos = form.checkbox("Tacos")






