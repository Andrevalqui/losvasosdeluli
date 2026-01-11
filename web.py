import streamlit as st
import os
from datetime import datetime

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Los Vasos de Luli | Repostería Artesanal", layout="wide")

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

# 2. DATOS DE LA EMPRESA
INFO = {
    "nombre": "Los Vasos de Luli",
    "ubicacion": "Repostería Artesanal",
    "descripcion": "Transformamos ingredientes seleccionados en obras de arte comestibles. Especialistas en repostería fina de autor para momentos inolvidables.",
    "whatsapp": "51977905037",
    "instagram": "https://www.instagram.com/losvasosdeluli7/",
    "facebook": "https://www.facebook.com/profile.php?id=61568275415704",
    "tiktok": "https://www.tiktok.com/@losvasosdeluli7",
    "mapa_link": "https://www.google.com/maps" # Puedes cambiarlo por tu ubicación real
}

SERVICIOS = [
    {"icono": "fa-ice-cream", "nombre": "Postres en Vaso"},
    {"icono": "fa-birthday-cake", "nombre": "Tortas de Autor"},
    {"icono": "fa-box-open", "nombre": "Cajas de Regalo"},
    {"icono": "fa-cookie-bite", "nombre": "Petit Fours"},
    {"icono": "fa-truck", "nombre": "Delivery Seguro"},
    {"icono": "fa-certificate", "nombre": "Calidad Gourmet"},
]

TESTIMONIOS = [
    {"nombre": "Valeria S.", "comentario": "La choco fresa fue el centro de atención en mi evento. ¡Increíble!"},
    {"nombre": "Marco R.", "comentario": "El mejor postre que he probado. La presentación es impecable."},
    {"nombre": "Empresa TechX", "comentario": "Nuestros clientes quedaron fascinados con los detalles."}
]

# 3. LÓGICA DE RUTAS GITHUB (Para que las fotos carguen siempre)
USER = "Andrevalqui"
REPO = "losvasosdeluli"
BASE_URL = f"https://raw.githubusercontent.com/{USER}/{REPO}/main"

# Generar HTML de la galería
gallery_html = ""
img_folder = "static/img"
if os.path.exists(img_folder):
    for foto in os.listdir(img_folder):
        if foto.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            url_full = f"{BASE_URL}/static/img/{foto}"
            gallery_html += f'''
                <div class="swiper-slide">
                    <div class="photo-frame shadow-sm">
                        <a href="{url_full}" class="glightbox">
                            <img src="{url_full}" class="img-fluid w-100" style="height: 400px; object-fit: cover; border-radius: 8px;">
                        </a>
                    </div>
                </div>'''

# Link del video
video_path = f"{BASE_URL}/static/video/postres.mp4"

# 4. PROCESAR EL HTML
def cargar_web():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        html = f.read()
        
        # Inyectar Listas (Servicios y Testimonios)
        serv_html = "".join([f'<div class="col-md-4 col-6" data-aos="fade-up"><div class="service-card p-4 bg-white rounded shadow-sm h-100"><i class="fas {s["icono"]} fa-2x text-pink mb-3"></i><h6 class="text-uppercase small fw-bold">{s["nombre"]}</h6></div></div>' for s in SERVICIOS])
        test_html = "".join([f'<div class="col-md-4 mb-4" data-aos="fade-up"><div class="review-box p-4 border border-secondary rounded h-100 text-white"><div class="stars mb-2 text-warning">★★★★★</div><p class="fst-italic opacity-75">"{t["comentario"]}"</p><small class="text-uppercase text-pink">{t["nombre"]}</small></div></div>' for t in TESTIMONIOS])
        
        html = html.replace("{{ servicios_items }}", serv_html)
        html = html.replace("{{ testimonios_items }}", test_html)
        html = html.replace("{{ gallery_content }}", gallery_html)
        html = html.replace("{{ video_url }}", video_path)
        
        # Inyectar Info básica
        for clave, valor in INFO.items():
            html = html.replace(f"{{{{ {clave} }}}}", str(valor))
        
        html = html.replace("{{ anio }}", str(datetime.now().year))
        return html

# 5. RENDER
st.components.v1.html(cargar_web(), height=2500, scrolling=False)
