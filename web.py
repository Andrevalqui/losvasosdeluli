import streamlit as st
import os

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Los Vasos de Luli | Repostería", layout="wide")

# Ocultar menús de Streamlit
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0px !important;}
        iframe {border: none !important;}
    </style>
""", unsafe_allow_html=True)

# 2. DATOS
INFO = {
    "nombre": "Los Vasos de Luli",
    "ubicacion": "Repostería Artesanal",
    "descripcion": "Transformamos ingredientes seleccionados en obras de arte comestibles. Especialistas en repostería fina de autor para momentos inolvidables.",
    "whatsapp": "51977905037",
    "instagram": "https://www.instagram.com/losvasosdeluli7/",
    "facebook": "https://www.facebook.com/profile.php?id=61568275415704",
    "tiktok": "https://www.tiktok.com/@losvasosdeluli7"
}

# 3. LÓGICA PARA CARGAR ARCHIVOS DE GITHUB
# Reemplaza 'Andrevalqui' y 'losvasosdeluli' si cambian los nombres
BASE_GITHUB = "https://raw.githubusercontent.com/Andrevalqui/losvasosdeluli/main"

# Generar HTML de la galería dinámicamente
gallery_html = ""
img_path = "static/img"
if os.path.exists(img_path):
    archivos = os.listdir(img_path)
    for foto in archivos:
        if foto.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            url_foto = f"{BASE_GITHUB}/static/img/{foto}"
            gallery_html += f'<div class="swiper-slide"><div class="photo-frame"><img src="{url_foto}"></div></div>'

# Link del video
video_url = f"{BASE_GITHUB}/static/video/postres.mp4"

# 4. CARGAR Y PROCESAR INDEX.HTML
def cargar_index():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        html = f.read()
        # Inyectar Galería y Video
        html = html.replace("{{ gallery }}", gallery_html)
        html = html.replace("{{ video_url }}", video_url)
        # Inyectar INFO
        for clave, valor in INFO.items():
            html = html.replace(f"{{{{ {clave} }}}}", str(valor))
        return html

# 5. RENDER
st.components.v1.html(cargar_index(), height=2200, scrolling=False)
