import streamlit as st
from cubamap import cuba_mun_map

st.title('Mapa de Cuba por municipios')

color = st.slider("Color", 0.1, 1.0, 0.1, 0.01)

mun_data = {
    "21.01": color,
    "21.02": color,
    "21.03": color,
    "21.04": color,
    "21.05": color,
    "22.11": color,
    "23.12": color,
    "23.13": color,
    "23.14": color,
    "23.15": color,
    "24.01": color,
    "24.02": color,
    "24.03": color,
    "24.06": color,
    "24.07": color,
    "24.08": color,
    "24.09": color,
    "23.01": color,
}

point = cuba_mun_map(mun_map=mun_data)

st.write(f'El punto seleccionado es {point}')

"[Código fuente](https://github.com/hiancdtrsnm/cubamap)"

st.code("""
import streamlit as st
from cubamap import cuba_mun_map

st.title('Mapa de Cuba por municipios')

color = st.slider("Color", 0.1, 1.0, 0.1, 0.01)

mun_data = {
    "21.01": color,
    "21.02": color,
    "21.03": color,
    "21.04": color,
    "21.05": color,
    "22.11": color,
    "23.12": color,
    "23.13": color,
    "23.14": color,
    "23.15": color,
    "24.01": color,
    "24.02": color,
    "24.03": color,
    "24.06": color,
    "24.07": color,
    "24.08": color,
    "24.09": color,
    "23.01": color,
}

point = cuba_mun_map(mun_map=mun_data)

st.write(f'El punto seleccionado es {point}')

"[Código fuente](https://github.com/hiancdtrsnm/cubamap)"

""")