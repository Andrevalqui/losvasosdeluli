import streamlit as st
import os

st.set_page_config(page_title="Los Vasos de Luli", layout="wide")

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0px !important;}
        iframe {border: none !important; width: 100%;}
    </style>
""", unsafe_allow_html=True)

INFO = {
    "nombre": "Los Vasos de Luli",
    "ubicacion": "Repostería Artesanal",
    "descripcion": "Transformamos ingredientes seleccionados en obras de arte comestibles. Especialistas en repostería fina de autor para momentos inolvidables.",
    "whatsapp": "51977905037",
    "instagram": "https://www.instagram.com/losvasosdeluli7/",
    "facebook": "https://www.facebook.com/profile.php?id=61568275415704",
    "tiktok": "https://www.tiktok.com/@losvasitosdeluli7?fbclid=IwY2xjawPQn_5leHRuA2FlbQIxMABicmlkETFkUGF2aHdqM1V4a0gwMXJ0c3J0YwZhcHBfaWQQMjIyMDM5MTc4ODIwMDg5MgABHh7Br_jKbR-eLmTiOeDiEEnvkY37IKpR4z5Ax2g7aZ86PEknNxQRPHg15i30_aem_3tTP-g9zBqMhGcVMaCZknw"
}

USER = "Andrevalqui"
REPO = "losvasosdeluli"
BASE_URL = f"https://raw.githubusercontent.com/{USER}/{REPO}/main"

gallery_items = ""
img_folder = "static/img"
if os.path.exists(img_folder):
    for foto in os.listdir(img_folder):
        if foto.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            url_full = f"{BASE_URL}/static/img/{foto}"
            gallery_items += f'<div class="swiper-slide"><div class="photo-frame"><img src="{url_full}"></div></div>'

video_final = f"{BASE_URL}/static/video/postres.mp4"

def cargar_web():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        html = f.read()
        html = html.replace("{{ gallery_content }}", gallery_items)
        html = html.replace("{{ video_path }}", video_final)
        for clave, valor in INFO.items():
            html = html.replace(f"{{{{ {clave} }}}}", str(valor))
        return html

# Reducimos la altura a 100vh para que se adapte al navegador del usuario
st.components.v1.html(cargar_web(), height=1000, scrolling=True)
