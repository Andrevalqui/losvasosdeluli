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

# 2. DATOS (Igual a como los tenías)
INFO = {
    "nombre": "Los Vasos de Luli",
    "ubicacion": "Repostería Artesanal",
    "descripcion": "Transformamos ingredientes seleccionados en obras de arte comestibles. Especialistas en repostería fina de autor para momentos inolvidables.",
    "whatsapp": "51977905037",
    "instagram": "https://www.instagram.com/losvasosdeluli7/",
    "facebook": "https://www.facebook.com/profile.php?id=61568275415704",
    "tiktok": "https://www.tiktok.com/@losvasosdeluli7"
}

# 3. LÓGICA DE RUTAS GITHUB (Para que las fotos carguen en el servidor)
# Reemplaza 'Andrevalqui' y 'losvasosdeluli' si tus nombres en GitHub son diferentes
USER = "Andrevalqui"
REPO = "losvasosdeluli"
BASE_URL = f"https://raw.githubusercontent.com/{USER}/{REPO}/main"

# Buscamos las fotos en tu carpeta static/img
gallery_items = ""
img_folder = "static/img"
if os.path.exists(img_folder):
    for foto in os.listdir(img_folder):
        if foto.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            url_full = f"{BASE_URL}/static/img/{foto}"
            gallery_items += f'<div class="swiper-slide"><div class="photo-frame"><img src="{url_full}"></div></div>'

# Buscamos el video
video_final = f"{BASE_URL}/static/video/postres.mp4"

# 4. CARGAR INDEX.HTML Y REEMPLAZAR VARIABLES
def cargar_web():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        html = f.read()
        # Inyectamos la galería y el video dinámico
        html = html.replace("{{ gallery_content }}", gallery_items)
        html = html.replace("{{ video_path }}", video_final)
        # Inyectamos el resto de info
        for clave, valor in INFO.items():
            html = html.replace(f"{{{{ {clave} }}}}", str(valor))
        return html

# 5. RENDER FINAL
st.components.v1.html(cargar_web(), height=2500, scrolling=False)
