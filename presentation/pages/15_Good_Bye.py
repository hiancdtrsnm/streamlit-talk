import streamlit as st

st.title("👋")

col1, col2 = st.columns([0.4, 0.6])

with col1:
    st.image("../img/streamlitmeme.png")

with col2:
    "## Preguntas?"


    "[link a la presentación](https://github.com/hiancdtrsnm/streamlit-presentation)"
    st.download_button("Descargar presentación", open("../streamlit-python-valencia.zip", 'rb').read(), "streamlit-python-valencia.zip")

    "Mi twitter: [@hian_cd](https://twitter.com/hian_cd)"

"""
Para seguir con Streamlit:

http://awesome-streamlit.org/


https://streamlit.io/


https://docs.streamlit.io/
"""