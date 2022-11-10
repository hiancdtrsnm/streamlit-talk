import streamlit as st
import qrcode

def generate_url_qr(url = "http://192.168.0.61:8501"):
    img = qrcode.make(url)
    st.image(img._img, caption="URL de la presentación", width=400)