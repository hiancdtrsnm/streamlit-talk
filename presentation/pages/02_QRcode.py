import streamlit as st
import qrcode
from datetime import datetime

st.title("Generador de QR")

text = st.text_input("Texto a codificar", "example.com")

if '@' not in text:
    st.error("El texto debe contener un @")
    st.stop()

text
f'# {text}'

img = qrcode.make(text)

st.image(img._img, caption="QR Code")

filename = f"../qrs/qrcode-{datetime.now()}.png"
img.save(filename)

st.download_button("Descargar", open(filename, 'rb').read(), "qrcode.png")

if st.checkbox("Mostrar código"):
    st.code("""
import streamlit as st
import qrcode
from datetime import datetime

st.title("Generador de QR")

text = st.text_input("Texto a codificar", "example.com")

text
f'# {text}'


img = qrcode.make(text)

st.image(img._img, caption="QR Code")

filename = f"../qrs/qrcode-{datetime.now()}.png"
img.save(filename)

st.download_button("Descargar", open(filename, 'rb').read(), "qrcode.png")

    
    """)
