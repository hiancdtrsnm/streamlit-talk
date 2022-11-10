import streamlit as st
from common import generate_url_qr
import os

os.makedirs("../qrs", exist_ok=True)

col1, col2 = st.columns([.8, .2])

with col1:
    "# Streamlit, de scripts al Dashboard sin esfuerzo"
    "Hian Cañizares 🇨🇺, Noviembre 2022"
    "Estoy en [Twitter](https://twitter.com/hian_cd) y [GitHub](https://github.com/hiancdtrsnm)"

with col2:
    st.image("../img/streamlitlogo.png", width=250)

generate_url_qr()

"""# ⚠️ Aviso ⚠️
Esta presentación es altamente interactiva, por lo que el autor no se hace responsable de tener que hacer algun hotfix en el código para que funcione correctamente.
"""