import streamlit as st
import qrcode
from datetime import datetime

st.title("Generador de QR++")

text = st.text_input("Texto a codificar", "example.com")

col1, col2, col3, col4 = st.columns(4)
with col1:
    box_size = st.number_input("Tamaño del cuadro", 1, 20, 10)

with col2:
    border = st.number_input("Tamaño del borde", 1, 20, 4)

with col3:
    fill_color = st.color_picker("Color de relleno", "#FF0000")

with col4:
    back_color = st.color_picker("Color de fondo", "#0000FF")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=box_size,
    border=border,
)

qr.add_data(text)
qr.make(fit=True)

img = qr.make_image(fill_color=fill_color, back_color=back_color)

st.image(img._img, caption="QR Code")

filename = f"../qrs/qrcode-{datetime.now()}.png"
img.save(filename)

st.download_button("Descargar", open(filename, 'rb').read(), "qrcode.png")

if st.checkbox("Mostrar código"):
    st.code("""
import streamlit as st
import qrcode
from datetime import datetime

st.title("Generador de QR++")

text = st.text_input("Texto a codificar", "example.com")

col1, col2, col3, col4 = st.columns(4)
with col1:
    box_size = st.number_input("Tamaño del cuadro", 1, 20, 10)

with col2:
    border = st.number_input("Tamaño del borde", 1, 20, 4)

with col3:
    fill_color = st.color_picker("Color de relleno", "#FF0000")

with col4:
    back_color = st.color_picker("Color de fondo", "#0000FF")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=box_size,
    border=border,
)

qr.add_data(text)
qr.make(fit=True)

img = qr.make_image(fill_color=fill_color, back_color=back_color)

st.image(img._img, caption="QR Code")

filename = f"../qrs/qrcode-{datetime.now()}.png"
img.save(filename)

st.download_button("Descargar", open(filename, 'rb').read(), "qrcode.png")

    
    """)
