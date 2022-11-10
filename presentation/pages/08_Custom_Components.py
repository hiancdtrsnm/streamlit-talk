import streamlit as st
import streamlit.components.v1 as components
import os

"# Listando los QR que hemos generado"

ans = "\n".join([f"<li> {file} </li>" for file in os.listdir("../qrs")])

components.html(f"<ul>\n{ans}\n</ul>", scrolling=True)

"[Documentación de Streamlit Components](https://docs.streamlit.io/library/components/components-api)"

st.code(
    """
import streamlit as st
import streamlit.components.v1 as components
import os

"# Listando los QR que hemos generado"

ans = "\n".join([f"<li> {file} </li>" for file in os.listdir("../qrs")])

components.html(f"<ul>\n{ans}\n</ul>", scrolling= True)

""", language="python"
)
