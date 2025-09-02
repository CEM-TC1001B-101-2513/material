import streamlit as st

st.header("Introducción a la problemática")

st.write("""
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Donec pretium, felis sed tincidunt dignissim, risus elit
consectetur lorem, ac vestibulum erat orci sit amet velit.
Suspendisse aliquet magna eget condimentum ornare.
In vitae dictum mauris. Suspendisse rutrum nulla vel
est scelerisque, sit amet iaculis purus lacinia.
Quisque enim quam, ultricies in iaculis eu,
efficitur at lorem. Praesent ante tellus,
laoreet et egestas quis, tincidunt eget ex.
Cras ac hendrerit tortor.
Curabitur pulvinar gravida urna id blandit.
Nullam et ipsum vel ipsum vulputate maximus.
Sed eu lacinia lacus.
""")

st.markdown("""
# Encabezado
## Sub encabezado
### Sub sub encabezado
---
#### Listado ordenado:
1. Primer elemento
2. Segundo elemento
3. Tercer elemento
#### Listado no ordenado
- Primer elemento
- Segundo elemento
- Tercer elemento

#### Lista de varios niveles
1. Primer elemento
    - Primer subelemento
2. Segundo elemento
    - Segundo subelemento
    
### Enlaces
Enlace a Canvas: https://experiencia21.tec.mx/courses/623237

[Canvas](https://experiencia21.tec.mx/courses/623237)

### Formatos
:blue[Este texto es azul]

:red-background[Este texto tiene un fondo rojo]

:red-background[:blue[Texto azul con fondo rojo]]

*Cursivas*
**Negritas**
***Cursivas y negritas***

### Símbolos
->, <-, ==, >=, <=, !=

### Emojis
Bamboo :bamboo:

Material icons :material/Home:

### Latex (ecuaciones)
$$\sum_{k=1}^{n}x^{2}-3x+5$$

### Tablas
| # | Elemento | Descripción |
| --- | --- | --- |
| 1 | Primer elemento | Primera descripción |
| 2 | Segundo elemento | Segunda descripción |
| 3 | Tercer elemento | Tercera descripción |
""")

lista = [
    ["#", "Elemento", "Descripción"],
    ["1", "Primer elemento", "Primera descripción"],
    ["2", "Segundo elemento", "Segunda descripción"],
    ["3", "Tercer elemento", "Tercera descripción"],
    ]
st.table(lista)

st.image("imagenes/pexels-chevanon-1108099.jpg")
st.caption("Imagen tomada de: https://www.pexels.com/photo/two-yellow-labrador-retriever-puppies-1108099/")

# Crea dos columnas del mismo tamaño
c1, c2 = st.columns(2)
c1.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec pretium, felis sed tincidunt dignissim, risus elit consectetur lorem, ac vestibulum erat orci sit amet velit. Suspendisse aliquet magna eget condimentum ornare. In vitae dictum mauris. Suspendisse rutrum nulla vel est scelerisque, sit amet iaculis purus lacinia. Quisque enim quam, ultricies in iaculis eu, efficitur at lorem. Praesent ante tellus, laoreet et egestas quis, tincidunt eget ex. Cras ac hendrerit tortor. Curabitur pulvinar gravida urna id blandit. Nullam et ipsum vel ipsum vulputate maximus. Sed eu lacinia lacus.")
c2.image("imagenes/pexels-chevanon-1108099.jpg")
c2.caption("Imagen tomada de: https://www.pexels.com/photo/two-yellow-labrador-retriever-puppies-1108099/")

c3, c4 = st.columns([0.7, 0.3])
c3.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec pretium, felis sed tincidunt dignissim, risus elit consectetur lorem, ac vestibulum erat orci sit amet velit. Suspendisse aliquet magna eget condimentum ornare. In vitae dictum mauris. Suspendisse rutrum nulla vel est scelerisque, sit amet iaculis purus lacinia. Quisque enim quam, ultricies in iaculis eu, efficitur at lorem. Praesent ante tellus, laoreet et egestas quis, tincidunt eget ex. Cras ac hendrerit tortor. Curabitur pulvinar gravida urna id blandit. Nullam et ipsum vel ipsum vulputate maximus. Sed eu lacinia lacus.")
c4.image("imagenes/pexels-chevanon-1108099.jpg")
c4.caption("Imagen tomada de: https://www.pexels.com/photo/two-yellow-labrador-retriever-puppies-1108099/")

st.video("https://www.youtube.com/watch?v=qf7ws2DF-zk")